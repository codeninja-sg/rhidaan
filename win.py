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
        title_label.config(text=f"Hello,{name}!")
    else:
        title_label.config(text="Hello , Tkinter")
hello_btn = tk.Button(root,text= "Say Hello", command=say_hello)
hello_btn.pack(pady=5)

clicks = tk.IntVar(value=0)
def count_click():
    clicks.set(clicks.get)()( + 1)
    counter_label.config(text=f"clicks: {clicks.get}")
    




root.mainloop()
