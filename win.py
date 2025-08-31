import tkinter as tk

root = tk.Tk()
root.title("Buttons & Displays")

title_label = tk.Label(root, text="Hello Tkinter!", font=("Arial", 18))
title_label.pack(pady=10)

name_label = tk.Label (root, text="your name:")
name_label.pack()
name_entry = tk.Entry(root, text= "your name")
name_entry.pack(pady=5)
def say_hello():
    name = name_entry.get().strip()
    if name:
        pass

root.mainloop()
