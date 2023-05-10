#pip install Pillow

from PIL import Image

def flip_image(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Flip the image horizontally
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    # Save the flipped image
    flipped_image.save('flipped_' + image_path)
    print("Image flipped and saved as 'flipped_" + image_path + "'.")

# Provide the path to your 'image.txt' file here
image_list_path = 'image.txt'

# Read the image file paths from 'image.txt'
with open(image_list_path, 'r') as file:
    image_paths = file.read().splitlines()

# Process each image in the list
for image_path in image_paths:
    flip_image(image_path)
