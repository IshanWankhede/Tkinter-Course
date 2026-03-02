from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes = [
                                        ("Text files", "*.txt"),
                                        ("HTML files", "*.html"),
                                        ("All files", "*.*")     
                                    ])
    if file is None:
        return    # user cancelled save dialog
    filetext = str(text.get(1.0, END))  # get text from text box (1.0 means line 1, character 0)
    file.write(filetext)  # write text to file
    file.close()

window = Tk()
window.geometry("400x400")

button = Button(window, text="Save File", command=savefile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()