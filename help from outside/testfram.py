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
root.grid_columnconfigure((0,1,2,3,4), weight=1)
root.grid_columnconfigure((5,6,7,8,9), weight=2)
root.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
for ix in range(10):
    for iy in range(10):
        tk.Frame(root, bd=3, relief=tk.RIDGE).grid(sticky="nesw",column=ix, row=iy)

tk.Frame(root, bg="red").grid(column=2, columnspan=2, row=1, rowspan=4)

root.mainloop()