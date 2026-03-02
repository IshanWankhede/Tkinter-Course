from tkinter import *
import os

window = Tk()

window.title("My First GUI")

window.geometry("400x300")

window.config(bg="#000000")

icon = PhotoImage(file=os.path.join("data", "logo.png"))

icon = icon.subsample(7, 7) # resizes the image by subsampling it (reducing its size by a factor of 2 in both dimensions)

label = Label(window, text="Hello World!", 
              font=("Arial", 20),
              fg="#FFFFFF", 
              bg="#231818",
              relief=RAISED, # sets the border style of the Label widget to "raised"
              bd=5,
              padx=10,
              pady=10,
              image = icon,
              compound='bottom') # creates a Label widget with the specified text, font, foreground color, background color, and image
label.pack() # adds the Label widget to the window and centers it

label2 = Label(window, text="Welcome to Python GUI programming!")
label2.pack() # adds the second Label widget to the window and centers it

# label.config(text="Hello Python!") # updates the text of the first Label widget 
# label.place(x=50, y=50) # positions the first Label widget at the specified coordinates (x=50, y=50)

window.mainloop()
