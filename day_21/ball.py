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

    def move(self):
        self.forward(20)    

    def bounce(self):
        if self.heading() <= 45 :
            self.tilt(90)
        elif self.heading() > 45 :
            self.tilt(-90)
        elif self.heading() <= 135 :
            self.tilt(90)
        elif self.heading() > 135 :
            self.tilt(-90)
        elif self.heading() <= 225 :
            self.tilt(90)
        elif self.heading() > 225 :
            self.tilt(-90)
        elif self.heading() <= 315 :
            self.tilt(90)
        elif self.heading() > 315 :
            self.tilt(-90)        