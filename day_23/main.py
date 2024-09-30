from turtle import Screen
from player import Player
from cars import CarManager
from game_msg import GameMsg
import time

scr = Screen()
car_manager = CarManager()
in_game_msgs = GameMsg()
scr.bgcolor('white')
scr.setup(height = 600,width = 600)
scr.tracer(0)

player = Player()
game_is_on=True
in_game_msgs.level_msg()
scr.listen()
scr.onkey(fun = player.move,key ='Up')
i = 0
car_list = []
while game_is_on:
    time.sleep(0.1)
    scr.update()
    car_manager.create_cars()
    car_manager.move_cars()
    
    # detect collision
    for car in car_manager.all_cars:
        if car.xcor() >= player.xcor()-10:  #check collision with cars only on the left side
            if car.distance(player) < 20 and car.ycor() :
                in_game_msgs.game_over_msg()
                game_is_on = False
    # detect successful crossing
    if player.is_at_finish_line():
        in_game_msgs.level_msg()
        player.go_to_start()
        car_manager.increase_speed()


scr.exitonclick()
