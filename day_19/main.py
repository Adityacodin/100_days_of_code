#turtle graphics,event listeners,state and multiple intances,higher order functions
from turtle import Turtle,Screen    
ttl = Turtle()
scr = Screen()

def move_forward():
    ttl.forward(10)

def move_backward():
    ttl.back(10)

def move_cclk():
    ttl.setheading(ttl.heading()+10)

def move_clk():
    ttl.setheading(ttl.heading()-10)

def clear():
    # ttl.reset()    
    ttl.clear()
    ttl.penup()
    ttl.home()
    ttl.pendown()

scr.listen()
scr.onkey(fun = move_forward,key = 'w')
scr.onkey(fun = move_cclk,key = 'a')
scr.onkey(fun = move_backward,key = 's')
scr.onkey(fun = move_clk,key = 'd')
scr.onkey(fun = clear,key = 'c')

scr.exitonclick()
