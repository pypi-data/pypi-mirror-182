import torch
from torch.utils.data import Dataset

from PIL import Image
import pandas as pd
import random
import logging

from open_clip import tokenize, SimpleTokenizer


class MlmDataset(Dataset):
    def __init__(self, args, input_filename, transforms, is_train):
        logging.debug(f'Loading csv data from {input_filename}.')

        self.mlm = args.mlm  # whether to use mlm loss
        img_key = args.csv_img_key
        caption_key = args.csv_caption_key
        sep = args.csv_separator
        df = pd.read_csv(input_filename, sep=sep)

        self.images = df[img_key].tolist()
        self.captions = df[caption_key].tolist()
        self.transforms = transforms
        self.mask_token = '<mask>'
        self.tokenizer = SimpleTokenizer(special_tokens=[self.mask_token])
        self.context_length = args.context_length
        self.ratio = args.mask_ratio if is_train else 0.0
        logging.debug('Done loading data.')

    def __len__(self):
        return len(self.captions)

    def __getitem__(self, idx):
        output = dict.fromkeys(["images", "bert_input", "bert_label"], None)
        images = self.transforms(Image.open(str(self.images[idx])))
        caption = str(self.captions[idx])

        # Remove words for MLM task
        text_input, output_mask = self.remove_mlm_words(sentence=caption, ratio=self.ratio)
        output_mask += [0] * (self.context_length - len(output_mask))
        output_mask = torch.tensor(output_mask[:self.context_length])
        logging.debug(len(output_mask), output_mask)
        text_input = ' '.join(text_input)
        bert_label = tokenize(_tokenizer=self.tokenizer, texts=[text_input])[0]
        # bert_input: [49406, 46550, 24773, 49408,  1093, ...]
        # output_mask: [0, 0, 1, 0, 1, ...]
        bert_input = bert_label * output_mask
        # print(f"new_bert_label: {bert_label}\n")

        output.update({
            "images": images,
            "bert_input": bert_input,
            "bert_label": bert_label
        })
        return output

    def remove_mlm_words(self, sentence, ratio=0.15):
        """
        Remove mlm words

        Args:
            sentence: str
            ratio: probability of token been masked out
        output_label: 85% 的概率为 0 表示无操作; 其它情况为 1 表示 token 被替换为了其他值
        """
        tokens = sentence.split()
        output_mask = []
        for i, token in enumerate(tokens):
            prob = random.random()
            if prob < ratio:
                prob /= ratio
                # 80% randomly change token to mask token
                if prob < 0.8:
                    tokens[i] = self.mask_token
                # 10% randomly change token to random token
                elif prob < 0.9:
                    # tokens[i] = random.randrange(self.tokenizer.vocab_size)
                    tokens[i] = random.choice(self.tokenizer.vocab).replace('</w>', '')
                # 10% randomly change token to current token
                else:
                    tokens[i] = token
                output_mask.append(1)
            else:
                tokens[i] = token
                output_mask.append(0)
        logging.debug(f"\033[42mtokens:\033[0m {tokens}")
        logging.debug(f"\033[42moutput_mask:\033[0m {output_mask}")
        return tokens, output_mask


if __name__ == '__main__':
    print('Dataset Unit Test')
    class Args(object):
        def __init__(self):
            self.batch_size = 128
            self.csv_img_key = "image"
            self.csv_caption_key = "caption"
            self.csv_separator = ","
            self.dataset_type = "auto"
            self.device = "cuda:0"
            self.distributed = False
            self.epochs = 32
            self.force_quick_gelu = False
            self.imagenet_val = None
            self.imagenet_v2 = None
            self.model = "RN50"
            self.pretrained = ''
            self.pretrained_image = False
            self.precision = "amp"
            self.rank = 0
            # self.resume = "/remote-home/weixionglin/vlp/open_clip/src/logs/2022_07_26-13_30_03-model_RN50-lr_0.001-b_128-j_8-p_amp/checkpoints/epoch_30.pt"
            self.save_logs = False
            self.torchscript = False
            self.train_data = None
            self.val_data = "/remote-home/share/medical/public/ROCO/test/radiology/processed_test.csv"
            self.val_frequency = 1
            self.wandb = False
            self.workers = 8
            self.mlm = True
            self.mask_ratio = 0.15
            self.context_length = 77
    args = Args()
    preprocess_fn = lambda x:x
    dataset = MlmDataset(
        args,
        input_filename='/remote-home/share/medical/public/ROCO/test/radiology/processed_test.csv',
        transforms=preprocess_fn,
        is_train=True
    )
    output0 = dataset[0]
    print(output0.keys())

    raise RuntimeError('stop here')
    for i in range(len(dataset)):
        output = dataset[i]
        label_len = len(output['bert_label'])
        if label_len != 77:
            print(f"idx: {i}; label_len: {label_len}")
    print(f"\033[42moutput:\033[0m {len(output['bert_label'])}")
