import json
import logging
import os
import pathlib
import re
from copy import deepcopy
from pathlib import Path
from typing import Optional, Tuple

import torch

from .model import CLIP, CLIP_MLM, CLIP_HuggingFace, CLIP_MLM_IMG, WenLan, MoCo_Img, MoCo_Text, \
    convert_weights_to_fp16, resize_pos_embed
from .openai import load_openai_model
from .pretrained import get_pretrained_url, download_pretrained
from .transform import image_transform


# _MODEL_CONFIG_PATHS = [Path(__file__).parent / f"model_configs/"]
_MODEL_CONFIG_PATHS = [Path("/remote-home/share/weixionglin/medclip/vlp/open_clip/src/open_clip/model_configs")]
_MODEL_CONFIG_PATHS = list(set(_MODEL_CONFIG_PATHS))  # remove duplicate paths
_MODEL_CONFIGS = {}  # directory (model_name: config) of model architecture configs


def _natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_.lower())]


def _rescan_model_configs():
    global _MODEL_CONFIGS

    config_ext = ('.json',)
    config_files = []
    for config_path in _MODEL_CONFIG_PATHS:
        if config_path.is_file() and config_path.suffix in config_ext:
            config_files.append(config_path)
        elif config_path.is_dir():
            for ext in config_ext:
                config_files.extend(config_path.rglob(f'*{ext}'))  # rglob recursively collect config files in the folder

    for cf in config_files:
        with open(cf, 'r') as f:
            model_cfg = json.load(f)
            if all(a in model_cfg for a in ('embed_dim', 'vision_cfg', 'text_cfg')):
                _MODEL_CONFIGS[cf.stem] = model_cfg

    _MODEL_CONFIGS = {k: v for k, v in sorted(_MODEL_CONFIGS.items(), key=lambda x: _natural_key(x[0]))}


_rescan_model_configs()  # initial populate of model config registry


def load_state_dict(checkpoint_path: str, map_location='cpu'):
    checkpoint = torch.load(checkpoint_path, map_location=map_location)
    if isinstance(checkpoint, dict) and 'state_dict' in checkpoint:
        state_dict = checkpoint['state_dict']
    else:
        state_dict = checkpoint
    if next(iter(state_dict.items()))[0].startswith('module'):
        state_dict = {k[7:]: v for k, v in state_dict.items()}
    return state_dict


def load_checkpoint(model, checkpoint_path, strict=True):
    state_dict = load_state_dict(checkpoint_path)
    resize_pos_embed(state_dict, model)
    incompatible_keys = model.load_state_dict(state_dict, strict=strict)
    return incompatible_keys


def create_model(
        args,
        precision: str = 'fp32',
        device: torch.device = torch.device('cpu'),
        jit: bool = False,
        force_quick_gelu: bool = False,
        pretrained_image: bool = False,
):
    model_name, pretrained = args.model, args.pretrained
    model_name = model_name.replace('/', '-')  # for callers using old naming with / in ViT names

    if pretrained.lower() == 'openai':
        logging.info(f'Loading pretrained {model_name} from OpenAI.')
        model = load_openai_model(model_name, device=device, jit=jit)
        # See https://discuss.pytorch.org/t/valueerror-attemting-to-unscale-fp16-gradients/81372
        if precision == "amp" or precision == "fp32":
            model = model.float()
    else:
        if model_name in _MODEL_CONFIGS:
            logging.info(f'Loading {model_name} model config.')
            model_cfg = deepcopy(_MODEL_CONFIGS[model_name])
            # NOTE assign bert_model_name to args, used in CsvDataset for HuggingFace + MLM
            args.bert_model_name = model_cfg['text_cfg']['bert_model_name']
            logging.info(f'{model_name} Loaded.')
        else:
            logging.error(f'Model config for {model_name} not found; available models {list_models()}.')
            raise RuntimeError(f'Model config for {model_name} not found.')

        if force_quick_gelu:
            # override for use of QuickGELU on non-OpenAI transformer models
            model_cfg["quick_gelu"] = True

        if pretrained_image:
            if 'timm_model_name' in model_cfg.get('vision_cfg', {}):
                # pretrained weight loading for timm models set via vision_cfg
                model_cfg['vision_cfg']['timm_model_pretrained'] = True
            else:
                assert False, 'pretrained image towers currently only supported for timm models'

        model_cfg['args'] = args
        args.clip_model = model_cfg["clip_model"]
        args.queue_size = model_cfg['text_cfg'].get("QUEUE_SIZE", None)

        if not model_cfg["clip_model"]:
            raise RuntimeError('please assign clip_model')

        model_class = {
            "CLIP": CLIP,
            # "CLIP_MLM": CLIP_MLM,
            "CLIP_MLM_IMG": CLIP_MLM_IMG,
            "CLIP_HuggingFace": CLIP_HuggingFace,
            "WenLan": WenLan,
            "MoCo_Img": MoCo_Img,
            "MoCo_Text": MoCo_Text,
        }[model_cfg["clip_model"]]
        # HACK 需要从 config.json 中传参(clip_model), 但是 model_class 中没有这个参数, 所以需要抛掉
        model_cfg.pop("clip_model")
        # model_cfg.pop("QUEUE_SIZE")
        # HACK
        model = model_class(**model_cfg)
        """
        if args.mlm and not args.hugging_face:  # MLM pretraining task, hand crafted TextEncoder
            model = CLIP_MLM(**model_cfg)
        if args.hugging_face:  # TextEncoder from HuggingFace, MLM available
            model = CLIP_HuggingFace(**model_cfg)
        if args.mlm + args.hugging_face == 0:  # vanilla CLIP
            model = CLIP(**model_cfg)
        """

        if pretrained:
            checkpoint_path = ''
            url = get_pretrained_url(model_name, pretrained)
            if url:
                checkpoint_path = download_pretrained(url)
            elif os.path.exists(pretrained):
                checkpoint_path = pretrained

            if checkpoint_path:
                logging.info(f'Loading pretrained {model_name} weights ({pretrained}).')
                load_checkpoint(model, checkpoint_path)
            else:
                logging.warning(f'Pretrained weights ({pretrained}) not found for model {model_name}.')
                raise RuntimeError(f'Pretrained weights ({pretrained}) not found for model {model_name}.')

        model.to(device=device)
        if precision == "fp16":
            assert device.type != 'cpu'
            convert_weights_to_fp16(model)

        if jit:
            model = torch.jit.script(model)

    return model


def create_model_and_transforms(
        args,
        precision: str = 'fp32',
        device: torch.device = torch.device('cpu'),
        jit: bool = False,
        force_quick_gelu: bool = False,
        pretrained_image: bool = False,
        mean: Optional[Tuple[float, ...]] = None,
        std: Optional[Tuple[float, ...]] = None,
):
    model_name, pretrained = args.model, args.pretrained
    model = create_model(
        args, precision, device, jit,
        force_quick_gelu=force_quick_gelu,
        pretrained_image=pretrained_image
    )
    preprocess_train = image_transform(
        args=args,
        image_size=model.visual.image_size,
        is_train=True,
        mean=mean,
        std=std,
    )
    preprocess_val = image_transform(
        args=args,
        image_size=model.visual.image_size,
        is_train=False,
        mean=mean,
        std=std
    )
    return model, preprocess_train, preprocess_val


def list_models():
    """ enumerate available model architectures based on config files """
    return list(_MODEL_CONFIGS.keys())


def add_model_config(path):
    """ add model config path or file and update registry """
    if not isinstance(path, Path):
        path = Path(path)
    _MODEL_CONFIG_PATHS.append(path)
    _rescan_model_configs()
