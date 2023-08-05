import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--horovod",
        default=False,
        action="store_true",
        help="Use horovod for distributed training."
    )
    parser.add_argument(
        "--force-quick-gelu",
        default=False,
        action='store_true',
        help="Force use of QuickGELU activation for non-OpenAI transformer models.",
    )
    parser.add_argument(
        "--pretrained-image",
        default=False,
        action='store_true',
        help="Load imagenet pretrained weights for image tower backbone if available.",
    )
    parser.add_argument(
        "--logs",
        type=str,
        default="./logs/",
        help="Where to store tensorboard logs. Use None to avoid storing logs.",
    )
    parser.add_argument(
        "--log-local",
        action="store_true",
        default=False,
        help="log files on local master, otherwise global master only.",
    )
    parser.add_argument(
        "--name",
        type=str,
        default=None,
        help="Optional identifier for the experiment when storing logs. Otherwise use current time.",
    )
    parser.add_argument(
        "--resume",
        default=None,
        type=str,
        help="path to latest checkpoint (default: none)",
    )
    parser.add_argument(
        "--precision",
        choices=["amp", "fp16", "fp32"],
        default="amp",
        help="Floating point precision."
    )
    parser.add_argument(
        "--model",
        type=str,
        default="RN50",
        help="Name of the vision backbone to use.",
    )
    parser.add_argument(
        "--pretrained",
        default='',
        type=str,
        help="Use a pretrained CLIP model weights with the specified tag or file path.",
    )
    parser.add_argument(
        "--torchscript",
        default=False,
        action='store_true',
        help="torch.jit.script the model, also uses jit version of OpenAI models if pretrained=='openai'",
    )
    parser.add_argument(
        "--trace",
        default=False,
        action='store_true',
        help="torch.jit.trace the model for inference / eval only",
    )
    # arguments for distributed training
    parser.add_argument(
        "--dist-url",
        default="env://",
        type=str,
        help="url used to set up distributed training",
    )
    parser.add_argument(
        "--dist-backend", default="nccl", type=str, help="distributed backend"
    )
    parser.add_argument(
        "--report-to",
        default='',
        type=str,
        help="Options are ['wandb', 'tensorboard', 'wandb,tensorboard']"
    )
    parser.add_argument(
        "--debug",
        default=False,
        action="store_true",
        help="If true, more information is logged."
    )
    parser.add_argument(
        "--no-set-device-rank",
        default=False,
        action="store_true",
        help="Don't set device index from local rank (when CUDA_VISIBLE_DEVICES restricted to one per proc)."
    )
    parser.add_argument(
        "--seed", type=int, default=0, help="Default random seed."
    )

    parser.add_argument(
        "--device",
        default=None,
        type=str,
        help="Manually decide device to use, train on a single gpu"
    )

    parser.add_argument(
        "--filter", default=False, action="store_true", help="Whether to mask out low frequency words"
    )
    parser.add_argument(
        "--filter-ratio", type=float, default=None, help="Ratio of masking low frequency words"
    )

    parser.add_argument(
        "--crop-scale", type=float, default=0.9, help="RandomCrop scale (crop_scale, 1.o)"
    )

    parser.add_argument(
        "--mlm",
        default=False,
        action="store_true",
        help="Whether to use MLM Loss"
    )
    parser.add_argument("--mask-ratio", type=float, default=0.15, help="Probability to replace token to <mask>")

    parser.add_argument(
        "--hugging-face",
        default=False,
        action="store_true",
        help="Load tokenizer & text encoder from HuggingFace"
    )

    parser.add_argument(
        "--moco-aug",
        default=False,
        action="store_true",
        help="Use augmentations of MoCo or just those in OpenClip"
    )
    parser.add_argument(
        "--freeze-bert",
        type=str,
        default=None,
        help="Freeze ALL params in BERT",
    )
    parser.add_argument(
        "--umls-filter",
        default=False,
        action="store_true",
        help="Use spacy to filter non-umls words in captions",
    )
    parser.add_argument(
        "--loss-weight",
        type=str,
        default="0",
        help="Different loss weight",
    )

    ######################################################################################
    # NOTE 不要在命令行里面用这些, 只是用来传参数
    parser.add_argument(
        "--clip-model",
        type=str,
        default=None,
        help="CLIP Model",
    )
    parser.add_argument(
        "--queue-size",
        type=int,
        default=None,
        help="int",
    )
    ######################################################################################
    # NOTE 指明需要 extract ImageEncoder 还是 TextEncoder
    parser.add_argument(
        "--extract",
        type=str,
        default=None,
        help="ImageEncoder ? TextEncoder",
    )

    args = parser.parse_args()

    return args
