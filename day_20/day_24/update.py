
class HighscoreManager():
    def __init__(self):
        with open('C:/Users/33333333333333333333/100_days_ofcode/day_24/highscore.txt',mode='r') as self.file:
            self.old_score = int(self.file.read().split(' ')[-1])

    def update_highscore(self,new_score):
        if new_score>self.old_score:
            with open('C:/Users/33333333333333333333/100_days_ofcode/day_24/highscore.txt',mode='w') as self.file:
                self.file.write(f'highscore = {new_score}')

    def get_highscore(self):
        return self.old_score

