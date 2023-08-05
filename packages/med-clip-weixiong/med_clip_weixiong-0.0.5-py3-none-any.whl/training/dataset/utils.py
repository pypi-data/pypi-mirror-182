import logging
import random
import pandas as pd
import torch
import re


def get_word_to_frequency(input_filename):
    """
    Map word to frequency
    """
    wordfrequency_path = {
        '/remote-home/share/medical/public/ROCO/test/radiology/processed_test.csv': '/remote-home/weixionglin/vlp/Analysis/ROCO/Frequency/csv_cache/test_wordcount.csv',
        '/remote-home/share/medical/public/ROCO/valid/radiology/processed_valid.csv': '/remote-home/weixionglin/vlp/Analysis/ROCO/Frequency/csv_cache/valid_wordcount.csv',
        '/remote-home/share/medical/public/ROCO/train/radiology/processed_train.csv': '/remote-home/weixionglin/vlp/Analysis/ROCO/Frequency/train_wordcount.csv',
        "/remote-home/weixionglin/vlp/Analysis/ROCO/Frequency/csv_cache/train_disjoint.csv": '/remote-home/weixionglin/vlp/Analysis/ROCO/Frequency/csv_cache/train_wordcount.csv',
        "/remote-home/weixionglin/vlp/Analysis/ROCO/Frequency/csv_cache/valid_disjoint.csv": '/remote-home/weixionglin/vlp/Analysis/ROCO/Frequency/csv_cache/valid_wordcount.csv'
    }[input_filename]
    df_wordfrequency = pd.read_csv(wordfrequency_path, sep=self.args.csv_separator)
    word_frequency = dict(zip(df_wordfrequency['word'].tolist(), df_wordfrequency['norm_frequency'].tolist()))
    return word_frequency

def remove_low_frequency_words(caption: str, word_to_frequency: dict, filter_ratio: float):
    """
    过滤 low frequency word:
    - 根据 word frequency 决定 word 被 mask 的概率
    - 被 mask 概率 = filter_ratio * (1 - norm(frequency))
    """
    words = caption.split(' ')
    # words = [word for word in words if random.random() < self.word_frequency.get(word, 0.0) * self.filter_ratio]
    words = [word for word in words if random.random() < word_to_frequency.get(word, 1.0) * filter_ratio]
    return ' '.join(words)


def base_masker(caption, vocab, mask_token='<MASK>', pad_token='<PAD>', ratio=0.15, *rest):
    """
    NOTE 参考
    Masker for base strategy

    Args:
        caption: str
        ratio: probability of token been masked out
        rest: 多的参数, 为了配合 umls_masker
    output_label: 85% 的概率为 0 表示无操作; 其它情况为 1 表示 token 被替换为了其他值
    """
    tokenizer, nlp = rest  # nlp is for umls, but not here

    def measure_word_len(word):
        token_ids = tokenizer.encode(word)
        # tokens = [tokenizer.decode(x) for x in token_ids]
        return len(token_ids) - 2

    tokens = caption.split()
    bert_input_tokens = []
    output_mask = []
    bert_label_tokens = []  # 被 mask 的保留原词, 否则用 [PAD] 代替
    for i, token in enumerate(tokens):
        prob = random.random()
        if prob < ratio:
            prob /= ratio
            # 80% randomly change token to mask token
            if prob < 0.8:
                word_len = measure_word_len(token)
                bert_input_tokens += [mask_token] * word_len
            # 10% randomly change token to random token
            elif prob < 0.9:
                rand_token = random.choice(vocab).replace('</w>', '')
                word_len = measure_word_len(rand_token)
                # tokens[i] = random.randrange(self.tokenizer.vocab_size)
                bert_input_tokens += [rand_token]
            # 10% randomly change token to current token
            else:
                bert_input_tokens += [token]
                word_len = measure_word_len(token)
            output_mask += [1] * word_len
            bert_label_tokens += [token]
        else:
            word_len = measure_word_len(token)
            bert_input_tokens += [token]
            output_mask += [0] * word_len
            bert_label_tokens += [pad_token] * word_len
    # raise RuntimeError(prob, tokens, caption, bert_label_tokens)
    # logging.info(f"\033[42mprob:\033[0m {prob}")
    # logging.info(f"\033[42mtokens:\033[0m {tokens}")
    # logging.info(f"\033[42mcaption:\033[0m {caption}")
    # logging.info(f"\033[42mbert_label_tokens:\033[0m {bert_label_tokens}")
    logging.debug(f"\033[42moutput_mask:\033[0m {output_mask}")

    token_result = dict.fromkeys(["bert_input_tokens", "output_mask", "bert_label_tokens"], None)
    for key in token_result:
        token_result[key] = eval(key)  # HACK dark magic, could be dangerous
    return token_result


