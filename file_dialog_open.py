from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()
window.title("My First GUI")

button = Button(window, text="Open File", command=openfile) # creates a Button widget that opens a file dialog when clicked
button.pack() # adds the Button widget to the window and centers it

window.mainloop()