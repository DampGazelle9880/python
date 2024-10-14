from tkinter import *
from datetime import datetime
def calculateage():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    birth_date = datetime(year,month,day)
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month,today.day)<(birth_date.month,birth_date.day))
    result_label.config(text=f"You're age is:{age} years")
root = Tk()
root.title("Age Calculator!")
Label(root,text="Enter your date of birth").pack(pady=10)
Label(root,text="Day:").pack()
day_entry = Entry(root)
day_entry.pack(pady=5)
Label(root,text="Month:").pack()
month_entry = Entry(root)
month_entry.pack(pady=5)
Label(root,text="Year:").pack()
year_entry = Entry(root)
year_entry.pack(pady=5)
Button(root,text="Calculate age",command=calculateage).pack(pady=20)
result_label = Label(root,text="")
result_label.pack()
root.mainloop()


