#import module
from tkinter import *

from PIL Image, ImageTk



#create root window
root  = Tk()

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

btn.grid(column=1, row=0)
img = Image.open(/images/daniel-farrelly-grace.png).resize((WINDOW_WIDTH, 80))
_banner_img = ImageTk.photoImage(img)
tk.lable(header, image=_banner_img, bg=HEADER_COLOUR).pack
Root.mainloop()



