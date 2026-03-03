from tkinter import *

# example demonstrating key events in Tkinter

window = Tk()
window.title("Key Events Example")
window.geometry("400x300")

# label to display key info
label = Label(window, text="Press any key...", font=("Arial", 14))
label.pack(pady=20)

# text widget to show all keys pressed
text_box = Text(window, height=10, width=50)
text_box.pack(padx=10, pady=10)

# function to handle key press events
def on_key_press(event):
    # event.char gives the character pressed
    # event.keysym gives the symbolic name of the key
    # event.keycode gives the numeric code of the key
    
    key_info = f"Key pressed: {event.char} | Keysym: {event.keysym} | Keycode: {event.keycode}\n"
    text_box.insert(END, key_info)
    
    # update label
    label.config(text=f"Key: {event.keysym}")

# function to handle key release events
def on_key_release(event):
    key_info = f"Key released: {event.keysym}\n"
    text_box.insert(END, key_info)

# bind key press and release events to the window
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

# bind specific keys
window.bind("<Return>", lambda e: text_box.insert(END, "--- ENTER pressed ---\n"))
window.bind("<Escape>", lambda e: window.quit())

window.mainloop()
