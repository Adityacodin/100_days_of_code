from turtle import Turtle,Screen
import random as rd

colors = ['CornFlowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray','SeaGreen']
def draw_shape(ttl,n_of_sides):
    angle = 360/n_of_sides
    # ttl.color(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
    ttl.color(rd.choice(colors))
    for _ in range(n_of_sides):
        ttl.forward(100)
        ttl.left(angle)

def random_colors():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    return (r,g,b)

def random_walk(ttl):
    pos = [0,90,180,270]
    num = 200
    while num:
        if rd.randint(1, 100)%2 == 0:
            ttl.left(rd.choice(pos))
        else:
            ttl.right(rd.choice(pos))
        # ttl.color(rd.choice(colors))
        r = random_colors()
        ttl.color(r)
        ttl.forward(30)
        num-=1

def spirograph(ttl,gap):
    for _ in range(360//gap):
        ttl.color(random_colors())
        ttl.circle(100)
        ttl.setheading(ttl.heading()+gap)

def draw_dashedline(ttl,distance):
    for _ in range(distance):
        ttl.forward(10)
        ttl.penup()
        ttl.forward(10)
        ttl.pendown()


timmy = Turtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)
spirograph(timmy,5)
screen.exitonclick() 

