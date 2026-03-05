from tkinter import *
import os
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()
window.title("2D Animations Example")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file=os.path.join("data", "black_hole.png"))
background_image = background_image.subsample(7, 4)
background = canvas.create_image(0, 0, anchor=NW, image=background_image)

# background_image = PhotoImage(file=os.path.join("data", "sky.png"))
# background_image = background_image.subsample(7, 4)
# background = canvas.create_image(0, 0, anchor=NW, image=background_image)

photo_image = PhotoImage(file=os.path.join("data", "spaceship.png"))
photo_image = photo_image.subsample(3, 3)       
spaceship = canvas.create_image(0, 0, anchor=NW, image=photo_image)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(spaceship)
    print(coordinates)

    if coordinates[0] < 0 or coordinates[0] >= (WIDTH - image_width):
        xVelocity = -xVelocity
    if coordinates[1] < 0 or coordinates[1] >= (HEIGHT - image_height):
        yVelocity = -yVelocity
    canvas.move(spaceship, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()