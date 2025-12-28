import tkinter as tk
import random


root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x300")




title_label = tk.Label(root, text="Guess the Number !" , font=("Arial" , 18))
title_label.pack(pady=18)


prompt_label = tk.Label(root, text="Enter a number (1-100):")
prompt_label.pack()


guess_entry = tk.Entry(root, width=10, justify="center")
guess_entry.pack(pady=5)


result_label = tk.Label(root, text ="Good luck!", font=("Arial", 14))


root.mainloop()
