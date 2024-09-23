from turtle import Screen,Turtle

def create_snake():
    s = []
    for i in range(0,3):
        s.append(Turtle())
        s[i].penup()
        s[i].color('white','black')
        s[i].shape('square')
        x = int(s[i].xcor()) - ((i+1)*20)
        s[i].goto(x=x, y = 0)
    return s

scr = Screen()
scr.setup(width=600,height = 600)
scr.bgcolor('black')
scr.title('Snake Slither')
snk = create_snake()

scr.exitonclick()