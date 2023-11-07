from pathlib import Path
import shutil
import os

file_dir = r'/root/workspace/project/my-pytorch-CycleGAN-and-pix2pix/results/class_5_1/train_183/images'
target_dir = r'/root/workspace/data/YoloGan/train_data/detection/fake_class_5/kfold_1'

NEW_IMG_EXT = ".jpg"
for item in Path(file_dir).rglob("*.png"):
    if "_fake_B" not in item.name:
        continue
    item_name = item.name.split('.')[0]
    item_name = item_name.replace("_fake_B", "")
    item_name += NEW_IMG_EXT
    new_path = Path(target_dir, "train", "images", item_name)
    os.makedirs(new_path.parent, exist_ok=True)
    # print(new_path)
    os.symlink(str(item), str(new_path))
    
# for item in Path(file_dir, "test").rglob("*.png"):
#     if "_fake_B" not in item.name:
#         continue
#     item_name = item.name.split('.')[0]
#     item_name = item_name.replace("_fake_B", "")
#     item_name += NEW_IMG_EXT
#     new_path = Path(target_dir, "val", "images", item_name)
#     # print(new_path)
#     shutil.copy(str(item), str(new_path))
#     os.symlink(str(item), str(new_path))