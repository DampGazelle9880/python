import tkinter as tk
from tkinter import messagebox
import random
def determinewinner(userchoice,computerchoice):
    if userchoice == computerchoice:
        return "It is a tie!"
    elif (userchoice == "rock"and computerchoice == "scissors") or \
        (userchoice == "scissors"and computerchoice == "paper") or \
           (userchoice == "paper"and computerchoice == "rock"):
               return "You win!"
    else:
        return "Computer wins!"
def user_choice(choice):
    computerchoice = random.choice(["rock","paper","scissors"])
    result = determinewinner(choice,computerchoice)
    result_label.config(text=f"Computer choose: {computerchoice}\n{result}")
root = tk.Tk()
root.title("Rock,paper and scissors game!")
title_label = tk.Label(root,text="rock,paper and scissors",font=("Helvetica",18))
title_label.pack(pady=10)
rock_btn = tk.Button(root,text="rock",width=15,command=lambda:user_choice("rock"))
rock_btn.pack(pady=5)
paper_btn = tk.Button(root,text="paper",width=15,command=lambda:user_choice("paper"))
paper_btn.pack(pady=5)
scissors_btn = tk.Button(root,text="scissors",width=15,command=lambda:user_choice("scissors"))
scissors_btn.pack(pady=5)
result_label = tk.Label(root,text="",font=("Helvetica",14))
result_label.pack(pady=20)
root.mainloop()
               
  