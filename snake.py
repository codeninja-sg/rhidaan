import tkinter as tk 
import random 
root = tk.TK()
root.title ("Snake - 1 ")

SIZE = 20 
W = 400
H = 400

canvas = tk.Canvas(root, width=W, height=H, bg= "White")
canvas.pack()

snake = (10, 10)

dx=1
dy=0

food = (random.randint(0, W//SIZE - 1)
        random.randint(0, H//SIZE - 1))

def draw ():
    canvas.delete("all")

    fx, fy = food 
    canvas.create_rectangle(fx*SIZE, fy*SIZE,
                            fx*SIZE+SIZE , y*SIZE+SIZE,
                            fill="green")


    for (x , y) in snake:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                                 x*SIZE+SIZE, y*SIZE+SIZE,
                                 fill= "green")
        
def game_loop():
    print()

root.mainloop()
