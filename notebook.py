from tkinter import *
from tkinter import ttk

# simple example of creating a notebook (tabbed interface) with two tabs

window = Tk()
window.title("Notebook Example")
window.geometry("400x300")

notebook = ttk.Notebook(window)  
notebook.pack(fill="both", expand=True)   # make the notebook fill the entire window and expand when resized    

# create frames for each tab
frame1 = Frame(notebook) # create a frame for the first tab
frame2 = Frame(notebook)

notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")

# populate tab 1
label1 = Label(frame1, text="This is the content of tab 1")
label1.pack(padx=10, pady=10)

# populate tab 2
label2 = Label(frame2, text="This is the content of tab 2")
label2.pack(padx=10, pady=10)

window.mainloop()
