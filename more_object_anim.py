from tkinter import *
from ball import *
import time

window = Tk()
window.title("Animation")

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "blue")
tenis_ball = Ball(canvas, 0, 0, 50, 4, 3, "cyan")
cricket_ball = Ball(canvas, 0, 0, 70, 3, 2, "magenta")

while True:
    volley_ball.move()
    tenis_ball.move()
    cricket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()