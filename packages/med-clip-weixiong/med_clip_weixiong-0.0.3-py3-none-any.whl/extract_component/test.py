import torch

model = torch.load('/remote-home/share/weixionglin/medclip/vlp/open_clip/src/extract_component/extracted/2022_11_12-17_40_03-model_RN50_PubmedBERT-lr_0.0005-b_128-j_8-p_amp/ImageEncoder.bin')

print(model)
