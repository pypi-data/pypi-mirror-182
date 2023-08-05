# coding=UTF-8
# %%
# 用 pretrain 的 Image/Text Encoder 提取特征
import torch
from transformers import AutoTokenizer

# %%
# Load Pretrained Model
image_encoder = torch.load("/remote-home/share/weixionglin/medclip/vlp/open_clip/src/extract_component/extracted/2022_12_20-04_56_27-model_RN50_MoCo_Img_256-p_amp/ImageEncoder.bin")
image_encoder.eval()
tokenizer = AutoTokenizer.from_pretrained('microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext')
text_encoder = torch.load('/remote-home/share/weixionglin/medclip/vlp/open_clip/src/extract_component/extracted/2022_12_20-04_52_58-model_RN50_MoCo_Img_256-p_amp/TextEncoder.bin')
text_encoder.eval()

# %%
# 超参
batch_size = 128
dataset_path = '/remote-home/share/medical/public/ROCO/test/radiology/processed_test.csv'
image_size = 224
device = 'cuda:1'

# %%
# Prepare Data
from data import get_csv_dataset

from transform import image_transform
preprocess_train = image_transform(
    image_size,
    is_train=True,
)
preprocess_val = image_transform(
    image_size,
    is_train=False,
)

dataloader = get_csv_dataset(dataset_path, batch_size, preprocess_train)

# %%
# Extract Image feature
batch_data = iter(dataloader).next()
images = batch_data['images'].to(device)
image_encoder.to(device)
image_feature = image_encoder(images)
print(f'image size: {images.shape}; feature size: {image_feature.shape}')

# %%
text_feature = text_encoder(batch_data)['text_features'].to(device)
print(text_feature.shape)
