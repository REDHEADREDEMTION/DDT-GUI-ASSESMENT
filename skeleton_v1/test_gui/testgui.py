#import module
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk



#create root window
root= tk.Tk()

#root window title and dimensions
root.title("Welcome to GeekForGeeks")
#set geometry (width x hight)
root.geometry('500x200')


#adding a lable title root window
lbl = Label(root, text= "Are you a Geek")
lbl.grid()

#function to display text when button is clicked
#button is clicked
def clicked():
    lbl.configure(text= "I just got clicked")

#button wigth with red color text inside
btn = Button(root, text= "click me", 
             fg  ="red" , command=clicked)
btn.grid()


lable = tk.Label(root, text="Geeksfor geeks.org!")
lable.grid()

# Create an entry box
tk.Label(root,text="First Name").grid(row=0, column=0)
tk.Label(root,text="Last Name").grid(row=1, column=0)
tk.Label(root,text="email").grid(row=2, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)


# create/add an image
WINDOW_WIDTH = 50
HEADER_COLOUR = "#ffffff"
header = tk.Frame(root)
header.grid()


img = Image.open("skeleton_v1/banner.jpg").resize((WINDOW_WIDTH, 50))
_banner_img = ImageTk.PhotoImage(img)
label = tk.Label(header, image=_banner_img, bg=HEADER_COLOUR)
label.image = _banner_img  # keep reference
label.grid()

root.mainloop()



