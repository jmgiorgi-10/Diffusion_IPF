
import os
from PIL import Image

# Define the folder and file filter
folder_path = "."  # Replace with your folder path
search_string = "Ti7_1"  # Replace with your search string
output_folder = "./lr_64"  # Output folder for resized images
os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

# Resize dimensions
new_width = 64
new_height = 64

# Loop through files in the folder
for file_name in os.listdir(folder_path):
    if search_string in file_name and file_name.endswith((".png")):  # Filter by string and extensions
        input_path = os.path.join(folder_path, file_name)
        output_path = os.path.join(output_folder, file_name)
        
        # Open and resize the image
        with Image.open(input_path) as img:
            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_path)
        
        print(f"Resized {file_name} to {new_width}x{new_height} and saved as {output_path}")

print("Batch resizing completed.")