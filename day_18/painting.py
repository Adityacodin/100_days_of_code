from turtle import Turtle,Screen
import random as rd

colors = [(238, 248, 243), (251, 242, 246), (226, 237,
246), (30, 106, 145), (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77), (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124), (235, 211,
85), (6, 103, 66), (145, 185, 167), (216, 209, 11), (3, 69, 136), (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83),
(53, 60, 15), (223, 170, 191), (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25), (165, 207, 191), (147, 210, 222),
(97, 128, 164), (170, 192, 218), (81, 32, 74)]

ttl = Turtle()
scr = Screen()
scr.colormode(255)
ttl.penup()
ttl.goto(-200,-200)
ttl.hideturtle()

for i in range(10):
    for _ in range(10):
        ttl.pendown()
        ttl.dot(20,rd.choice(colors))
        ttl.penup()
        if _ != 9:
            ttl.forward(50)
    if i%2==0:
            ttl.left(90)
            ttl.forward(50)
            ttl.left(90)
    else:
            ttl.right(90)
            ttl.forward(50)
            ttl.right(90)




scr.exitonclick()