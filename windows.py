from tkinter import *

import os 

# winows = serves as a container for all the widgets in the application
# widgets = buttons, text, labels, etc

windows = Tk() # creates a window object and assigns it to the variable "windows"

windows.title("My First GUI") # sets the title of the window

windows.geometry("400x300") # width x height

icon = PhotoImage(file=os.path.join("data", "logo.png")) # creates a PhotoImage object from the specified file path
windows.iconphoto(True, icon) # sets the window's icon to the PhotoImage object

windows.config(bg="#000000") # sets the background color of the window

windows.mainloop() # keeps the window open until we close it

