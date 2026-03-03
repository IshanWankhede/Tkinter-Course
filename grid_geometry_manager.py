from tkinter import *

# example illustrating the grid geometry manager in Tkinter

window = Tk()
window.title("Grid Geometry Manager Example")
window.geometry("300x200")

# create some labels and entry widgets positioned using grid
Label(window, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
Entry(window).grid(row=0, column=1, padx=5, pady=5)

Label(window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")   # sticky="e" aligns the label to the right (east) within its grid cell 
Entry(window).grid(row=1, column=1, padx=5, pady=5)

Label(window, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
Entry(window).grid(row=2, column=1, padx=5, pady=5)

# use a button that spans two columns
Button(window, text="Submit").grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
