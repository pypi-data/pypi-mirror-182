from torch.utils.data import Dataset, DataLoader
import pandas as pd
from PIL import Image


def csv_loader(input_filename, img_key, caption_key, sep):
    # Load images, captions from Csv data
    df = pd.read_csv(input_filename, sep=sep)
    images, captions = df[img_key].tolist(), df[caption_key].tolist()
    return images, captions


class CsvDataset(Dataset):
    def __init__(self, input_filename, transforms, img_key='image', caption_key='caption'):

        loader = csv_loader
        self.images, self.captions = loader(
            input_filename=input_filename,
            img_key=img_key,
            caption_key=caption_key,
            sep=','
        )
        self.transforms = transforms

    def __len__(self):
        return len(self.captions)

    def __getitem__(self, idx):
        output = dict.fromkeys(["images", "bert_input"], None)
        images = self.transforms(Image.open(str(self.images[idx])))
        caption = str(self.captions[idx])

        output.update({
            "images": images,
            "bert_input": caption,
        })
        return output


def get_csv_dataset(input_filename, batch_size, preprocess_func):
    dataset_cls = CsvDataset
    dataset = dataset_cls(
        input_filename,
        preprocess_func
    )

    num_samples = len(dataset)

    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        num_workers=8,
        pin_memory=True,
    )
    dataloader.num_samples = num_samples
    dataloader.num_batches = len(dataloader)

    return dataloader


