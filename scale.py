from tkinter import *
import os

def submit():
    print(f"Temperature is {str(scale.get())} degree C") # retrieves the current value of the Scale widget and prints it to the console

window = Tk()
window.title("My First GUI")
window.geometry("250x790")

fire = PhotoImage(file=os.path.join("data", "fire.png"))
fire = fire.subsample(6, 6) # resizes the image by subsampling
fire_label = Label(window, image=fire)
fire_label.pack()


scale = Scale(window, 
              from_ = 100, 
              to = 0,
              length = 600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,  # adds tick marks to the Scale widget at intervals of 10
            #   showvalue= 0, # hides the current value of the Scale widget (set to 1 to show the value)
              resolution=0.5, # sets the increment for the Scale widget to 0.5 (allows for more precise adjustments)
              troughcolor="#BC691A", # sets the color of the trough (the area where the slider moves) of the Scale widget
              fg="#FF1C00", # sets the color of the text and tick marks on the Scale widget
              bg="#000000", # sets the background color of the Scale widget
              ) # creates a Scale widget with the specified properties

scale.set((scale['from'] + scale['to']) / 2) # sets the initial value of the Scale widget to the midpoint between the from and to values
scale.pack()

ice = PhotoImage(file=os.path.join("data", "ice.png"))
ice = ice.subsample(6, 6) # resizes the image by subsampling
ice_label = Label(window, image=ice)
ice_label.pack() # adds the ice image to the bottom of the window

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
