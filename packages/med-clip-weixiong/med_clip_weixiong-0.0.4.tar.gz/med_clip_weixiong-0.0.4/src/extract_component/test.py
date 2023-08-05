import torch

# ImageEncoder
model = torch.load("/remote-home/share/weixionglin/medclip/vlp/open_clip/src/extract_component/extracted/2022_12_20-04_56_27-model_RN50_MoCo_Img_256-p_amp/ImageEncoder.bin")
# TextEncoder
# model = torch.load('/remote-home/share/weixionglin/medclip/vlp/open_clip/src/extract_component/extracted/2022_12_20-04_52_58-model_RN50_MoCo_Img_256-p_amp/TextEncoder.bin')

print(model)
