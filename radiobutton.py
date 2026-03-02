from tkinter import *
import os

# radiobutton = widget that allows the user to select one option from a set of options

food = [" 🍕 Pizza", " 🍔 Burger", " 🌭 Hotdog"]

def order():
    print(f"You ordered {food[x.get()]}") # retrieves the selected food item based on the value of the IntVar and prints it to the console      

window = Tk()
window.title("My First GUI")
window.geometry("400x300")
window.config(bg="#000000")

pizaza = PhotoImage(file=os.path.join("data", "pizza.png"))
pizaza = pizaza.subsample(7, 7) # resizes the image
burgger = PhotoImage(file=os.path.join("data", "burger.png"))
burgger = burgger.subsample(7, 7) # resizes the image
hotdog = PhotoImage(file=os.path.join("data", "hotdog.png"))
hotdog = hotdog.subsample(7, 7) # resizes the image

food_images = [pizaza, burgger, hotdog] # creates a list of the food images

x = IntVar() # creates an IntVar to hold the state of the selected Radiobutton

for index in range(len(food)):
    radiobutton = Radiobutton(window, text=food[index], 
                              value=index, # sets the value of the Radiobutton widget to the index of the food item
                              variable=x, # associates the Radiobutton widget with the IntVar to track its state
                              font=("Arial", 16), 
                              fg="#FFFFFF", 
                              bg="#544A03",
                              activeforeground="#FF0000",  # sets the foreground color of the Radiobutton widget when it is active (clicked)
                              activebackground="#0000FF",
                              relief=RAISED,
                              bd=5,
                              padx=10,
                              pady=10,
                              command=order,
                              image=food_images[index],
                              compound=LEFT) # creates a Radiobutton widget with the specified properties and associates it with the IntVar
    


    radiobutton.pack(anchor=W) # adds the Radiobutton widget to the window and aligns it to the left (west) side of the window
window.mainloop()