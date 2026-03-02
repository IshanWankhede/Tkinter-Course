# frame = a rectanguar area on a screen. like a window in a house

from tkinter import *

window = Tk()
window.title("Frames")

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.pack()

Button(frame, text="W", font = ("Consolas", 24), bg="black", fg="white", width=3).pack(side=TOP)
Button(frame, text="A", font = ("Consolas", 24), bg="black", fg="white", width=3).pack(side=LEFT)
Button(frame, text="S", font = ("Consolas", 24), bg="black", fg="white", width=3).pack(side=LEFT)
Button(frame, text="D", font = ("Consolas", 24), bg="black", fg="white", width=3).pack(side=LEFT)


window.mainloop()