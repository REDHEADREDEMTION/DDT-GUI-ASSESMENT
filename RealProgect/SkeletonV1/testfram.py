import tkinter as tk

root = tk.Tk()
root.title("Frame Demo")
root.geometry('500x200')
frametop = tk.Frame(root, bg="lightblue", width=200, height=50, bd=3, relief=tk.RIDGE)
frametop.pack(padx=20, pady=20)


framebottom = tk.Frame(root, bg="darkblue", width=300, height=150, bd=3, relief=tk.RIDGE)
framebottom.pack(padx=70, pady=20)

label = tk.Label(frametop, text="This is a Frame", bg="lightblue")
label.pack(pady=20)

label = tk.Label(framebottom, text="bottom Frame", bg="darkblue")
label.pack(pady=20)

root.mainloop()