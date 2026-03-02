from tkinter import *
import os

def submit():

    languages = [] # retrieves the currently selected items in the Listbox widget and stores them in a list

    for i in listbox.curselection():
        languages.append(listbox.get(i))

    print("You Want to Learn: ")
    # print(listbox.get(listbox.curselection())) # retrieves the currently selected item in the Listbox widget and prints it to the console
    
    for i in languages:
        print(i) # prints each selected item in the Listbox widget to the console

def add():
    if entryBox.get() != "": # checks if the text entered in the Entry widget is not empty
        listbox.insert(listbox.size() + 1, entryBox.get()) # adds the text entered in the Entry widget to the end of the Listbox widget
        listbox.config(height=listbox.size())
        entryBox.delete(0, END) # deletes the text in the Entry widget after adding it to the Listbox widget

def delete():
    for i in reversed(listbox.curselection()): # iterates through the selected items in the Listbox widget in reverse order (to avoid index shifting issues when deleting items)
        listbox.delete(i) # deletes each selected item in the Listbox widget

    # listbox.delete(listbox.curselection()) # deletes the currently selected item in the Listbox widget
    listbox.config(height=listbox.size())

window = Tk()
window.title("My First GUI")

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("constantia", 35),
                  width=12,
                #   selectmode=SINGLE, # allows only one item to be selected at a time in the Listbox widget
                    selectmode=MULTIPLE, # allows multiple items to be selected at the same time in the Listbox widget
                  )
listbox.pack()

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "JavaScript")
listbox.insert(5, "Ruby")
listbox.insert(6, "Swift")

listbox.config(height=listbox.size()) # sets the height of the Listbox widget to the number of items in the list, ensuring that all items are visible without scrolling

entryBox = Entry(window)
entryBox.pack()

submit_button = Button(window, text="Submit",
                       font=("Arial", 16),  
                        fg="#FFFFFF",
                        bg="#0B5403",
                        activeforeground="#FFFFFF",
                        activebackground="#033C10",
                        relief=RAISED,
                        bd=5,
                        padx=10,
                        pady=10,
                        command=submit) 
submit_button.pack() 

add_button = Button(window, text="Add",
                       font=("Arial", 16),  
                        fg="#FFFFFF",
                        bg="#033E54",
                        activeforeground="#FFFFFF",
                        activebackground="#031E3C",
                        relief=RAISED,
                        bd=5,
                        padx=10,
                        pady=10,
                        command=add) # creates a Button widget that adds the text entered in the Entry widget to the end of the Listbox when clicked
add_button.pack()

delete_button = Button(window, text="Delete",
                       font=("Arial", 16),
                        fg="#FFFFFF",
                        bg="#540403",
                        activeforeground="#FFFFFF",
                        activebackground="#3C0303",
                        relief=RAISED,
                        bd=5,
                        padx=10,
                        pady=10,
                        command=delete) # creates a Button widget that deletes the currently selected item in the Listbox when clicked
delete_button.pack()

window.mainloop()