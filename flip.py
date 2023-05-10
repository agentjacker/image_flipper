#pip install Pillow

import os
from PIL import Image

def flip_image(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Flip the image horizontally
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    # Save the flipped image
    flipped_image.save('flipped_' + image_path)
    print("Image flipped and saved as 'flipped_" + image_path + "'.")

# Provide the path to the folder containing the images
folder_path = '/path/to/folder'

# List all files in the folder
files = os.listdir(folder_path)

# Process each file in the folder
for file in files:
    # Check if the file is an image (you can modify the condition to match specific image formats)
    if file.endswith('.jpg') or file.endswith('.png'):
        # Create the full path to the image file
        image_path = os.path.join(folder_path, file)
        flip_image(image_path)
