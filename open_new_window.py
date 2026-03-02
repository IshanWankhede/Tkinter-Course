import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    
    label = tk.Label(new_window, text="Hello from New Window!")
    label.pack(pady=20)
    
    close_btn = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_btn.pack()

# Main window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

label = tk.Label(root, text="This is the Main Window")
label.pack(pady=20)

open_btn = tk.Button(root, text="Open New Window", command=open_new_window)
open_btn.pack()

root.mainloop()