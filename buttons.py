from tkinter import *
import os

# button = widget that can be clicked to perform an action
count = 0

def click():
    global count
    count += 1
    print(f"Button clicked {count} times!")


window = Tk()
window.title("My First GUI")
window.geometry("400x300")
icon = PhotoImage(file=os.path.join("data", "logo.png"))
icon = icon.subsample(7, 7) # resizes the image by subsampling

button = Button(window, text="Click Me!",
                command=click, # sets the function to be called when the button is clicked
                font=("Arial", 16),
                fg="#FFFFFF",
                bg="#231818",
                activeforeground="#FF0000",
                activebackground="#0000FF",
                relief=RAISED,
                bd=5,               
                padx=10,
                pady=10,
                image=icon,
                compound='left') # creates a Button widget with the specified text, font, foreground color, background color, and image
button.pack() # adds the Button widget to the window and centers it

window.mainloop()
