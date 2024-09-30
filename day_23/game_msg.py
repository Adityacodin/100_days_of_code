from turtle import Turtle


class GameMsg(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = -1

    def upd_scr(self):
        self.clear()
        self.level+=1
        
    def level_msg(self):
        self.goto(-230,250)
        self.upd_scr()
        self.write(f'Level : {self.level}',align = 'left',font=('Arial', 12
        , 'normal'))

    def game_over_msg(self):
        self.home()
        self.write(f'Game Over',align = 'center',font=('Arial', 12
        , 'normal'))