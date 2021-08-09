from turtle import Turtle

PADDLE_MOVE = 20


class Paddle(Turtle):
    """docstring for Paddle"""

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        y = self.ycor() + PADDLE_MOVE
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - PADDLE_MOVE
        self.goto(self.xcor(), y)