def umls_split(caption, nlp):
    '''split caption into tokens according to UMLS
    - 提取 caption 中的 entities, 根据 entity 包含 token 的数量从大到小排序
    - 用每个 entity 将 caption 切分开, umls 对应的位置为 1, 否则为 0
    - 此时只有 entity 和非 entity 的短语; 将非 entity 短语 split 到 token 级别
    - 在 mask 的时候如果选中 entity 稍做处理即可
    '''
    # import spacy
    # nlp = spacy.load("en_core_sci_lg")
    # 将 entity 排序
    # caption = 'Bullet localization intraoperatively by portable imaging system (C-arm)'
    ents = [str(x) for x in nlp(caption).ents]
    ents = sorted(ents, key=lambda x: len(x.split()), reverse=True)
    # print(f"ents: {ents}")
    tokens = []

    # 用 entity 切分 caption
    def _umls_split(caption):
        if len(caption) == 0:
            return
        flag = False
        for ent in ents:
            res = re.search(re.escape(ent), caption)
            if res is not None:
                flag = True
                start, end = res.span()
                _umls_split(caption[:start])
                tokens.append(caption[start: end])
                _umls_split(caption[end:])
                break
        if flag == False:  # no entity
            tokens.append(caption)
    _umls_split(caption)
    return tokens, ents


def umls_masker(caption, vocab, mask_token='<MASK>', pad_token='<PAD>', ratio=0.15, *rest):
    """
    Masker for umls strategy
    """
    tokenizer, nlp = rest

    def measure_word_len(word):
        token_ids = tokenizer.encode(word)
        # tokens = [tokenizer.decode(x) for x in token_ids]
        return len(token_ids) - 2

    tokens, ents = umls_split(caption, nlp=nlp)
    # tokens = caption.split()
    bert_input_tokens = []
    output_mask = []
    bert_label_tokens = []  # 被 mask 的保留原词, 否则用 [PAD] 代替
    for i, token in enumerate(tokens):
        # logging.info(f"\033[42mumls_token:\033[0m {token}")
        prob = random.random()
        if prob < ratio and token in ents:
            prob /= ratio
            # 80% randomly change token to mask token
            if prob < 0.8:
                word_len = measure_word_len(token)
                bert_input_tokens += [mask_token] * word_len
            # 10% randomly change token to random token
            elif prob < 0.9:
                rand_token = random.choice(vocab).replace('</w>', '')
                word_len = measure_word_len(rand_token)
                # tokens[i] = random.randrange(self.tokenizer.vocab_size)
                bert_input_tokens += [rand_token]
            # 10% randomly change token to current token
            else:
                bert_input_tokens += [token]
                word_len = measure_word_len(token)
            output_mask += [1] * word_len
            bert_label_tokens += [token]
        else:
            word_len = measure_word_len(token)
            bert_input_tokens += [token]
            output_mask += [0] * word_len
            bert_label_tokens += [pad_token] * word_len
    # logging.info(f"\033[42mprob:\033[0m {prob}")
    # logging.info(f"\033[42mtokens:\033[0m {tokens}")
    # logging.info(f"\033[42mcaption:\033[0m {caption}")
    # logging.info(f"\033[42mbert_label_tokens:\033[0m {bert_label_tokens}")
    logging.debug(f"\033[42moutput_mask:\033[0m {output_mask}")

    token_result = dict.fromkeys(["bert_input_tokens", "output_mask", "bert_label_tokens"], None)
    for key in token_result:
        token_result[key] = eval(key)  # HACK dark magic, could be dangerous
    return token_result


def encode_mlm(caption, vocab, mask_token: str, pad_token: str, ratio: float, nlp, tokenizer, args):
    """
    生成 MLM 需要的 bert_input, bert_label

    参考代码:
    - [BERT-pytorch]
    - [DataCollatorForWholeWordMask](https://github.com/huggingface/transformers/blob/main/src/transformers/data/data_collator.py#L1072)
    """
    context_length = args.context_length
    masking_strategy = args.mlm_strategy
    masker = {
        'base': base_masker,
        'umls': umls_masker,
    }[masking_strategy]

    token_result = masker(
        caption,
        vocab,
        mask_token,
        pad_token,
        ratio,
        tokenizer,
        nlp,
    )  # Remove words for MLM task

    output_mask = token_result["output_mask"]
    output_mask += [0] * (context_length - len(output_mask))
    output_mask = torch.tensor(output_mask[:context_length])
    logging.debug(len(output_mask), output_mask)

    bert_input_tokens = token_result["bert_input_tokens"]
    bert_input = ' '.join(bert_input_tokens)
    bert_label_tokens = token_result["bert_label_tokens"]
    bert_label = ' '.join(bert_label_tokens)

    # logging.info(f"bert_input: {text_input}")
    # logging.info(f"bert_label: {caption}")
    # logging.info(f"output_mask: {output_mask}")

    # bert_input = bert_label * output_mask
    # raise RuntimeError('stop in encode_mlm')

    return bert_input, bert_label
