from tkinter import *
from PIL import ImageTk, Image
import itertools
import random
background_color = "#0D865D" # kind of green

root = Tk()
root.geometry("960x900")

first_image_path = "./0.png" # sides of a die
second_image_path = "./0.png"

first_dice_image = ImageTk.PhotoImage(Image.open(first_image_path))
first_dice_label = Label(root, image = first_dice_image, bg = background_color)
first_dice_label.pack()

second_dice_image = ImageTk.PhotoImage(Image.open(second_image_path))
second_dice_label = Label(root, image = second_dice_image, bg = background_color)
second_dice_label.pack()

'''
    Roll Dice function
    This is going to return a dice combination by a tuple
    for example : (6,1) or (4,4)
'''

def roll_dice():
  dice_numbers = list(range(1,7)) # returns us 1 2 3 4 5 6
  combinations = list(itertools.product(dice_numbers, repeat = 2))

  rolled_dice = random.choice(combinations)
  return rolled_dice

def update_roll_dice_image():
    rolled_dice = list(roll_dice()) # returns [4,4]
    print(rolled_dice)

    new_first_image_path = "./{}.png".format(rolled_dice[0])
    new_second_image_path = "./{}.png".format(rolled_dice[1])

    new_first_dice_image = ImageTk.PhotoImage(Image.open(new_first_image_path))
    new_second_dice_image = ImageTk.PhotoImage(Image.open(new_second_image_path))

    first_dice_label.configure(image = new_first_dice_image)
    second_dice_label.configure(image = new_second_dice_image)

    first_dice_label.image = new_first_dice_image
    second_dice_label.image = new_second_dice_image

roll_button = Button(root, text = "Roll Dices!", command = update_roll_dice_image)
roll_button.pack(side = TOP)

root.configure(bg = background_color)
root.mainloop()
