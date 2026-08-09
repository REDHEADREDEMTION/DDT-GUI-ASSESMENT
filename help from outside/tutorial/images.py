#import module
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#create root window
root= tk.Tk()




# create/add an image
WINDOW_WIDTH = 800
HEADER_COLOUR = "#ffffff"
header = tk.Frame(root)
header.grid()


img = Image.open("skeleton_v1/banner.png").resize((WINDOW_WIDTH, 800))
_banner_img = ImageTk.PhotoImage(img)
label = tk.Label(header, image=_banner_img, bg=HEADER_COLOUR)
label.image = _banner_img  # keep reference
label.grid()