#import modules
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import subprocess
import sys

#create root window
root= tk.Tk()
root.title("Make a better choice")

#set geometry (width x hight)
root.geometry('800x800')
root.config(width=9, height=9)
root.state("zoomed")
root.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
root.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
for ix in range(10):
    for iy in range(10):
        tk.Frame(root, bd=3, relief=tk.RIDGE).grid(sticky="nesw",column=ix, row=iy)

#create a frame for the search bar.
searchframe = tk.Frame(root, bg="lightblue", bd=3, relief=tk.RIDGE)
searchframe.grid(padx=20, pady=20, row=0, column=0, columnspan=2, rowspan=1, sticky="nesw")
searchframe.grid_propagate(False)
searchframe.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
searchframe.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
searchframe.grid_propagate(False)

#add an image to the search frame as a logo
#TO turn the image into a button and allow it to go to the home page I used chatgpt
def go_home():
    subprocess.Popen([sys.executable, "RealProgect/SkeletonV3/Gui.py"])
    root.destroy()


img = Image.open("RealProgect/SkeletonV3/Images/Logo.png")
img = img.resize((40, 40), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(img)

home_button = tk.Button(
    searchframe,
    image=logo_img,
    command=go_home,
    borderwidth=0,
    relief="flat",
    highlightthickness=0,
    cursor="hand2"
)

home_button.image = logo_img
home_button.grid(column=0, row=0, sticky="nesw")



# Her I created the drop down menu for the 5 jobs of my choice
tk.Label(searchframe, text="Select Job:").grid(column=2, row=0, columnspan=4, rowspan=1, sticky="nesw")
house = tk.StringVar(value="Choose job")
house_menu = ttk.Combobox(
    searchframe,
    textvariable=house,
    values=["Engineer", "Physicist"],
)
house_menu.grid(column=2, row=1, columnspan=4, rowspan=2, sticky="nesw")

#this pice of code below, allows the drop down menu to
#create new windows for the jobs, mainly engineer as I am using it as a test
#I Used AI as normal website couldent give me the awnser that
def job_selected(event):
    selected_job = house.get()

    if selected_job == "Engineer":
        subprocess.Popen(["python", "RealProgect/SkeletonV3/Jobs/Engineering.py"])
        root.destroy()

    elif selected_job == "Physicist":
        subprocess.Popen(["python", "RealProgect/SkeletonV3/Jobs/Physicist.py"])
        root.destroy()


        

house_menu.bind("<<ComboboxSelected>>", job_selected)

titleframe = tk.Frame(root)
titleframe.grid(column=3, row=1, columnspan=4, sticky="nesw")
titleframe.grid_columnconfigure((0), weight=1)
titleframe.grid_rowconfigure((0,1,2,3), weight=1)
tk.Label(titleframe, text="Physicist", font=("Ariel", 60, "underline")).grid(column=0, row=0, rowspan=3,)




root.mainloop()