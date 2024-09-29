from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

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
scr_bd = Scoreboard()
# moving the paddles
scr.listen()
scr.onkey(fun = r_padl.move_up,key = 'w')
scr.onkey(fun = r_padl.move_down,key = 's')
scr.onkey(fun = l_padl.move_up,key = 'Up')
scr.onkey(fun = l_padl.move_down,key = 'Down')
while game_is_on:
    sleep(ball.move_speed)
    scr.update()
    ball.move()

    if ball.ycor()>=TOP or ball.ycor()<=BTM:
        ball.bounce_y()

    if (ball.distance(l_padl)<60 and ball.xcor()>320) or (ball.distance(r_padl)<60 and ball.xcor()<-320):
        ball.bounce_x()

    if ball.xcor()>400:
        # l_padl wins
        scr_bd.l_point()
        ball.reset_pos()
    elif ball.xcor()<-400:
        # r_padl wins
        scr_bd.r_point()
        ball.reset_pos()

        
scr.exitonclick()
