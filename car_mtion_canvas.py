from tkinter import *
import os

window = Tk()
window.title("Car Motion Canvas Example")
window.geometry("500x500")

window.bind("<w>", lambda event: canvas.move(car, 0, -20))  # Move up
window.bind("<s>", lambda event: canvas.move(car, 0, 20))   # Move down
window.bind("<a>", lambda event: canvas.move(car, -20, 0))  # Move left
window.bind("<d>", lambda event: canvas.move(car, 20, 0))   # Move right

canvas = Canvas(window, width=500, height=500)
canvas.pack()

car_image = PhotoImage(file=os.path.join("data", "car.png"))
car_image = car_image.subsample(3, 3)

car = canvas.create_image(0, 0, anchor=NW, image=car_image) # Create the car image on the canvas
# synatx for create_image: canvas.create_image(x, y, anchor=NW, image=car_image)  anchor=NW means the top-left corner of the image will be at (x, y)

window.mainloop()