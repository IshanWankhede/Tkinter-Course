from tkinter import *

window = Tk()

menubar = Menu(window)  # create a menu bar
window.config(menu=menubar) # add the menu bar to the window

filemenu = Menu(menubar, tearoff=0, font = ("MV Boil", 15)) # create a "File" menu and add it to the menu bar
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=lambda: print("Open clicked")) # add a "Open" command to the "File" menu
filemenu.add_command(label="Save", command=lambda: print("Save clicked")) # add a "Save" command to the "File" menu
filemenu.add_separator() # add a separator line to the "File" menu
filemenu.add_command(label="Exit", command=window.quit) # add an "Exit" command to the "File" menu that closes the window when clicked

editmenu = Menu(menubar, tearoff=0, font = ("MV Boil", 15)) # create an "Edit" menu and add it to the menu bar
menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Cut", command=lambda: print("Cut clicked")) # add a "Cut" command to the "Edit" menu
editmenu.add_command(label="Copy", command=lambda: print("Copy clicked")) # add a
    
viewmenu = Menu(menubar, tearoff=0, font = ("MV Boil", 15)) # create a "View" menu and add it to the menu bar
menubar.add_cascade(label="View", menu=viewmenu)

viewmenu.add_command(label="Zoom In", command=lambda: print("Zoom In clicked")) # add a "Zoom In" command to the "View" menu
viewmenu.add_command(label="Zoom Out", command=lambda: print("Zoom Out clicked")) # add a "Zoom Out" command to the "View" menu 

window.mainloop()