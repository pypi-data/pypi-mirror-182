'''
Extract Text Encoder of CLIP

python -m extract_component.main  --extract TextEncoder \
    --model RN50_MoCo_Img_256 --hugging-face \
    --resume /remote-home/share/weixionglin/medclip/vlp/open_clip/src/logs/2022_11_14-02_09_39-model_RN50_MoCo_Img_256-lr_0.0001-b_128-j_8-p_amp/checkpoints/epoch_100.pt \
    --device cuda:0 --logs ./extract_component/extracted

python -m extract_component.main  --extract ImageEncoder \
    --model RN50_MoCo_Img_256 --hugging-face \
    --resume /remote-home/share/weixionglin/medclip/vlp/open_clip/src/logs/2022_11_14-02_09_39-model_RN50_MoCo_Img_256-lr_0.0001-b_128-j_8-p_amp/checkpoints/epoch_100.pt \
    --device cuda:0 --logs ./extract_component/extracted
'''
import logging
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # 否则 tokenizer 会给出 warning: https://github.com/huggingface/transformers/issues/5486
# os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,3,4"

import random
from datetime import datetime

import numpy as np
import torch
from torch import optim
from torch.cuda.amp import GradScaler

try:
    import torch.utils.tensorboard as tensorboard
except ImportError:
    tensorboard = None

from open_clip import create_model_and_transforms, trace_model
# from training.data import get_data
from training.distributed import is_master, init_distributed_device, world_info_from_env
from training.logger import setup_logging
from .utils import parse_args
# from training.train import train_one_epoch, train_one_epoch_mlm, evaluate, evaluate_wenlan

# decorator to report error message in torch distributed mode
if torch.__version__ >= '1.10':
    from torch.distributed.elastic.multiprocessing.errors import record
else:
    def record(func):
        def foo():
            func()
        return foo

def random_seed(seed=42, rank=0):
    torch.manual_seed(seed + rank)
    np.random.seed(seed + rank)
    random.seed(seed + rank)


def extract_TextEncoder(model, checkpoint, args, device, log_base_path):
    text_encoder = model.textual
    logging.info(text_encoder)

    # logging.info(checkpoint['state_dict'].keys())
    clip_model = checkpoint['state_dict']

    clip_model_keys = [k for k, v in clip_model.items()]
    # logging.info(clip_model_keys)
    # logging.info(text_encoder.state_dict().keys())
    # raise RuntimeError(1)

    pretrained_text_encoder = {k[8:]: v for k, v in clip_model.items() if k[8:] in text_encoder.state_dict()}  # k[13:] 去掉开头的 'textual.text_encoder.'

    text_encoder.load_state_dict(pretrained_text_encoder)
    torch.save(text_encoder, log_base_path + '/TextEncoder.bin')

    # save text encoder
    # text_encoder.save_pretrained(
    #     save_directory=log_base_path
    # )


def extract_ImageEncoder(model, checkpoint, args, device, log_base_path):
    image_encoder = model.visual
    logging.info(image_encoder)

    # logging.info(checkpoint['state_dict'].keys())
    clip_model = checkpoint['state_dict']
    logging.info(clip_model.keys())
    # pretrained_image_encoder = {k: v for k, v in clip_model.items() if k in image_encoder.state_dict()}
    pretrained_image_encoder = {k[7:]: v for k, v in clip_model.items() if k[7:] in image_encoder.state_dict()}
    # pretrained_image_encoder = {k[13:]: v for k, v in clip_model.items() if k[13:] in image_encoder.state_dict()}

    image_encoder.load_state_dict(pretrained_image_encoder)
    torch.save(image_encoder, log_base_path + '/ImageEncoder.bin')

    # save image encoder
    # image_encoder.save_pretrained(
    #     save_directory=log_base_path
    # )


@record
def main():
    args = parse_args()

    # sanitize model name for filesystem / uri use, easier if we don't use / in name as a rule?
    args.model = args.model.replace('/', '-')

    # get the name of the experiments
    if args.name is None:
        args.name = '-'.join([
            datetime.now().strftime("%Y_%m_%d-%H_%M_%S"),
            f"model_{args.model}",
            f"p_{args.precision}",
        ])

    # discover initial world args early so we can log properly
    args.distributed = False
    args.local_rank, args.rank, args.world_size = world_info_from_env()

    args.log_path = None
    if is_master(args, local=args.log_local):
        log_base_path = os.path.join(args.logs, args.name)
        os.makedirs(log_base_path, exist_ok=True)
        log_filename = f'out-{args.rank}' if args.log_local else 'out.log'
        args.log_path = os.path.join(log_base_path, log_filename)
        if os.path.exists(args.log_path):
            print(
                "Error. Experiment already exists. Use --name {} to specify a new experiment."
            )
            return -1

    # Set logger
    args.log_level = logging.DEBUG if args.debug else logging.INFO
    setup_logging(args.log_path, args.log_level)
    logging.info(f"Extracted Model: {args.resume}")

    # fully initialize distributed device environment
    torch.backends.cudnn.benchmark = True
    torch.backends.cudnn.deterministic = False
    # 在 init_distributed_device 给定 args.device 之前确保用户的意图是清晰的
    device = init_distributed_device(args)

    if is_master(args):
        args.checkpoint_path = os.path.join(args.logs, args.name, "checkpoints")


    assert args.precision in ['amp', 'fp16', 'fp32']
    if args.precision == 'fp16':
        logging.warning(
            'It is recommended to use AMP mixed-precision instead of FP16. '
            'FP16 support needs further verification and tuning, especially for train.')

    if args.horovod:
        logging.info(
            f'Running in horovod mode with multiple processes / nodes. Device: {args.device}.'
            f'Process (global: {args.rank}, local {args.local_rank}), total {args.world_size}.')
    elif args.distributed:
        logging.info(
            f'Running in distributed mode with multiple processes. Device: {args.device}.'
            f'Process (global: {args.rank}, local {args.local_rank}), total {args.world_size}.')
    else:
        logging.info(f'Running with a single process. Device {args.device}.')

    random_seed(args.seed, 0)
    model, preprocess_train, preprocess_val = create_model_and_transforms(
        args=args,
        precision=args.precision,
        device=device,
        jit=args.torchscript,
        force_quick_gelu=args.force_quick_gelu,
        pretrained_image=args.pretrained_image,
    )
    checkpoint = torch.load(args.resume, map_location=device)

    extract_component = {
        'TextEncoder': extract_TextEncoder,
        'ImageEncoder': extract_ImageEncoder
    }[args.extract]

    extract_component(model, checkpoint, args, device, log_base_path)

if __name__ == "__main__":
    main()
