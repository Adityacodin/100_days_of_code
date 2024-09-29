from turtle import Turtle
TOP = 290
BOTTOM = -280


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('white')
        self.move_speed = 0.1
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(self.xcor()+self.x,self.ycor()+self.y)

    def bounce_y(self):
        self.y *= -1
    
    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9
    
    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1