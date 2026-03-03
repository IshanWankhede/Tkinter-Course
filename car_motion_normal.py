from tkinter import *
import os 

def move_up(event):
    x = car_label.winfo_x()
    y = car_label.winfo_y()
    car_label.place(x=x, y=y-20)

def move_down(event):
    x = car_label.winfo_x()
    y = car_label.winfo_y()
    car_label.place(x=x, y=y+20)

def move_left(event):
    x = car_label.winfo_x()
    y = car_label.winfo_y()
    car_label.place(x=x-20, y=y)

def move_right(event):
    x = car_label.winfo_x()
    y = car_label.winfo_y()
    car_label.place(x=x+20, y=y)

window = Tk()
window.title("Car Motion Example")
window.geometry("500x500")

window.bind("w", move_up)
window.bind("s", move_down)
window.bind("a", move_left)
window.bind("d", move_right)

car_image = PhotoImage(file=os.path.join("data", "car.png"))
car_image = car_image.subsample(3, 3)  

car_label = Label(window, image=car_image)
car_label.place(x=0, y=0)

window.mainloop()