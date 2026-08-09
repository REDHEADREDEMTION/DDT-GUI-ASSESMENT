#import module
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#create root window
root= tk.Tk()


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