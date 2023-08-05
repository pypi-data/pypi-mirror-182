import logging

import torch
import torch.nn as nn
from torch.nn import functional as F
import numpy as np

from .utils import gather_features

class MoCo_Img_Loss(nn.Module):

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
        # compute logits for image -> text
        # positive logits: Nx1
        logit_scale = prediction["logit_scale"]
        logit_scale_moco = prediction["logit_scale_moco"]

        image_features_q, image_features_k = prediction['image_features_q'], prediction['image_features_k']
        text_output_q = prediction['text_output_q']
        img_queue = prediction['img_queue']

        # NOTE img2img Loss
        i2i_l_pos = torch.einsum('nc,nc->n', [image_features_q, image_features_k]).unsqueeze(-1)
        # negative logits: NxK
        i2i_l_neg = torch.einsum('nc,ck->nk', [image_features_q, img_queue.clone().detach()])
        # logits: Nx(1+K)
        i2i_logits = torch.cat([i2i_l_pos, i2i_l_neg], dim=-1)
        i2i_logits *= logit_scale_moco
        moco_labels = torch.zeros(i2i_logits.shape[0], dtype=torch.long).cuda()
        moco_loss = F.cross_entropy(i2i_logits, moco_labels)
        '''
        ### multi-label
        batch_size = image_features_q.shape[0]
        mask = torch.zeros((batch_size, self.K)).bool().cuda()  # <B, K>
        mask = torch.cat([torch.ones((batch_size, 1), dtype=torch.long, device=mask.device).bool(), mask], dim=1)  # <B, K+1>
        ### multi-label
        moco_loss = -1 * F.log_softmax(i2i_logits, dim=1)
        moco_loss = torch.masked_select(moco_loss, mask).sum() / batch_size              # masked_select return 1-d tensor
        '''

        # NOTE (i2t + t2i) Loss
        logits_per_image = logit_scale * image_features_q @ text_output_q["text_features"].T
        logits_per_text = logit_scale * text_output_q["text_features"] @ image_features_q.T
        num_logits = logits_per_image.shape[0]
        device = image_features_q.device
        labels = torch.arange(num_logits, device=device, dtype=torch.long)
        match_loss = (
            F.cross_entropy(logits_per_image, labels) +
            F.cross_entropy(logits_per_text, labels)
        ) / 2

        if self.mlm:
            bert_prediction = prediction["text_output_q"]["bert_prediction"]
            bert_prediction = bert_prediction.cpu()
            bert_label = prediction["text_output_q"]["encoded_label"]
            mlm_loss = F.nll_loss(bert_prediction.transpose(1, 2), bert_label, ignore_index=0)

        # MoCo evaluate
        metrics = {}
        with torch.no_grad():
            ranking = torch.argsort(i2i_logits, descending=True)
            ground_truth = torch.zeros(ranking.shape[0]).view(-1, 1)
            # raise RuntimeError(ranking.shape, moco_labels.shape, ranking[0])

            preds = torch.where(ranking.cpu() == ground_truth)[1]  # 正确的 sample 当前的 rank
            preds = preds.detach().cpu().numpy()
            metrics[f"moco_mean_rank"] = preds.mean() + 1
            metrics[f"moco_median_rank"] = np.floor(np.median(preds)) + 1
            for k in [1, 5, 10]:
                metrics[f"moco_R@{k}"] = np.mean(preds < k)

        return match_loss, mlm_loss, moco_loss, metrics
