from tkinter import *
from tkinter.ttk import *
import time

def start():
    task = 10
    x = 0
    while x < task:
        time.sleep(0.05)
        progress["value"] += 10
        x += 1
        percent.set(f"{(x/task)*100:.0f}%")
        window.update_idletasks()

window = Tk()
window.title("Progress Bar Example")
window.geometry("300x120")

percent = StringVar()

progress = Progressbar(window, orient="horizontal", length=250)
progress.pack()

percent_label = Label(window, textvariable=percent)
percent_label.pack()

button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()
