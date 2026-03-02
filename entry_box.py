from tkinter import *
import os

def submit():
    text = entry.get() # retrieves the text entered in the Entry widget
    print(f"You entered: {text}") # prints the retrieved text to the console

def delete():
    entry.delete(0, END) # deletes the text in the Entry widget from index 0 to the end

def back_spc():
    current_text = entry.get() # retrieves the current text in the Entry widget
    new_text = current_text[:-1] # removes the last character from the retrieved text
    print(f"Current text: {current_text}, New text: {new_text}") # prints the current and new text to the console for debugging
    entry.delete(0, END) # deletes the current text in the Entry widget
    entry.insert(0, new_text) # inserts the new text (without the last character) back into the Entry widget at index 0

window = Tk()
window.title("My First GUI")
window.geometry("400x300")

entry = Entry(window, font=("Arial", 50), 
              fg="#FFFFFF", 
              bg="#000000", 
              insertbackground="#FFFFFF", # sets the color of the cursor in the Entry widget
            #   show="*", # hides the characters entered in the Entry widget (useful for password fields
              relief=RAISED, 
              bd=5, 
              width=20) 

entry.insert(0, "Enter text here") 
# creates an Entry widget with the specified font, foreground color, background color, and other properties

entry.pack(side = LEFT) # adds the Entry widget to the window and centers it with some vertical padding

submit_button = Button(window, text="Submit",
                       font=("Arial", 16),
                        fg="#FFFFFF",
                        bg="#4C0354",
                        activeforeground="#FF0000",
                        activebackground="#0000FF",
                        relief=RAISED,
                        bd=5,
                        padx=10,
                        pady=10,
                        command= submit ) # creates a Button widget that prints the text entered in the Entry widget when clicked

submit_button.pack(side = RIGHT) # adds the Button widget to the window and centers it

delete_button = Button(window, text="Delete",
                       font=("Arial", 16),  
                        fg="#FFFFFF",
                        bg="#4C0354",
                        activeforeground="#FF0000",
                        activebackground="#0000FF",
                        relief=RAISED,
                        bd=5,
                        padx=10,
                        pady=10,
                        command= delete) # creates a Button widget that deletes the text entered in the Entry widget when clicked

delete_button.pack(side = RIGHT) # adds the Button widget to the window and centers it

back_button = Button(window, text="Back",
                       font=("Arial", 16),
                        fg="#FFFFFF",
                        bg="#4C0354",
                        activeforeground="#FF0000",
                        activebackground="#0000FF",
                        relief=RAISED,
                        bd=5,
                        padx=10,
                        pady=10,
                        command= back_spc) # creates a Button widget that deletes the last character entered in the Entry widget when clicked

back_button.pack(side = RIGHT) # adds the Button widget to the window and centers it

window.mainloop()
