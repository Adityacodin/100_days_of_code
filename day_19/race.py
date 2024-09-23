from turtle import Turtle,Screen
from random import randint
colors = ['red','green','blue','black','orange','purple','pink']
def initialise_turtles():
    ttl_ls = []
    for i in range(7):
        ttl_ls.append(Turtle())
        ttl_ls[i].shape('turtle')
        ttl_ls[i].color(colors[i])
        ttl_ls[i].penup()
    return ttl_ls

def position_turtles(ttls):
    yc = 125
    for ttl in ttls:
        ttl.goto(x = -230,y = yc)
        yc -= 40

is_race_on = False
scr = Screen()
scr.setup(width = 500, height = 400)
bet = scr.textinput("Place a bet", "Which color will win the race: ")
if bet:
    is_race_on = True
ttls = initialise_turtles()
position_turtles(ttls)
while is_race_on:
    for ttl in ttls:
        ttl.forward(randint(0,10))
        if ttl.xcor() >= 230:
            is_race_on = False
            winner = ttl.pencolor()

if bet == winner:
    print(f"{bet.capitalize()} turtle won the race,You won.")
else:
    print(f"{winner.capitalize()} turtle won the race,You lose.")
    




scr.exitonclick()