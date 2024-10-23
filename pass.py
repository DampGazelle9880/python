from tkinter import *
from tkinter import messagebox
def evaluate():
    password = entry.get()
    lenght = len(password)
    if lenght == 0:
        messagebox.showerror("Error!","Please enter a valid password:")
    elif lenght < 6:
        result_label.config(text="Password Strenght: Weak",fg="red")
    else:
        result_label.config(text="Password Strenght: Strong",fg="green")
root = Tk()
root.title("Password Strength Checkup!")
root.geometry("400x400")
root.configure(bg="light grey")
label = Label(root,text="Enter your password:",bg="light grey")
label.pack(pady=10)
entry = Entry(root,show="*",width=30)
entry.pack(pady=5)
btn = Button(root,text="Check strenght!",command=evaluate,bg="blue",fg="white")
btn.pack(pady=10)
result_label = Label(root,text="",bg="light grey")
result_label.pack(pady=5)
root.mainloop()