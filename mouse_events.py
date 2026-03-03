from tkinter import *

# function to handle mouse button click
def on_left_click(event):
    event_info = f"Left Click at ({event.x}, {event.y})\n"
    text_box.insert(END, event_info)

def on_right_click(event):
    event_info = f"Right Click at ({event.x}, {event.y})\n"
    text_box.insert(END, event_info)

# function to handle mouse motion
def on_mouse_move(event):
    label.config(text=f"Mouse Position: ({event.x}, {event.y})")

# function to handle mouse wheel (scroll)
def on_mouse_wheel(event):
    if event.num == 5 or event.delta < 0:
        event_info = f"Scroll Down at ({event.x}, {event.y})\n"
    else:
        event_info = f"Scroll Up at ({event.x}, {event.y})\n"
    text_box.insert(END, event_info)

# function for mouse enter
def on_enter(event):
    canvas.config(bg="lightgreen")
    text_box.insert(END, "Mouse Entered Canvas\n")

# function for mouse leave
def on_leave(event):
    canvas.config(bg="lightblue")
    text_box.insert(END, "Mouse Left Canvas\n")

window = Tk()
window.title("Mouse Events Example")
window.geometry("500x400")

# label to display mouse info
label = Label(window, text="Move your mouse or click...", font=("Arial", 12))
label.pack(pady=10)

# canvas to display a rectangle and log mouse events
canvas = Canvas(window, width=480, height=200, bg="lightblue", highlightthickness=2, highlightbackground="black")
canvas.pack(padx=10, pady=10)

# rectangle on canvas
rect = canvas.create_rectangle(100, 50, 400, 150, fill="yellow", outline="black", width=2)

# text widget to log events
text_box = Text(window, height=8, width=60)
text_box.pack(padx=10, pady=10)

# bind mouse events to canvas
canvas.bind("<Button-1>", on_left_click)
canvas.bind("<Button-3>", on_right_click)
canvas.bind("<Motion>", on_mouse_move)
canvas.bind("<MouseWheel>", on_mouse_wheel)
canvas.bind("<Enter>", on_enter)
canvas.bind("<Leave>", on_leave)

# clear button
Button(window, text="Clear Log", command=lambda: text_box.delete("1.0", END)).pack()

window.mainloop()
