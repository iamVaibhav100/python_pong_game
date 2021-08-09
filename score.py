from turtle import Turtle


class Score(Turtle):
    """docstring for Score"""

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=('Courier', 40, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, font=('Courier', 40, 'normal'))

    def r_score_update(self):
        self.r_score += 1
        self.write_score()

    def l_score_update(self):
        self.l_score += 1
        self.write_score()
