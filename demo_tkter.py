from tkinter import *
from datetime import date
root = Tk("Getting started with widgets!")
root.geometry("400x300")

lbl = Label(root,text="Hello",fg="white",bg="#072F5F",height="1",width="300")
lbl.pack()
name_label = root,text="Full Name?",bg="#3895BD"
name_label.pack()
name_entry = Entry(root)
name_entry.pack()
def display():
    name = name_entry.get()
    message = "Welcome To The Application! \n today's date is:"   
    greet = "Hello" + name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,str(date.today()))
text_box = Text(root,height=5,width=50)
text_box.pack()
btn = Button(root,text="begin",command=display,height=1,bg="#1261A0",fg="white")
btn.pack()
root.mainloop()