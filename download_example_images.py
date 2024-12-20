import os
import shutil
import stat
from datasets import load_from_disk
from PIL import Image
import numpy as np
from datasets import load_dataset

def download_and_extract_from_dataset(dataset_name,output_dir,image_dir):
    # Load the dataset
    print(f"Downloading the dataset: {dataset_name}")
    dataset = load_dataset(dataset_name)
    os.makedirs(image_dir, exist_ok=True)
    # Iterate through the dataset and save images
    print(f"Extracting images to: {image_dir}")
    for idx, sample in enumerate(dataset['train']):  # Use the appropriate split name
        # Convert image array to PIL Image
        image_array = sample['image']  # Adjust key to match your dataset
        image = Image.fromarray(np.array(image_array))
        # Save the image
        output_path = os.path.join(image_dir, f"image_{idx}.jpg")
        image.save(output_path)
    print("Images extracted successfully!")

dataset_name="harish03/catbreed"
output_dir = "./cat-breeds"
image_dir = 'example_images'
download_and_extract_from_dataset(dataset_name,output_dir,image_dir)