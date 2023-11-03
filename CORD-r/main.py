import os
import json
import tqdm

from datasets import load_dataset 

target_dir = 'images'

dataset_all = load_dataset("naver-clova-ix/cord-v2")

# or: locally load
# step 1. download from huggingface
# git clone https://huggingface.co/datasets/naver-clova-ix/cord-v2
# step 2. locally load
# load_dataset("path/to/local/cord-v2")

if not os.path.exists(f'./{target_dir}'):
    os.mkdir(f'./{target_dir}')

for split in ['test', 'train', 'valid']:
    if split == 'valid':
        dataset = dataset_all['validation'] 
    else:
        dataset = dataset_all[split] 
    for sample in tqdm.tqdm(dataset):
        data_ori = json.loads(sample['ground_truth'])
        assert split == data_ori['meta']['split']
        split = data_ori['meta']['split']
        sample_id_str = f"{split}_{str(data_ori['meta']['image_id']).zfill(4)}"
        image_path = f'{target_dir}/{sample_id_str}.png'
        sample['image'].save(image_path)