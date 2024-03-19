#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Funtion to change the size of images for neural network processing

def resize_images_in_directory(input_dir, output_dir, target_size):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get list of image files in input directory
    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Initialize tqdm progress bar
    progress_bar = tqdm(total=len(image_files), desc="Resizing images", unit="image", leave=True)
    
    # Iterate through each image in the input directory
    for filename in image_files:
        # Load and resize the image
        img_path = os.path.join(input_dir, filename)
        image = tf.io.read_file(img_path)
        image = tf.image.decode_jpeg(image, channels=3)  # Ensure RGB channels
        resized_image = tf.image.resize(image, target_size)
        
        # Convert resized image tensor to uint8 data type
        resized_image = tf.cast(resized_image, tf.uint8)
        
        # Write the resized image to the output directory
        output_path = os.path.join(output_dir, filename)
        img_bytes = tf.image.encode_jpeg(resized_image)
        tf.io.write_file(output_path, img_bytes)
        
        # Update progress bar
        progress_bar.update(1)
    
    # Close progress bar
    progress_bar.close()

