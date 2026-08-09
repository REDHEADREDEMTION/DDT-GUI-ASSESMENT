#import module
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#create root window
root= tk.Tk()


# Create an entry box
tk.Label(root,text="First Name").grid(row=0, column=0)
tk.Label(root,text="Last Name").grid(row=1, column=0)


entry1 = tk.Entry(root)
entry2 = tk.Entry(root)


entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
