#import modules
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime

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
img = Image.open("RealProgect/SkeletonV1/Images/Logo.png")
img = img.resize((40, 40), Image.LANCZOS)
_banner_img = ImageTk.PhotoImage(img)
label = tk.Label(searchframe, image=_banner_img)
label.image = _banner_img  # keep reference
label.grid(column=0, row=0, sticky="nesw" )





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
        subprocess.Popen(["python", "SkeletonV2/Jobs/Engineering.py"])
        root.destroy()

    elif selected_job == "Physicist":
        subprocess.Popen(["python", "SkeletonV2/Jobs/Physicist.py"])
        root.destroy()


        

house_menu.bind("<<ComboboxSelected>>", job_selected)

#this is a frame for the information box of my website that will keep the information safe.
titleframe = tk.Frame(root,bg="orange", relief=tk.RIDGE)
titleframe.grid(column=1, row=3, sticky="nesw", rowspan=5, columnspan=8)
titleframe.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
titleframe.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)


#I am creating the title of the main page.
tk.Label(titleframe, text="Find your career").grid(row=1, column=4, columnspan=3, sticky="nesw")

#creating a information frame to fo into the titleframe so that I can asteticaly design the layout
information = tk.Frame(titleframe, bg="red")
information.grid(column=1, row=3, columnspan=9, rowspan=7, sticky="nesw")
information.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
information.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
for ix in range(11):
    for iy in range(11):
        tk.Frame(information, bd=3, relief=tk.RIDGE).grid(sticky="nesw",column=ix, row=iy)

#below is all the texts and text boxes that will have the information.
tk.Label(information, text= """This is a app that allows you to research 
your jobs for the future efectivly""").grid(row=2, column=0, rowspan=6, columnspan=3, sticky="nesw")

tk.Label(information, text= """if your ever confused or strugiling your
way through life then just open
up Loan and search you way""").grid(row=2, column=4, rowspan=6, columnspan=3, sticky="nesw")

tk.Label(information, text= """We are here to help and serve 
you and to accomidat your needs.""").grid(row=2, column=8, rowspan=6, columnspan=3, sticky="nesw")




root.mainloop()


