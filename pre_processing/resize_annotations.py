#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function to resize annotations if data/images have been resized

def resize_annotations(annotations, target_size):
    # Calculate scaling factors for width and height
    scale_w = target_size[0] / annotations['images'][0]['width']
    scale_h = target_size[1] / annotations['images'][0]['height']
    
    # Loop through each annotation
    for annotation in annotations['annotations']:
        # Update bounding box coordinates
        annotation['bbox'][0] *= scale_w  # x-coordinate
        annotation['bbox'][1] *= scale_h  # y-coordinate
        annotation['bbox'][2] *= scale_w  # width
        annotation['bbox'][3] *= scale_h  # height
    
    # Update image size in annotations
    annotations['images'][0]['width'] = target_size[0]
    annotations['images'][0]['height'] = target_size[1]
    
    return annotations


# In[ ]:


# Function to adjust annotations with the first function resize_annotations()

def adjust_annotations(annotations_path, output_dir, target_size):
    # Load annotations from file
    with open(annotations_path, 'r') as f:
        annotations = json.load(f)

    # Resize annotations
    resized_annotations = resize_annotations(annotations, target_size)

    # Save adjusted annotations to a new file
    output_filename = os.path.basename(annotations_path)
    output_annotations_path = os.path.join(output_dir, output_filename)
    with open(output_annotations_path, 'w') as f:
        json.dump(resized_annotations, f)

