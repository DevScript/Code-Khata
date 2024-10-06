# First Run:
# pip install pillow


from PIL import Image
import os

def split_image(image_path, orientation, num_parts, output_path):
    # Open the image file
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Determine the folder name based on the image name
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    folder_path = os.path.join(output_path, image_name)

    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Split image horizontally or vertically
    if orientation.lower() == 'horizontal':
        piece_height = img_height // num_parts
        for i in range(num_parts):
            box = (0, i * piece_height, img_width, (i + 1) * piece_height)
            piece = img.crop(box)
            piece_name = f"{image_name}_horizontal_piece{i+1}.png"
            piece.save(os.path.join(folder_path, piece_name))
    elif orientation.lower() == 'vertical':
        piece_width = img_width // num_parts
        for i in range(num_parts):
            box = (i * piece_width, 0, (i + 1) * piece_width, img_height)
            piece = img.crop(box)
            piece_name = f"{image_name}_vertical_piece{i+1}.png"
            piece.save(os.path.join(folder_path, piece_name))
    
    print("Splitting done. Files saved to:", folder_path)
    input("Press any key to exit")

if __name__ == "__main__":
    # Get inputs from user
    image_path = input("Enter the image path: ")
    orientation = input("Do you want to split the image horizontally or vertically? (horizontal/vertical): ")
    num_parts = int(input("How many parts do you want to split the image into? "))
    output_path = input("Enter the folder path where you want to save the files: ")

    # Call the function to split the image
    split_image(image_path, orientation, num_parts, output_path)
