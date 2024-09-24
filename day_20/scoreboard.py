from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color('white')
        self.refresh()

    def refresh(self):
        self.score+=1
        self.goto((-1,270))
        self.clear()
        self.write(f"Score : {self.score}",False, font=('Arial', 12, 'normal'))
        
    def game_over(self):
        self.home()
        self.write(f"GAME OVER",False,font=('Arial', 12, 'normal'))