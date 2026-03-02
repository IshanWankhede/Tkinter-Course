from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor(title="Choose a color") # opens a color chooser dialog and returns the selected color as a tuple of RGB values and a hexadecimal string
    print(color) # prints the selected color to the console\
    colorhex = color[1] # retrieves the hexadecimal string representation of the selected color from the tuple
    print(colorhex) # prints the hexadecimal string representation of the selected color to the console
    window.config(bg=colorhex) # changes the background color of the window to the selected color using the hexadecimal string representation

window = Tk()

window.title("My First GUI")
window.geometry("400x300")

button = Button(window, text="Choose Color",
                command=click) # creates a Button widget
button.pack() # adds the Button widget to the window and centers it

window.mainloop()