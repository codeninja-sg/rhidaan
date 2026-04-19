import tkinter as tk
import random 

root = tk.Tk()
root.title("ball drop")

W = 400
H = 500

Speed = 20

canvas = tk.Canvas(root, width=W, height=H, bg= 'black')
canvas.pack()

pad_w = 90
pad_h = 12
pad_x = W // 2
pad_y = H - 40

Paddle = canvas.create_rectangle(pad_x - pad_w//2, pad_y - pad_h//2, pad_x + pad_w//2, pad_y + pad_h//2, fill= 'cyan', outline='')

def move_left(event):
    global pad_x
    pad_x -= Speed 


    if pad_x < pad_w // 2:
        pad_x = pad_w // 2
        canvas.coords(Paddle, pad_x - pad_w//2, pad_y - pad_h//2, pad_x + pad_w//2, pad_y + pad_h//2)

def move_right(event):
    global pad_x
    pad_x += Speed 

    if pad_x > W - pad_w // 2:
        pad_x = W - pad_w // 2
        canvas.coords(Paddle, pad_x - pad_w//2, pad_y - pad_h//2, pad_x + pad_w//2, pad_y + pad_h//2)

root.bind('<Left>', move_left)
root.bind('<Right>', move_right)

ball_r = 12
ball_x = W // 2
ball_y = 100
ball_dx = 3
ball_dy = 3

ball = canvas.create_oval( ball_x - ball_r, ball_y - ball_r, ball_x + ball_r, ball_y + ball_r, fill= 'white' , outline='')

score  = 0
game_over = False

score_label =tk.Label(root, text='score: 0',
                      font=('Arial', 14), bg='black', fg='White')
score_label.pack()

def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy, score, game_over

    if game_over:
        return
    
    ball_x += ball_dx
    ball_y += ball_dy
    
                    

                        

root.mainloop()










