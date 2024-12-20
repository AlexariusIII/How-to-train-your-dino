import os
import shutil
import argparse

def split_and_reformat_data(data_dir='example_images', target_dir='data', class_name='n77'):
    # Load image source
    images = os.listdir(data_dir)

    # Split data
    split_dict = {
        'train': images[:-10],
        'val': images[-10:-5],
        'test': images[-5:],
    }
    print(f"Train size: {len(split_dict['train'])}")
    print(f"Val size: {len(split_dict['val'])}")
    print(f"Test size: {len(split_dict['test'])}")

    # Reformat data
    target_root = os.path.join(target_dir, 'root')
    os.makedirs(target_root, exist_ok=True)

    for split in ['train', 'val', 'test']:
        split_dir = os.path.join(target_root, split, class_name)
        os.makedirs(split_dir, exist_ok=True)
        for img in split_dict[split]:
            src = os.path.join(data_dir, img)
            img_name = img.split('_')[-1]
            img_name = f"{img_name.split('.')[0]}.JPEG"
            dst = os.path.join(split_dir, f"{class_name}_{img_name}")
            shutil.copyfile(src, dst)


def add_labels(target_dir,class_id,class_name):
    # Create labels.txt
    target_dir = os.path.join(target_dir,'root')
    labels_file = os.path.join(target_dir, 'labels.txt')
    with open(labels_file, 'w') as f:
        f.write(f"{class_id},{class_name}\n")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Split and reformat image dataset.")
    parser.add_argument('--data_dir', type=str, default='example_images', help="Path to the source directory containing images.")
    parser.add_argument('--target_dir', type=str, default='data', help="Path to the target directory where the reformatted dataset will be saved.")
    parser.add_argument('--class_id', type=str, default='n77', help="Class name to label the images.")
    parser.add_argument('--class_name', type=str, default='cat', help="Class name to label the images.")
    args = parser.parse_args()

    # Call the function with parsed arguments
    split_and_reformat_data(args.data_dir, args.target_dir, args.class_id)
    add_labels(args.target_dir, args.class_id, args.class_name)


