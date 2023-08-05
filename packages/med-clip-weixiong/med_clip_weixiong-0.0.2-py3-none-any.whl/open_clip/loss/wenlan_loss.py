import logging

import torch
import torch.nn as nn
from torch.nn import functional as F

from .utils import gather_features

class WenLan_Loss(nn.Module):

    def __init__(self, args, cache_labels=False):
        super().__init__()
        self.local_loss = args.local_loss
        self.gather_with_grad = args.gather_with_grad
        self.cache_labels = cache_labels
        self.rank = args.rank
        self.world_size = args.world_size
        self.use_horovod = args.horovod
        self.K = args.queue_size
        self.mlm = args.mlm

        # cache state
        self.prev_num_logits = 0
        self.labels = {}

    def forward(self, prediction):
        ########################################################################################################################
        # compute logits for image -> text
        # positive logits: Nx1
        logit_scale = prediction["logit_scale"]

        image_features_q, image_features_k = prediction['image_features_q'], prediction['image_features_k']
        text_output_q, text_output_k = prediction['text_output_q'], prediction['text_output_k']
        img_queue, text_queue = prediction['img_queue'], prediction['text_queue']

        i2t_l_pos = torch.einsum('nc,nc->n', [image_features_q, text_output_k["text_features"]]).unsqueeze(-1)
        # negative logits: NxK
        i2t_l_neg = torch.einsum('nc,ck->nk', [image_features_q, text_queue.clone().detach()])
        # logits: Nx(1+K)
        i2t_logits = torch.cat([i2t_l_pos, i2t_l_neg], dim=-1)
        i2t_logits *= logit_scale

        # compute logits for text -> image
        # positive logits: Nx1
        t2i_l_pos = torch.einsum('nc,nc->n', [text_output_q["text_features"], image_features_k]).unsqueeze(-1)
        # negative logits: NxK
        t2i_l_neg = torch.einsum('nc,ck->nk', [text_output_q["text_features"], img_queue.clone().detach()])
        # logits: Nx(1+K)
        t2i_logits = torch.cat([t2i_l_pos, t2i_l_neg], dim=-1)
        t2i_logits *= logit_scale

        ### multi-label
        batch_size = image_features_q.shape[0]
        mask = torch.zeros((batch_size, self.K)).bool().cuda()  # <B, K>
        mask = torch.cat([torch.ones((batch_size, 1), dtype=torch.long, device=mask.device).bool(), mask], dim=1)  # <B, K+1>

        ### multi-label
        t2i_loss = -1 * F.log_softmax(t2i_logits, dim=1)                                    # <B, 1+K>
        t2i_loss = torch.masked_select(t2i_loss, mask).sum() / batch_size              # masked_select return 1-d tensor
        i2t_loss = -1 * F.log_softmax(i2t_logits, dim=1)
        i2t_loss = torch.masked_select(i2t_loss, mask).sum() / batch_size              # masked_select return 1-d tensor

        match_loss = t2i_loss + i2t_loss

        if self.mlm:
            bert_prediction = prediction["text_output_q"]["bert_prediction"]
            bert_prediction = bert_prediction.cpu()
            bert_label = prediction["text_output_q"]["encoded_label"]
            mlm_loss = F.nll_loss(bert_prediction.transpose(1, 2), bert_label, ignore_index=0)
        else:
            mlm_loss = match_loss

        return match_loss, mlm_loss
        ########################################################################################################################

        image_features = prediction["image_features"]
        text_features = prediction["text_features"]
        logit_scale = prediction["logit_scale"]
        bert_prediction = prediction["bert_prediction"]

        device = image_features.device
        bert_label = prediction["bert_label"]

        if self.world_size > 1:
            all_image_features, all_text_features = gather_features(
                image_features, text_features,
                self.local_loss, self.gather_with_grad, self.rank, self.world_size, self.use_horovod)

            if self.local_loss:
                logits_per_image = logit_scale * image_features @ all_text_features.T
                logits_per_text = logit_scale * text_features @ all_image_features.T
            else:
                logits_per_image = logit_scale * all_image_features @ all_text_features.T
                logits_per_text = logits_per_image.T
        else:
            logits_per_image = logit_scale * image_features @ text_features.T
            logits_per_text = logit_scale * text_features @ image_features.T

        # calculated ground-truth and cache if enabled
        num_logits = logits_per_image.shape[0]
        if self.prev_num_logits != num_logits or device not in self.labels:
            labels = torch.arange(num_logits, device=device, dtype=torch.long)
            if self.world_size > 1 and self.local_loss:
                labels = labels + num_logits * self.rank
            if self.cache_labels:
                self.labels[device] = labels
                self.prev_num_logits = num_logits
        else:
            labels = self.labels[device]

        # bert_prediction  # [128, 77, 49409]
        # bert_label  # [batch_size=128, n_ctx=77]
        # logging.debug(f"\033[42mbert_prediction\033[0m: {bert_prediction.shape}")  # [128, 49409, 77]
        # logging.info(f"\033[42mbert_prediction\033[0m: {bert_prediction.transpose(1, 2).shape}")  # [128, 49409, 77]

        bert_prediction = bert_prediction.cpu()
        logging.debug(f"\033[42mbert_prediction.device\033[0m: {bert_prediction.device}")  # 
        logging.debug(f"\033[42mbert_label.device\033[0m: {bert_label.device}")  # 

        mlm_loss = F.nll_loss(bert_prediction.transpose(1, 2), bert_label, ignore_index=0)
        match_loss = (
            F.cross_entropy(logits_per_image, labels) +
            F.cross_entropy(logits_per_text, labels)
            ) / 2
        return match_loss, mlm_loss
