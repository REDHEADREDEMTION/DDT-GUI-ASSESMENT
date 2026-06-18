#import module
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

#create root window
root= tk.Tk()

#root window title and dimensions
root.title("Welcome to GeekForGeeks")
#set geometry (width x hight)
root.geometry('800x800')
root.config(width=9, height=9)
root.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
root.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
for ix in range(10):
    for iy in range(10):
        tk.Frame(root, bd=3, relief=tk.RIDGE).grid(sticky="nesw",column=ix, row=iy)

searchframe = tk.Frame(root, bg="lightblue", bd=3, relief=tk.RIDGE)
searchframe.grid(padx=20, pady=20, row=0, column=0, columnspan=4, rowspan=2, sticky="nesw")
searchframe.grid_propagate(False)
searchframe.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
searchframe.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
for ix in range(10):
    for iy in range(10):
        tk.Frame(searchframe, bd=3, relief=tk.RIDGE).grid(sticky="nesw",column=ix, row=iy)

img = Image.open("RealProgect/SkeletonV1/Images/Logo.png")
img = img.resize((40, 40), Image.LANCZOS)
_banner_img = ImageTk.PhotoImage(img)
label = tk.Label(searchframe, image=_banner_img)
label.image = _banner_img  # keep reference
label.grid(column=0, row=0, sticky="nw" )


# --- Dropdown (houses) ---
tk.Label(searchframe, text="Select Job:").grid(column=1, row=0, columnspan=4, rowspan=1, sticky="nesw")
house = tk.StringVar(value="Choose job")
house_menu = ttk.Combobox(
    searchframe,
    textvariable=house,
    values=["Engineer", "physicest", "electrical engineer", "cook", "macdonalds worker"]# stops users typing their own text
)
house_menu.grid(column=1, row=1, columnspan=4, rowspan=2, sticky="nesw")

titleframe = tk.Frame(root,bg="orange", relief=tk.RIDGE)
titleframe.grid(column=0, row=2, sticky="nesw", rowspan=5, columnspan=4, padx=20, pady=20)
titleframe.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
titleframe.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
for ix in range(10):
    for iy in range(10):
        tk.Frame(titleframe, bd=3, relief=tk.RIDGE).grid(sticky="nesw",column=ix, row=iy)

tk.Label(titleframe, text="Find your career").grid(row=1, column=2)







root.mainloop()


