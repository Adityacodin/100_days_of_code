from turtle import Turtle
from random import randint,choice
COLORS  = ['red','yellow','green','blue','orange','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        self.all_cars =[]

    def create_cars(self):
        r_c = randint(1,6)
        if r_c == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid = 1,stretch_len = 2)
            new_car.goto((280,randint(-250,250)))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
       