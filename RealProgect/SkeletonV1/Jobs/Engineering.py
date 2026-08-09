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
    subprocess.Popen([sys.executable, "RealProgect/SkeletonV1/Gui.py.py"])
    root.destroy()


img = Image.open("RealProgect/SkeletonV1/Images/Logo.png")
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
    values=["Engineer", "physicest", "electrical engineer", "cook", "macdonalds worker"],
)
house_menu.grid(column=2, row=1, columnspan=4, rowspan=2, sticky="nesw")

#this pice of code below, allows the drop down menu to
#create new windows for the jobs, mainly engineer as I am using it as a test
#I Used AI as normal website couldent give me the awnser that
def job_selected(event):
    selected_job = house.get()

    if selected_job == "Engineer":
        subprocess.Popen(["python", "RealProgect/SkeletonV1/Jobs/Engineering.py"])
        root.destroy()

    elif selected_job == "physicest":
        subprocess.Popen(["python", "RealProgect/SkeletonV1/Jobs/physicest.py"])
        root.destroy()

    elif selected_job == "electrical engineer":
        subprocess.Popen(["python", "RealProgect/SkeletonV1/Jobs/electrical_engineer.py"])
        root.destroy()

    elif selected_job == "cook":
        subprocess.Popen(["python", "RealProgect/SkeletonV1/Jobs/cook.py"])
        root.destroy()

    elif selected_job == "macdonalds worker":
        subprocess.Popen(["python", "RealProgect/SkeletonV1/Jobs/macdonalds_worker.py"])
        root.destroy()
        

house_menu.bind("<<ComboboxSelected>>", job_selected)

titleframe = tk.Frame(root)
titleframe.grid(column=3, row=1, columnspan=4, sticky="nesw")
titleframe.grid_columnconfigure((0), weight=1)
titleframe.grid_rowconfigure((0,1,2,3), weight=1)
tk.Label(titleframe, text="Engineer", font=("Ariel", 60, "underline")).grid(column=0, row=0, rowspan=3,)

# this code was mad through the help of Chat GPT beacuse I was unable to find help from a webstie to help with this pice of code
# ==========================
# Timeline Frame (Scrollable)
# ==========================

timelineframe = tk.Frame(root, bg="darkblue")
timelineframe.grid(column=1, row=3, columnspan=3, rowspan=6, sticky="nesw")

timelineframe.grid_rowconfigure(0, weight=1)
timelineframe.grid_columnconfigure(0, weight=1)

# Canvas
canvas = tk.Canvas(
    timelineframe,
    bg="darkblue",
    highlightthickness=0
)
canvas.grid(row=0, column=0, sticky="nesw")

# Scrollbar
scrollbar = ttk.Scrollbar(
    timelineframe,
    orient="vertical",
    command=canvas.yview
)
scrollbar.grid(row=0, column=1, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

# Frame that holds all buttons
button_frame = tk.Frame(canvas, bg="darkblue")

canvas.create_window(
    (0, 0),
    window=button_frame,
    anchor="nw"
)

# Update scroll region
button_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# Mouse wheel scrolling (Windows)
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def button_clicked(number):
    print(f"Button {number} clicked")

for i in range(20):

    btn = tk.Button(
        button_frame,
        text=f"Timeline Step {i+1}",
        bg="orange",
        width=25,
        height=5,
        font=("Arial", 14),
        command=lambda x=i+1: button_clicked(x)
    )

    btn.pack(pady=15)

canvas.bind_all("<MouseWheel>", on_mousewheel)






informationframe = tk.Frame(root, bg ="Green")
informationframe.grid(column=5, row=3, columnspan=4, rowspan=6, sticky="nesw")




root.mainloop()