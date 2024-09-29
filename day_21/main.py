from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from random import randint

TOP = 290
BTM  = -290

# create screen
scr = Screen()
scr.title('The Pong Game')
scr.setup(height = 600,width = 800)
scr.bgcolor('black')
game_is_on = True
# creating paddles
scr.tracer(0)
l_padl = Paddle(initial_pos = (350,0))
r_padl = Paddle(initial_pos = (-350,0))
ball = Ball()
ball.tilt(randint(0,90))
# moving the paddles
scr.listen()
scr.onkey(fun = r_padl.move_up,key = 'w')
scr.onkey(fun = r_padl.move_down,key = 's')
scr.onkey(fun = l_padl.move_up,key = 'Up')
scr.onkey(fun = l_padl.move_down,key = 'Down')
while game_is_on:
    sleep(0.1)
    scr.update()
    ball.move()

    if ball.ycor() >= TOP or ball.ycor()<= BTM:
        ball.bounce()
    if ball.distance(l_padl) <50 and ball.xcor()>340:
        ball.bounce()
    
scr.exitonclick()
