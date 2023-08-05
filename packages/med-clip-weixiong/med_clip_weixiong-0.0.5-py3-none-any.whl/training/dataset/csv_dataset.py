import logging
import random
import pandas as pd
import jsonlines
from PIL import Image

import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer
# from open_clip import tokenize, simple_tokenizer, mlm_tokenizer

from .utils import get_word_to_frequency, remove_low_frequency_words, encode_mlm

import spacy


def csv_loader(input_filename, img_key, caption_key, sep):
    """
    Load images, captions from Csv data
    """
    df = pd.read_csv(input_filename, sep=sep)
    images, captions = df[img_key].tolist(), df[caption_key].tolist()
    return images, captions

def jsonl_loader(input_filename, img_key, caption_key, sep):
    images, captions = [], []
    with jsonlines.open(input_filename) as reader:
        for obj in reader:
            images.append(obj[img_key])
            captions.append(obj[caption_key])
    return images, captions

class CsvDataset(Dataset):
    def __init__(self, args, input_filename, transforms, is_train):
        logging.debug(f'Loading csv data from {input_filename}.')

        self.args = args
        suffix = input_filename.split('.')[-1]
        loader = {
            'csv': csv_loader,
            'jsonl': jsonl_loader,
        }[suffix]
        self.images, self.captions = loader(
            input_filename=input_filename,
            img_key=args.csv_img_key,
            caption_key=args.csv_caption_key,
            sep=args.csv_separator
        )
        self.transforms = transforms
        self.nlp = spacy.load("en_core_sci_lg")

        if args.mlm:
            if (args.hugging_face and args.model in ['RN50_ClinicalBERT', 'RN50_PubmedBERT', 'RN50_UMLSBERT', 'RN50_MoCo_Text']) or\
                (args.model in [
                    'RN50_MemBank_256',
                    'RN50_MemBank_256_09',
                    'RN50_MemBank_256_99',
                    'RN50_MemBank_512',
                    'RN50_MemBank_512_99',
                    'RN50_MemBank_128_00',
                    'RN50_MemBank_1024_99',
                    'RN50_MemBank_4096_99',
                    'RN50_MemBank_8192_99',
                    'RN50_MoCo_Img',
                    'RN50_MoCo_Img_32_99',
                    'RN50_MoCo_Img_256',
                    'RN50_MoCo_Img_256_99',
                    'RN50_MoCo_Img_512',
                    'RN50_MoCo_Img_512_99',
                    'RN50_MoCo_Img_2048_99',
                    'RN50_MoCo_Img_8192_99',
                    'RN50_MoCo_Img_32768_99',
                    # MLM Image
                    'RN50_PubmedBERT_MLMG',
                ]):
                self.tokenizer = AutoTokenizer.from_pretrained(args.bert_model_name)
                self.mask_token, self.pad_token = '[MASK]', '[PAD]'
                vocab = list(self.tokenizer.get_vocab().keys())  # get_vocab: {'token': token_id}
                # NOTE vocab 里面去掉 special token, 否则会对之后预测有干扰
                self.vocab_with_no_special_token = [vocab_token for vocab_token in vocab if vocab_token not in self.tokenizer.all_special_tokens]

            else:
                raise RuntimeError('please check the special token of your tokenizer')
            # self.mlm_tokenizer = mlm_tokenizer
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
        
        if self.args.umls_filter:
            raise NotImplementedError('This feature is replaced with args.mlm_strategy')
            entities = self.nlp(caption).ents
            umls_tokens = [str(x) for x in entities]
            caption = ' '.join(umls_tokens)

        if self.args.mlm:  # MLM task
            bert_input, bert_label = encode_mlm(
                caption=caption,
                vocab=self.vocab_with_no_special_token,
                mask_token=self.mask_token,
                pad_token=self.pad_token,
                ratio=self.ratio,
                nlp=self.nlp,
                tokenizer=self.tokenizer,
                args=self.args,
            )
        else:
            bert_input = caption
            bert_label = caption  # pytorch 不允许 batch 中有 None

        output.update({
            "images": images,
            "bert_input": bert_input,
            "bert_label": bert_label
        })
        return output


if __name__ == '__main__':
    print('\033[42mUnit Test\033[0m')
    csv_dataset = CsvDataset(
        input_filename='/remote-home/share/medical/public/ROCO/test/radiology/processed_test.csv',
        transforms=lambda x:x,
        img_key='image',
        caption_key='caption',
        sep=','
    )
