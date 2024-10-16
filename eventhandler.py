from tkinter import *
window = Tk()
window.title("Event Handler!")
window.geometry("200x100")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("The button was clicked.")
btn = Button(text="Click me!")
btn.pack()
btn.bind("<Button-1>",handle_click)
window.mainloop()