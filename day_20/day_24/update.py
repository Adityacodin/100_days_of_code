
class HighscoreManager():
    def __init__(self):
        with open('day_20/day_24/highscore.txt',mode='r') as self.file:
            self.old_score = int(self.file.read().split(' ')[-1])

    def update_highscore(self,new_score):
        if new_score>self.old_score:
            with open('day_20/day_24/highscore.txt',mode='w') as self.file:
                self.file.write(f'highscore = {new_score}')

    def get_highscore(self):
        return self.old_score

