#import modules
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import subprocess
import sys

conn = sqlite3.connect("Timeline_select.db")
cursor = conn.cursor()

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
    values=["Engineer", "physicest"],
)
house_menu.grid(column=2, row=1, columnspan=4, rowspan=2, sticky="nesw")

#this pice of code below, allows the drop down menu to
#create new windows for the jobs, mainly engineer as I am using it as a test
#I Used AI as normal website couldent give me the awnser that
def job_selected(event):
    selected_job = house.get()

    if selected_job == "Engineer":
        subprocess.Popen(["python", "RealProgect/SkeletonV3/Jobs/EngineeringWindow/Engineering.py"])
        root.destroy()

    elif selected_job == "Physicist":
        subprocess.Popen(["python", "RealProgect/SkeletonV3/Jobs/Physicist.py"])
        root.destroy()
        

house_menu.bind("<<ComboboxSelected>>", job_selected)

titleframe = tk.Frame(root)
titleframe.grid(column=3, row=1, columnspan=4, sticky="nesw")
titleframe.grid_columnconfigure((0), weight=1)
titleframe.grid_rowconfigure((0,1,2,3), weight=1)
tk.Label(titleframe, text="Engineer", font=("Ariel", 60, "underline")).grid(column=0, row=0, rowspan=3,)


# ==========================
# Timeline Frame (Scrollable)
# ==========================
# this code was made through the help of Chat GPT beacuse I was unable to 
# find help from a webstie to help with this pice of code

informationframe = tk.Frame(root, bg ="Green")
informationframe.grid(column=5, row=3, columnspan=4, rowspan=6, sticky="nesw")
informationframe.grid_rowconfigure(0, weight=1)
informationframe.grid_columnconfigure(0, weight=1)
informationframe.grid_propagate(False)

timelineframe = tk.Frame(root, bg="darkblue")
timelineframe.grid(column=1, row=3, columnspan=3, rowspan=6, sticky="nesw")
timelineframe.grid_rowconfigure(0, weight=1)
timelineframe.grid_columnconfigure(0, weight=1)
timelineframe.grid_propagate(False)
# ==========================
# Information Canvas
# ==========================

canvasinfo = tk.Canvas(
    informationframe,
    bg="pink",
    highlightthickness=0
)

canvasinfo.grid(
    row=0,
    column=0,
    sticky="nesw"
)


# Scrollbar for information
scrollbarInfo = ttk.Scrollbar(
    informationframe,
    orient="vertical",
    command=canvasinfo.yview
)

scrollbarInfo.grid(
    row=0,
    column=1,
    sticky="ns"
)


canvasinfo.configure(
    yscrollcommand=scrollbarInfo.set
)


# Frame INSIDE the canvas
infotext = tk.Frame(
    canvasinfo,
    bg="white"
)

canvasinfo.create_window(
    (0, 0),
    window=infotext,
    anchor="nw"
)


# Information label
infolable = tk.Label(
    infotext,
    text="",
    font=("Arial", 18),
    justify="left",
    anchor="nw",
    bg="white",
    fg="black",
    wraplength=500
)

infolable.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# Update scroll region whenever the information changes
def update_info_scroll(event=None):
    canvasinfo.configure(
        scrollregion=canvasinfo.bbox("all")
    )

infotext.bind(
    "<Configure>",
    update_info_scroll
)

def on_info_mousewheel(event):
    canvasinfo.yview_scroll(-int(event.delta / 120), "units")



# Canvas for timeline
canvas = tk.Canvas(
    timelineframe,
    bg="darkblue",
    highlightthickness=0
)
canvas.grid(row=0, column=0, sticky="nesw")

# Scrollbar for timeline
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

def on_timeline_mousewheel(event):
    canvas.yview_scroll(-int(event.delta / 120), "units")

def Timeline():
    cursor.execute('SELECT Description FROM engineer WHERE StepName= "Timeline"')
    result = cursor.fetchone()
    infolable.config(text=result[0])

def ncea_level2():
    cursor.execute('SELECT Description FROM engineer WHERE StepName= "Year 11"')
    result = cursor.fetchone()
    infolable.config(text=result[0])

def ncea_level3():
    cursor.execute('SELECT Description FROM engineer WHERE StepName= "Year 12"')
    result = cursor.fetchone()
    infolable.config(text=result[0])

def ncea_level4():
    cursor.execute('SELECT Description FROM engineer WHERE StepName= "Year 13"')
    result = cursor.fetchone()
    infolable.config(text=result[0])
    
def ncea_level5():
    cursor.execute('SELECT Description FROM engineer WHERE StepName= "University Entrence"')
    result = cursor.fetchone()
    infolable.config(text=result[0])

def ncea_level6():
    cursor.execute('SELECT Description FROM engineer WHERE StepName= "Bachelor of Engineering (Honours)"')
    result = cursor.fetchone()
    infolable.config(text=result[0])
    
def ncea_level7():
    cursor.execute('SELECT Description FROM engineer WHERE StepName= "Year 12"')
    result = cursor.fetchone()
    infolable.config(text=result[0])

def ncea_level8():
    print("Opening NCEA Level 8")

def ncea_level9():
    print("Opening NCEA Level 9")





btn1 = tk.Button(button_frame, text="NCEA Level 1", bg="red", width=25, height=5, command=Timeline)
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(button_frame, text="NCEA Level 2", bg="orange", width=25, height=5, command=ncea_level2)
btn2.grid(row=1, column=0, padx=5, pady=5)

btn3 = tk.Button(button_frame, text="NCEA Level 3", bg="yellow", width=25, height=5, command=ncea_level3)
btn3.grid(row=2, column=0, padx=5, pady=5)

btn4 = tk.Button(button_frame, text="NCEA Level 4", bg="green", width=25, height=5, command=ncea_level4)
btn4.grid(row=3, column=0, padx=5, pady=5)

btn5 = tk.Button(button_frame, text="NCEA Level 5", bg="cyan", width=25, height=5, command=ncea_level5)
btn5.grid(row=4, column=0, padx=5, pady=5)

btn6 = tk.Button(button_frame, text="NCEA Level 6", bg="blue", width=25, height=5, command=ncea_level6)
btn6.grid(row=5, column=0, padx=5, pady=5)

btn7 = tk.Button(button_frame, text="NCEA Level 7", bg="purple", width=25, height=5, command=ncea_level7)
btn7.grid(row=6, column=0, padx=5, pady=5)

btn8 = tk.Button(button_frame, text="NCEA Level 8", bg="pink", width=25, height=5, command=ncea_level8)
btn8.grid(row=7, column=0, padx=5, pady=5)

btn9 = tk.Button(button_frame, text="NCEA Level 9", bg="lightgreen", width=25, height=5, command=ncea_level9)
btn9.grid(row=8, column=0, padx=5, pady=5)



canvasinfo.bind(
    "<Enter>",
    lambda event: canvasinfo.bind_all(
        "<MouseWheel>",
        on_info_mousewheel
    )
)

canvasinfo.bind(
    "<Leave>",
    lambda event: canvasinfo.unbind_all("<MouseWheel>")
)


canvas.bind(
    "<Enter>",
    lambda event: canvas.bind_all(
        "<MouseWheel>",
        on_timeline_mousewheel
    )
)

canvas.bind(
    "<Leave>",
    lambda event: canvas.unbind_all("<MouseWheel>")
)










root.mainloop()