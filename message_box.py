from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="This is an info message", message="You clicked the button!") # displays an informational message box with the specified title and message
    # while True:
    #     messagebox.showwarning(title="Warning", message="Virus Downloading.....") # displays a warning message box with the specified title and message
    # messagebox.showerror(title="Error", message="An error occurred!") # displays an error message box with the specified title and message
    # if messagebox.askokcancel(title="Ask ok cancel", message="Do you want to continue?"): # displays a question message box with the specified title and message and returns the user's response as "yes" or "no"
    #     print("You clicked OK!") # prints a message to the console if the user clicks "OK"
    # else:
    #     print("You clicked Cancel!") # prints a message to the console if the user clicks "Cancel"

    # if messagebox.askretrycancel(title="Ask retry cancel", message="An error occurred. Do you want to retry?"): # displays a question message box with the specified title and message and returns the user's response as "yes" or "no"
    #     print("You clicked Retry!") # prints a message to the console if the user clicks "Retry"    
    # else:
    #     print("You clicked Cancel!") # prints a message to the console if the user clicks "Cancel"

    #  if messagebox.askyesno(title="Ask yes no", message="Do you like Python?"): # displays a question message box with the specified title and message and returns the user's response as "yes" or "no"
    #     print("You clicked Yes!") # prints a message to the console if the user clicks "Yes"
    #  else:
    #     print("You clicked No!") # prints a message to the console if the user clicks "No"
        
        # messagebox.askquestion(title="Ask question", message="Do you like Python?") # displays a question message box with the specified title and message and returns the user's response as "yes" or "no" 

    

window = Tk()
window.title("My First GUI")

button = Button(window, text="Click Me!",
                command=click)

button.pack() # adds the Button widget to the window and centers it

window.mainloop()
