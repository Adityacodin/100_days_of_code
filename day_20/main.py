from turtle import Screen,write
from snake import Snake
from food import Food
from scoreboard import Score
import time
            
scr = Screen()
scr.setup(width=600,height = 600)
scr.bgcolor('black')
scr.title('Snake Slither')
scr.tracer(0)

snake = Snake()
food = Food()
sc = Score()
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")

game_is_on  = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        sc.increase_score()
        scr.update()
        snake.add_seg(snake.snk[-1].position())
    # detect collision with the wall
    if (snake.head.xcor() >= 290 or snake.head.xcor() <= -290) or (snake.head.ycor() >= 290 or snake.head.ycor() <= -290) :
        snake.reset()
        sc.reset()
    # detect collision with the tail
    # if the head collides with any segment in the tail, we can trigger this function
    for seg in snake.snk[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset()
            sc.reset()


scr.exitonclick()