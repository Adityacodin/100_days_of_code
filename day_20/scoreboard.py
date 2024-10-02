from turtle import Turtle
from day_24.update import HighscoreManager


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hs = HighscoreManager()
        self.score = -1
        self.high_score = self.hs.get_highscore()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto((-1,270))
        self.increase_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} | Highscore : {self.high_score}",False, font=('Arial', 12, 'normal'))
    
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.hs.update_highscore(self.high_score)
        self.score = 0
        self.update_scoreboard()
