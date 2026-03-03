from tkinter import *

# simple canvas example demonstrating how to draw shapes

window = Tk()
window.title("Canvas Drawing Example")
window.geometry("400x300")

# create a canvas widget
canvas = Canvas(window, width=400, height=300, bg="white")
canvas.pack()

# draw a rectangle
canvas.create_rectangle(50, 50, 150, 100, fill="blue", outline="black", width=2)
# syntax for create_rectangle: (x1, y1, x2, y2) where (x1, y1) is the top-left corner and (x2, y2) is the bottom-right corner of the rectangle

# draw a circle (oval with equal width and height)
canvas.create_oval(200, 50, 300, 150, fill="red", outline="black", width=2)
# syntax for create_oval: (x1, y1, x2, y2) where (x1, y1) is the top-left corner of the bounding box and (x2, y2) is the bottom-right corner of the bounding box. To draw a circle, make sure the width and height of the bounding box are equal.

# draw a line
canvas.create_line(50, 200, 350, 200, fill="green", width=3)
# syntax for create_line: (x1, y1, x2, y2) where (x1, y1) is the starting point and (x2, y2) is the ending point of the line. You can also specify multiple points to create a polyline by providing more coordinates.

# draw an arc
canvas.create_arc(50, 150, 150, 250, start=0, extent=70, fill="yellow", outline="black", width=2)
# syntax for create_arc: (x1, y1, x2, y2) where (x1, y1) is the top-left corner of the bounding box and (x2, y2) is the bottom-right corner of the bounding box. The start and extent parameters define the starting angle and extent of the arc in degrees.

# draw text
canvas.create_text(200, 250, text="Canvas Drawing", font=("Arial", 16), fill="black")
# syntax for create_text: (x, y) where (x, y) is the position of the text. You can specify the font and fill color as well.

window.mainloop()
