from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP,DOWN,LEFT,RIGHT = 90,270,180,0
class Snake():

    def __init__(self):
        self.snk = []
        self.create_snake()
        self.head = self.snk[0]
        
    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_seg(pos)
                
    def add_seg(self,pos):
        new_seg = Turtle("square")
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(pos)
        self.snk.append(new_seg)

    def move(self):
        for s_num in range(len(self.snk)-1,0,-1):
            new_x = self.snk[s_num-1].xcor()
            new_y = self.snk[s_num-1].ycor()
            self.snk[s_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

