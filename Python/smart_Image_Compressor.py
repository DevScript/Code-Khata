# pip install pillow

from PIL import Image
import os

def compress_image(image_path, output_path, quality=85):
    # Open the image
    img = Image.open(image_path)
    
    # Ensure output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Define the output file path
    image_name = os.path.basename(image_path)
    output_file = os.path.join(output_path, f"compressed_{image_name}")

    # Compress and save the image
    img.save(output_file, "JPEG", optimize=True, quality=quality)
    print(f"Image compressed and saved to {output_file}")

if __name__ == "__main__":
    image_path = input("Enter the image file path: ")
    output_path = input("Enter the output folder path: ")
    quality = int(input("Enter the desired quality (1-100, 100 is best quality): "))
    
    compress_image(image_path, output_path, quality)
