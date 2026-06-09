#import module
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#create root window
root= tk.Tk()

#root window title and dimensions
root.title("Welcome to GeekForGeeks")
#set geometry (width x hight)
root.geometry('800x800')

searchframe = tk.Frame(root, bg="lightblue", width=500, height=100, bd=3, relief=tk.RIDGE)
searchframe.pack(padx=20, pady=20)

img = Image.open("RealProgect/SkeletonV1/Images/Logo.png")
img = img.resize((100, 100), Image.LANCZOS)
_banner_img = ImageTk.PhotoImage(img)
label = tk.Label(image=_banner_img)
label.image = _banner_img  # keep reference
label.grid()

root.mainloop()


