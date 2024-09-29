from turtle import Screen
from player import Player
from cars import CarManager
import time

scr = Screen()
scr.bgcolor('white')
scr.setup(height = 600,width = 600)
scr.tracer(0)

ttl = Player()
ttl.setheading(90)
game_is_on=True

scr.listen()
scr.onkey(fun = ttl.move,key ='Up')
while game_is_on:
    time.sleep(0.1)
    scr.update()
    c = CarManager()

scr.exitonclick()
