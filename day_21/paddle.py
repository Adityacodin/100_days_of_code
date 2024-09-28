from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,initial_pos):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.goto(initial_pos)
        self.left(90)
        self.shapesize(stretch_wid=1,stretch_len = 5)

    def move_up(self):
        self.forward(20)
        

    def move_down(self):
        self.back(20)
        