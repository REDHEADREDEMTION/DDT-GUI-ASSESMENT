import tkinter as tk
from tkinter import ttk

# EXCLAIMER: i apoligise for the shitty naming sceme this is souly for demonstraitave purposes
# the current method used is stacking 4 frames ontop of eachother inside of a frame
# then whenever an option is selected from the combo box it uses the .tkraise() func to bring it to the top
# the 4th frame (page) is used to block out the others when the page first opens
# do what you want with this code i dont really give a shit

root = tk.Tk()
root.geometry('1000x1000')
root.title('Ngaru_descriptionPages')
root['bg'] = '#ffffff'
f = ("Times bold", 14)

root.columnconfigure((0,2), weight=1)
root.rowconfigure((0,2), weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(1,weight=2)
root.grid_propagate(False)

descPageFrame = tk.Frame(root, bg="#000000")
descPageFrame.grid(sticky="nesw", column=1, row=1)
descPageFrame.columnconfigure(0, weight=1)
descPageFrame.rowconfigure(0, weight=1)

def page1():
    titleframe = tk.Frame(descPageFrame)
    titleframe.grid(column=0, row=0, sticky="nesw")
    titleframe.grid_columnconfigure((0), weight=1)
    titleframe.grid_rowconfigure((0,1,2,3), weight=1)
    tk.Label(titleframe, text="Cook", font=("Ariel", 60, "underline")).grid(column=0, row=0, rowspan=3,)

    #... rest of code for page 1
    return titleframe

def page2():
    page2Frame = tk.Frame(descPageFrame, bg="#00ff00")
    page2Frame.grid(sticky="nesw", column=0, row=0)
    tk.Label(page2Frame, text="page2").grid(sticky="nesw")
    #... rest of code for page 2
    return page2Frame

def page3():
    page3Frame = tk.Frame(descPageFrame, bg="#0000ff")
    page3Frame.grid(sticky="nesw", column=0, row=0)
    tk.Label(page3Frame, text="page3").grid(sticky="nesw")
    #... rest of code for page 3
    return page3Frame

def BlankPage(): #probs shit method for starting with a blank page and resource inefficient but its the easiest method rn
    blankPageFrame = tk.Frame(descPageFrame, bg="#0000ff")
    blankPageFrame.grid(sticky="nesw", column=0, row=0)
    return blankPageFrame

descPages = ["page1", "page2", "page3"]
Pages = [page1(), page2(), page3(), BlankPage()]

tk.Button(root, command=Pages[0].tkraise, text="page1").grid(column=0, row=0, sticky="n")
tk.Button(root, command=Pages[1].tkraise, text="page2").grid(column=0, row=0, sticky="n", pady=40)
tk.Button(root, command=Pages[2].tkraise, text="page3").grid(column=0, row=0, sticky="n", pady=80)



root.mainloop()