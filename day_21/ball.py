from turtle import Turtle
TOP = 290
BOTTOM = -280


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('white')
        self.x = 10
        self.y = 10

    def tilt(self,t):
        self.setheading(self.heading()+t)

    def bounce(self):
        if self.ycor() >= TOP:
            self.tilt(-45)
        self.forward(10)        
        