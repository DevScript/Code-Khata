# Installation of pillow library - pip install Pillow
# change the image extension
# resize image files
# resize multiple images using for loop
# Sharpness
# Brightness
# Color
# Contrast
# Image Blur, GaussianBlur

from PIL import Image, ImageEnhance, ImageFilter
import os

img1 = Image.open(r'Images\img1.jpg')
# Change extension
img1.save(r'Edited Images\img1.png')
img1.show()

# Resize
MAX_SIZE = (250, 250)
img1.thumbnail(MAX_SIZE)
img1.save(r'Edited Images\img1_small.png')

for item in os.listdir('Images'):
    if item.endswith('.jpg'):
        img = Image.open(f'Images\\{item}')
        filename, extension = os.path.splitext(item)
        img.save(f'Edited Images\\{filename}.png')

sharpness_obj = ImageEnhance.Sharpness(img1)
sharpness_obj.enhance(4).save(r'Edited Images\cat_edited.jpg')
print(type(sharpness_obj))
# 0 : blurry
# 1 : original image
# 2 : image with increased sharpness

color_obj = ImageEnhance.Color(img1)
color_obj.enhance(4).save(r'Edited Images\cat_edited.jpg')
# 0 : black and white
# 1 : original image
# 2 : image with increased colors

bright_obj = ImageEnhance.Brightness(img1)
bright_obj.enhance(3).save(r'Edited Images\cat_edited.jpg')
# 0 : black
# 1 : original image
# 2 : image with increased brightness

contrast_obj = ImageEnhance.Contrast(img1)
contrast_obj.enhance(3).save(r'Edited Images\cat_edited.jpg')
# 0 : black
# 1 : original image
# 2 : image with increased brightness

img1.filter(ImageFilter.GaussianBlur()).save(r'Edited Images\cat_blur.jpg')
