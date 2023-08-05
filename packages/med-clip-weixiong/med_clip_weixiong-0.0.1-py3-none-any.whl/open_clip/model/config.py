from typing import Tuple, Union, Callable, Optional

from dataclasses import dataclass

@dataclass
class CLIPVisionCfg:
    layers: Union[Tuple[int, int, int, int], int] = 12
    width: int = 768
    head_width: int = 64
    mlp_ratio: float = 4.0
    patch_size: int = 16
    image_size: Union[Tuple[int, int], int] = 224
    timm_model_name: str = None  # a valid model name overrides layers, width, patch_size
    timm_model_pretrained: bool = False  # use (imagenet) pretrained weights for named model
    timm_pool: str = 'avg'  # feature pooling for timm model ('abs_attn', 'rot_attn', 'avg', '')
    timm_proj: str = 'linear'  # linear projection for timm model output ('linear', 'mlp', '')


@dataclass
class CLIPTextCfg:
    bert_model_name: str = 'base'
    context_length: int = 77
    vocab_size: int = 49408
    width: int = 512
    heads: int = 8
    layers: int = 12
    fusion_layers: int = 1  # layers of fusion_module
    # 参数取自 WenLan(https://github.com/BAAI-WuDao/BriVL/blob/main/BriVL-code-inference/cfg/test_xyb.yml)
    QUEUE_SIZE: int = 8192
    MOMENTUM: float = 0.5
    # MOMENTUM: float = 0.99
