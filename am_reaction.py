import tkinter as tk
import random
import time

root = tk.Tk()
root,title("Reaction Timer")
root.geometry("400x250")

title_label = tk.Label(root, text="Reaction Timer" , font="Arial" , 20)
title_label.pack(pady=20)

info_label = tk.Label(root, text="press start to begin" , font=("Arial" , 14))
info_label.pack(pady=20)

start_btn = tk.Button(root, text="stop" , width=10)

root.mainloop()

