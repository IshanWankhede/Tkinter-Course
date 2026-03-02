# text_widget = widget that allows the user to enter multiple lines of text

from tkinter import *

def submit():
    input = text.get("1.0", END) # retrieves the text entered in the Text widget from the first character (line 1, character 0) to the end of the text and stores it in the variable "input"
    print(input) # prints the retrieved text to the console

window = Tk()
window.title("My First GUI")

text = Text(window,
            bg ="light yellow",
            fg = "purple",
            font = ("Ink Free", 24),
            height = 8,
            width=20,
            padx=20,
            pady=20)

text.pack() # adds the Text widget to the window and centers it

button = Button(window, text="Submit", command=submit)
button.pack() # adds the Button widget to the window and centers it

window.mainloop()