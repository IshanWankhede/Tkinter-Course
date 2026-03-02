from tkinter import *
import os

def display():
    if x.get() == 1: # checks if the first checkbox is selected (value of 1)
        print("Option 1 selected") # prints a message to the console if the first checkbox is selected
    else:
        print("Option 1 deselected") # prints a message to the console if the first checkbox is deselected

window = Tk()

window.title("My First GUI")
window.geometry("400x300")

x = IntVar() # creates an IntVar to hold the state of the first checkbox

checkbox1 = Checkbutton(window, text="Option 1", 
                        variable=x, # associates the Checkbutton widget with the IntVar to track its state
                        onvalue=1, # sets the value of the IntVar to 1 when the checkbox is selected
                        offvalue=0, # sets the value of the IntVar to 0 when the checkbox is deselected
                        command= display,
                        font=("Arial", 16), 
                        fg="#FFFFFF", 
                        bg="#4C0354",
                        activeforeground="#FF0000",  # sets the foreground color of the Checkbutton widget when it is active (clicked)
                        activebackground="#0000FF",
                        relief=RAISED,
                        bd=5,
                        padx=10,
                        pady=10) # creates a Checkbutton widget with the specified properties and associates it with the IntVar

checkbox1.pack(side = LEFT) # adds the Checkbutton widget to the window and centers it

window.mainloop() 