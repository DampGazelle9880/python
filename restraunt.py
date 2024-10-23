import tkinter as tk 
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
class Resterauntordermangement:
    def __init__(self,root):
        self.root = root
        self.root.title("Resterant Management App!")
        self.menu_items = {"Fries meal":2,"A lunch meal":2,"Burger meal":3,"Pizza meal":4,"Cheese burger":2.5,"Drinks":1}
        self.exchange_rate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Resteraunt Order Management",font=("Ariel",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i ,(item,price) in enumerate(self.menu_items.items(),start=1):
            label = ttk.Label(frame,text=f"{item} (${price}):",font=("Ariel",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_labels[item] =label
            quantity_entry = ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item] =quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(frame,text="Currency:",font=("Ariel",12)).grid(row=len(self.menu_items)+1,column=0,padx=10,pady=5)
        currency_dropdown = ttk.Combobox(frame,textvariable=self.currency_var,state="readonly",width=18,values=('USD','PKR'))
        currency_dropdown.current(0)
        self.currency_var.trace('w',self.updatemenuprice)
        order_btn = ttk.Button(frame,text="Place order:",command=self.placeorder)
        order_btn.grid(row=len(self.menu_items)+2,columnspan=3,padx=10,pady=10)
    def setup_background(self,root):
        bg_width,bg_heigth = 800,600
        canvas = tk.Canvas(root,width=bg_width,height=bg_heigth)
        canvas.pack()
        orignalimage = Image.open("rest.png")
        resizerimage = orignalimage.resize((bg_width,bg_heigth),Image.LANCZOS)
        background_image = ImageTk.PhotoImage(resizerimage)
        canvas.create_image(0,0,anchor=tk.NW,image=background_image)
        canvas.image = background_image
    def updatemenuprice(self,*args):
        currency = self.currency_var.get()
        symbol = "Rs" if currency == "PKR"else"$"
        rate = self.exchange_rate if currency == "PKR"else 1
        for item,label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")
    def placeorder(self):
        totalcost = 0
        ordersummary = "Order summary:\n"
        currency = self.currency_var.get()
        symbol = "Rs" if currency == "PKR"else"$"
        rate = self.exchange_rate if currency == "PKR"else 1
        for item,entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                totalcost += cost
                if quantity > 0:
                    ordersummary += f"{item}: {quantity}x{symbol}{price}= {symbol}{cost}\n"
        if totalcost > 0:
            ordersummary += f"\nTotal cost: {symbol}{totalcost}"
            messagebox.showinfo("Order placed",ordersummary)
        else:
            messagebox.showerror("Error!","Please order at least one item")
if __name__ == "__main__":
    root = tk.Tk()
    app = Resterauntordermangement(root)
    root.geometry("800x600")
    root.mainloop()