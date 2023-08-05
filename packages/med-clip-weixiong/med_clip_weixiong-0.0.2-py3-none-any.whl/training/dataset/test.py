# %%
import jsonlines

# %%
def jsonl_loader(input_filename, img_key, caption_key, sep):
    images, captions = [], []
    with jsonlines.open(input_filename) as reader:
        for obj in reader:
            images.append(obj[img_key])
            captions.append(obj[caption_key])
    return images, captions

# %%
images, captions = jsonl_loader(
    '/remote-home/share/medical/public/PMC_OA/pairs.jsonl',
    img_key='image',
    caption_key='caption',
    sep=','
)

# %%
print(images[0])
print(captions[0])

# %%
print(len(images))
print(len(captions))
