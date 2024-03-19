#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function to copy filtered images to new directory
# NEEDS: Initialized coco instances, mapped categories, directories to save filtered files


def copy_filtered_images(coco, img_ids, image_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for img_id in img_ids:
        img_info = coco.loadImgs(img_id)[0]
        img_file = os.path.join(image_dir, img_info['file_name'])
        shutil.copy(img_file, output_dir)

