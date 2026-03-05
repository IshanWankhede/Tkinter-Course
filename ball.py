class Ball:
    def __init__(self,canvas,x,y,diamerter,x_speed,y_speed,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diamerter,diamerter,fill=color)
        self.x = x
        self.y = y
        self.diameter = diamerter
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.color = color

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if coordinates[0] < 0 or coordinates[2] >= self.canvas.winfo_width():
            self.x_speed = -self.x_speed

        if coordinates[1] < 0 or coordinates[3] >= self.canvas.winfo_height():
            self.y_speed = -self.y_speed

        self.canvas.move(self.image,self.x_speed,self.y_speed)