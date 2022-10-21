#Display Images using tkinter GUI
from tkinter import *

m = Tk()
m.geometry("700x500")
photo = PhotoImage(file= r"C:\Users\aisha\Desktop\lakeimage.png")

img_label = Label(image=photo)
img_label.pack()
m.mainloop()
