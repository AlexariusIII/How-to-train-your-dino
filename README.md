# How-to-train-your-dino
How to setup dinoV2 for pretraining of cutsom data

# Pretraining Steps
## First Step: Clone the repository and install dependencies
### Clone Repository
- git clone https://github.com/facebookresearch/dinov2 
### Create Environment and Install dependencies
- conda create --name dino2 python=3.10
- conda env create --file env.yml
- conda activate dino2
- pip install -U -r dinov2/requirements.txt
- pip install -e dinov2/

## Second Step: Adjust dataset
For sake of simplicity we assume you have all your image files desired for pretraining are in a single folder. 
### Download example images for pretraining
As an example we will download a small image dataset containing cat breeds from huggingspace
- python download_example_images.py
### Reformat Data and add labels.txt
Next we need to reformat our data, since dinov2 expect data to be in the imageNet format:
    - data/root/train/classID/classID_image1.JPEG
    - data/root/train/classID/classID_image2.JPEG
    ...
    - data/root/val/classID/classID_image4.JPEG
    ...
    - data/root/test/classID/classID_image5.JPEG
    ...
The original dinov2 paper uses imageNet and requires the labels for the different classes for further downstram tasks. Since we want to pretrain on a custom dataset without labels we are using a single mock label (n77)
    - python reformat_data.py --data_dir example_images --target_dir data --class_id n77 --class_name cat
### Add extra files
Dinov2 requires some extra files for your dataset. Create them using:
    - python get_extra.py --root data/root --extra data/extra

## Dinov2 Code adjustments
### Add custom split numbers to dinov2 imageNet class
Count the number of images in each split:
    - python count_images.py --train_folder data/root/train --val_folder data/root/val
Adjust dinov2/dinov2/data/datasets/image_net.py with your numbers. 
### Modify config by adding your data paths and move to config folder
    - cp example.yaml dinov2/dinov2/configs/example.yml
###  Add line in train script to remove slurm dependency if applicable
in dinov2/dinov2/train/train.py you need to add an additional argument:
    - parser.add_argument("--local-rank", default=0, type=int, help="Variable for distributed computing.")
Alternatively just copy the given train.py and replace the old one:
    - cp train.py dinov2/dinov2/train/train.py

## Start training
To start the training on 2 full gpus (recommended):
    cd dinov2
    - torchrun --nproc_per_node=2 dinov2/train/train.py --config-file=dinov2/configs/example.yml --output-dir=outputs/

## Inference
TODO