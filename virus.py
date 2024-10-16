from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Virus detected!")
root.geometry("200x200")
def message():
    messagebox.showwarning("Alert!","Stop! Virus found!")
btn = Button(root,text="Scan for virus",command=message)
btn.place(x=40,y=80)
root.mainloop()