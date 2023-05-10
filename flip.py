import os
from PIL import Image
import glob
import sys

def flip_image(image_path, output_folder):
    try:
        # Open the image
        image = Image.open(image_path)

        # Flip the image horizontally
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

        # Get the filename and extension
        file_name = os.path.basename(image_path)
        file_name, extension = os.path.splitext(file_name)

        # Define the flipped image path
        flipped_image_path = os.path.join(output_folder, file_name + '_flipped' + extension)

        # Save the flipped image
        flipped_image.save(flipped_image_path)
        print("Image flipped and saved as:", flipped_image_path)

        # Delete the original image file
        os.remove(image_path)
        print("Original image deleted:", image_path)
    except (OSError, IOError) as e:
        # Error occurred while opening or processing the image
        print(f"Error processing image: {image_path} - {e}")

# Provide the path to the folder containing the images in the Windows format
folder_path = r'file/path'

# Provide the path to the output folder where flipped images will be saved
output_folder = r'file/path'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Find all image files in the folder
image_files = glob.glob(os.path.join(folder_path, '*.jpg')) + glob.glob(os.path.join(folder_path, '*.png'))

# Process each image file
for image_file in image_files:
    flip_image(image_file, output_folder)

# Exit the script
sys.exit()
