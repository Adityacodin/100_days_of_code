from turtle import Turtle
from random import randint,choice
COLORS  = ['red','yellow','green','blue','orange','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def  __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_wid = 1,stretch_len = 3)
        self.goto((280,randint(-200,200)))
       
