import tkinter as tk
def calculateinterest():
    try:
        principle = float(entry_principle.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        simple_interest = (principle*rate*time)/100
        compound_interest = principle*((1+rate/100)**time)-principle
        result_label.config(text=f"Simple interest: {simple_interest:.2f}\n Compound interest: {compound_interest:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number:")
window = tk.Tk()
window.title("Interest Calculator!")
window.geometry("400x400")
tk.Label(window,text="Principle amount:").grid(row=0,column=0,padx=10,pady=10)
entry_principle = tk.Entry(window)
entry_principle.grid(row=0,column=1,padx=10,pady=10)
tk.Label(window,text="Rate of interest:").grid(row=1,column=0,padx=10,pady=10)
entry_rate = tk.Entry(window)
entry_rate.grid(row=1,column=1,padx=10,pady=10)
tk.Label(window,text="Time:").grid(row=2,column=0,padx=10,pady=10)
entry_time = tk.Entry(window)
entry_time.grid(row=2,column=1,padx=10,pady=10)
calculate_button = tk.Button(window,text="Calculate interest",command=calculateinterest)
calculate_button.grid(row=3,column=0,columnspan=2,pady=20)
result_label = tk.Label(window,text="")
result_label.grid(row=4,column=0,columnspan=2,pady=10)
window.mainloop()

