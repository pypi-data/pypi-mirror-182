'''
其实 JsonlDataset 和 CsvDataset 的差别很小, 但是考虑到之后 medicat 的扩展性, 写成两个文件比较合适
'''
import logging
import random
import pandas as pd
from PIL import Image
from pathlib import Path
from dataclasses import dataclass
import jsonlines

import torch
from torch.utils.data import Dataset
from open_clip import tokenize, SimpleTokenizer


def read_jsonl(file_path):
    data_list = []
    with jsonlines.open(file_path) as reader:
        for obj in reader:
            data_list.append(obj)
    return data_list


def load_from_jsonl(input_filename):
    data_list = read_jsonl(input_filename)
    images, captions = [], []
    root_dir = Path('/remote-home/share/medical/public/MedICaT')

    for obj in data_list:
        img_path = root_dir / "release/figures/" / f"{obj['pdf_hash']}_{obj['fig_uri']}"
        images.append(img_path)
        captions.append(obj['s2_caption'])
    return images, captions


class JsonlDataset(Dataset):
    def __init__(self, args, input_filename, transforms, is_train):
        logging.debug(f'Loading jsonl data from {input_filename}.')

        self.args = args
        self.images, self.captions = load_from_jsonl(input_filename=input_filename)

        self.transforms = transforms
        self.simple_tokenizer = SimpleTokenizer()

        if args.mlm:
            self.mask_token = '<mask>'
            self.mlm_tokenizer = SimpleTokenizer(special_tokens=[self.mask_token])
            self.ratio = args.mask_ratio if is_train else 0.0

        if self.args.filter:  # 需要过滤 low frequency words
            self.word_to_frequency = get_word_to_frequency(input_filename)
        logging.debug('Done loading data.')

    def __len__(self):
        return len(self.captions)

    def __getitem__(self, idx):
        output = dict.fromkeys(["images", "bert_input", "bert_label"], None)
        images = self.transforms(Image.open(str(self.images[idx])))
        caption = str(self.captions[idx])

        if self.args.filter:  # Filter out low frequency words
            caption = remove_low_frequency_words(
                caption=caption,
                word_to_frequency=self.word_to_frequency,
                filter_ratio=self.args.filter_ratio
            )

        if self.args.mlm:
            bert_input, bert_label = encode_mlm(
                caption=caption,
                tokenizer=self.mlm_tokenizer,
                mask_token=self.mask_token,
                ratio=self.ratio,
                context_length=self.args.context_length
            )
        else:
            bert_input = 0  # pytorch 不允许 batch 中有 None
            bert_label = tokenize(_tokenizer=self.simple_tokenizer, texts=[caption])[0]

        # texts = tokenize([str(self.captions[idx])])[0]
        # image, text = batch["images"], batch["bert_input"]
        output.update({
            "images": images,
            "bert_input": bert_input,
            "bert_label": bert_label
        })
        return output


if __name__ == '__main__':
    print('\033[42mUnit Test\033[0m')
    class Args(object):
        batch_size = 128
        csv_img_key = "image"
        csv_caption_key = "caption"
        csv_separator = ","
        dataset_type = "auto"
        device = "cuda:0"
        distributed = False
        epochs = 32
        force_quick_gelu = False
        imagenet_val = None
        imagenet_v2 = None
        model = "RN50"
        pretrained = ''
        pretrained_image = False
        precision = "amp"
        rank = 0
        resume = "/remote-home/weixionglin/vlp/open_clip/src/logs/2022_07_26-13_30_03-model_RN50-lr_0.001-b_128-j_8-p_amp/checkpoints/epoch_30.pt"
        save_logs = False
        torchscript = False
        train_data = None
        val_data = "/remote-home/share/medical/public/ROCO/test/radiology/processed_test.csv"
        val_frequency = 1
        wandb = False
        workers = 8
        mlm = False
        context_length = 77
        filter = False
    args = Args()

    jsonl_dataset = JsonlDataset(
        args=args,
        input_filename='/remote-home/weixionglin/vlp/Analysis/medicat/test.jsonl',
        transforms=lambda x:x,
        is_train=True
    )
    print(jsonl_dataset[0])
