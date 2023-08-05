""" HuggingFace CLIP Model

The Text Encoder is loaded from Huggingface.
"""
from collections import OrderedDict
from dataclasses import dataclass
import logging
import math
from typing import Tuple, Union, Callable, Optional

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.checkpoint import checkpoint

from open_clip.timm_model import TimmModel
from open_clip.utils import freeze_batch_norm_2d, to_2tuple

from transformers import AutoTokenizer, AutoModel

from .config import CLIPTextCfg, CLIPVisionCfg
from .utils import concat_all_gather
from .blocks import Bottleneck, AttentionPool2d, ModifiedResNet, LayerNorm, QuickGELU, ResidualAttentionBlock,\
                    Transformer, VisualTransformer, _get_bert_basemodel, TextLearnableEncoder


class MoCo_Text(nn.Module):
    def __init__(
            self,
            args,
            embed_dim: int,
            vision_cfg: CLIPVisionCfg,
            text_cfg: CLIPTextCfg,
            quick_gelu: bool = False,
    ):
        super().__init__()
        if isinstance(vision_cfg, dict):
            vision_cfg = CLIPVisionCfg(**vision_cfg)
        if isinstance(text_cfg, dict):
            text_cfg = CLIPTextCfg(**text_cfg)

        self.args = args
        self.context_length = text_cfg.context_length
        self.device = torch.device(args.device)

        # OpenAI models are pretrained w/ QuickGELU but native nn.GELU is both faster and more
        # memory efficient in recent PyTorch releases (>= 1.10).
        # NOTE: timm models always use native GELU regardless of quick_gelu flag.
        act_layer = QuickGELU if quick_gelu else nn.GELU

        if vision_cfg.timm_model_name:
            self.visual = TimmModel(
                vision_cfg.timm_model_name,
                pretrained=vision_cfg.timm_model_pretrained,
                pool=vision_cfg.timm_pool,
                proj=vision_cfg.timm_proj,
                embed_dim=embed_dim,
                image_size=vision_cfg.image_size
            )
            act_layer = nn.GELU  # so that text transformer doesn't use QuickGELU w/ timm models
        elif isinstance(vision_cfg.layers, (tuple, list)):
            vision_heads = vision_cfg.width * 32 // vision_cfg.head_width
            self.visual = ModifiedResNet(
                layers=vision_cfg.layers,
                output_dim=embed_dim,
                heads=vision_heads,
                image_size=vision_cfg.image_size,
                width=vision_cfg.width
            )
            self.visual_m = ModifiedResNet(
                layers=vision_cfg.layers,
                output_dim=embed_dim,
                heads=vision_heads,
                image_size=vision_cfg.image_size,
                width=vision_cfg.width
            )
        else:
            vision_heads = vision_cfg.width // vision_cfg.head_width
            self.visual = VisualTransformer(
                image_size=vision_cfg.image_size,
                patch_size=vision_cfg.patch_size,
                width=vision_cfg.width,
                layers=vision_cfg.layers,
                heads=vision_heads,
                mlp_ratio=vision_cfg.mlp_ratio,
                output_dim=embed_dim,
                act_layer=act_layer,
            )

        # self.text_encoder = self._get_bert_basemodel(bert_model_name='emilyalsentzer/Bio_ClinicalBERT', freeze_layers=None)
        if text_cfg.bert_model_name:
            self.textual = TextLearnableEncoder(args=args, embed_dim=embed_dim, text_cfg=text_cfg)
            self.textual_m = TextLearnableEncoder(args=args, embed_dim=embed_dim, text_cfg=text_cfg)
        else:
            self.text_encoder = Transformer(
                width=text_cfg.width,
                layers=text_cfg.layers,
                heads=text_cfg.heads,
                act_layer=act_layer,
            )

        self.logit_scale = nn.Parameter(torch.ones([]) * np.log(1 / 0.07))
        self.register_buffer('attn_mask', self.build_attention_mask(), persistent=False)

        self.init_parameters()

        # add new params in .yml config file
        self.K = text_cfg.QUEUE_SIZE
        self.m = text_cfg.MOMENTUM
        # create the img queue 
        self.register_buffer("img_queue", torch.randn(embed_dim, self.K))
        self.img_queue = nn.functional.normalize(self.img_queue, dim=0)
        self.register_buffer("img_queue_ptr", torch.zeros(1, dtype=torch.long))  # image queue points
        # create the text queue
        self.register_buffer("text_queue", torch.randn(embed_dim, self.K))
        self.text_queue = nn.functional.normalize(self.text_queue, dim=0)
        self.register_buffer("text_queue_ptr", torch.zeros(1, dtype=torch.long))  # text queue points


    def init_parameters(self):
        nn.init.constant_(self.logit_scale, np.log(1 / 0.07))

        if hasattr(self.visual, 'init_parameters'):
            self.visual.init_parameters()

        for param_q, param_k in zip(self.visual.parameters(), self.visual_m.parameters()):
            param_k.data.copy_(param_q.data)  # initialize
            param_k.requires_grad = False  # not update by gradient

        for param_q, param_k in zip(self.textual.parameters(), self.textual_m.parameters()):
            param_k.data.copy_(param_q.data)  # initialize
            param_k.requires_grad = False  # not update by gradient


    def build_attention_mask(self):
        # lazily create causal attention mask, with full attention between the vision tokens
        # pytorch uses additive attention mask; fill with -inf
        mask = torch.empty(self.context_length, self.context_length)
        mask.fill_(float("-inf"))
        mask.triu_(1)  # zero out the lower diagonal
        return mask

    def lock_image_tower(self, unlocked_groups=0, freeze_bn_stats=False):
        # lock image tower as per LiT - https://arxiv.org/abs/2111.07991
        self.visual.lock(unlocked_groups=unlocked_groups, freeze_bn_stats=freeze_bn_stats)

    @torch.jit.ignore
    def set_grad_checkpointing(self, enable=True):
        self.visual.set_grad_checkpointing(enable)
        self.transformer.grad_checkpointing = enable


    @torch.no_grad()
    def _momentum_update_key_encoder(self):
        """
        Momentum update of the key encoder for image modal
        """
        for param_q, param_k in zip(self.visual.parameters(), self.visual_m.parameters()):
            param_k.data = param_k.data * self.m + param_q.data * (1. - self.m)
        for param_q, param_k in zip(self.textual.parameters(), self.textual_m.parameters()):
            param_k.data = param_k.data * self.m + param_q.data * (1. - self.m)

    @torch.no_grad()
    def _dequeue_and_enqueue(self, keys, option='img'):
        # option in 
        # gather keys before updating queue
        if self.args.distributed:
            keys = concat_all_gather(keys)
        batch_size = keys.shape[0]

        # raise RuntimeError(self.img_queue.shape, keys.shape)  # [embed_dim(1024), self.K(9600)], [bs * gpu(128*2=256), embed_dim(1024)]
        if option == 'img':
            ptr = int(self.img_queue_ptr)
            assert self.K % batch_size == 0  # for simplicity
            # replace the keys at ptr (dequeue and enqueue)
            self.img_queue[:, ptr:ptr + batch_size] = keys.T
            ptr = (ptr + batch_size) % self.K  # move pointer
            self.img_queue_ptr[0] = ptr
        else:
            ptr = int(self.text_queue_ptr)
            assert self.K % batch_size == 0  # for simplicity
            # replace the keys at ptr (dequeue and enqueue)
            self.text_queue[:, ptr:ptr + batch_size] = keys.T
            ptr = (ptr + batch_size) % self.K  # move pointer
            self.text_queue_ptr[0] = ptr


    def encode_image(self, image):
        return self.visual(image)

    def encode_text(self, batch):
        return self.textual(batch)

    def forward(self, batch):
        image = batch["images"]
        image = image.to(device=self.device, non_blocking=True)
        # text = text.to(device=self.device, non_blocking=True)

        if (image is None) or (batch["bert_input"] is None):
            raise RuntimeError('Missing Image OR Text in the input')

        image_features_q = self.encode_image(image)
        image_features_q = F.normalize(image_features_q, dim=-1)

        text_output_q = self.encode_text(batch)
        text_output_q["text_features"] = F.normalize(text_output_q["text_features"], dim=-1)

        with torch.no_grad():  # no gradient to keys
            self._momentum_update_key_encoder()  # update img & text encoder

            # self._batch_shuffle_ddp(...)
            image_features_k = self.visual_m(image)
            image_features_k = F.normalize(image_features_k, dim=-1)

            text_output_k = self.textual_m(batch)
            text_output_k["text_features"] = F.normalize(text_output_k["text_features"], dim=-1)
        # End-With

        ## enqueue and dequeue
        self._dequeue_and_enqueue(image_features_k, option='img')
        self._dequeue_and_enqueue(text_output_k["text_features"], option='text')

        clip_prediction = dict.fromkeys([
            "image_features_q", "text_output_q",
            "image_features_k", "text_output_k",
            "img_queue", "text_queue",
            "logit_scale", "attentions"
        ], None)
        clip_prediction.update({
            "image_features_q": image_features_q, "text_output_q": text_output_q,
            "image_features_k": image_features_k, "text_output_k": text_output_k,
            "img_queue": self.img_queue, "text_queue": self.text_queue,
            "logit_scale": self.logit_scale.exp(),
        })
        return clip_prediction

    def extract(self):
        raise RuntimeError('not implemented')
