from tkinter import *
def converttocentimeter():
    try:
        inches = float(entry.get())
        centimeters = inches*2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number:")
root = Tk()
root.title("Inches to Centimetres Convertor")
root.geometry("300x150")
Label(root,text="Enter lenght in inches:").pack(pady=5)
entry = Entry(root)
entry.pack(pady=5)
convert_btn = Button(root,text="Convert",command=converttocentimeter)
convert_btn.pack(pady=5)
result_label = Label(root,text="")
result_label.pack(pady=5)
root.mainloop()