from tkinter import *

# draw a pokemon ball using canvas

window = Tk()
window.title("Pokemon Ball")
window.geometry("300x300")

# create canvas
canvas = Canvas(window, width=300, height=300, bg="lightgray")
canvas.pack()

# draw the pokemon ball
center_x, center_y = 150, 150
radius = 80

# top half (red)
canvas.create_arc(center_x - radius, center_y - radius, 
                  center_x + radius, center_y + radius,
                  start=0, extent=180, fill="red", outline="black", width=3)

# bottom half (white)
canvas.create_arc(center_x - radius, center_y - radius,
                  center_x + radius, center_y + radius,
                  start=180, extent=180, fill="white", outline="black", width=3)

# middle line
canvas.create_line(center_x - radius, center_y, center_x + radius, center_y, 
                   fill="black", width=3)

# center circle (black)
circle_radius = 15
canvas.create_oval(center_x - circle_radius, center_y - circle_radius,
                   center_x + circle_radius, center_y + circle_radius,
                   fill="black", outline="black", width=2)

# center circle (white dot)
dot_radius = 6
canvas.create_oval(center_x - dot_radius, center_y - dot_radius,
                   center_x + dot_radius, center_y + dot_radius,
                   fill="white", outline="white")

window.mainloop()
