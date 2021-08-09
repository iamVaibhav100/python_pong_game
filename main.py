from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('The Pong')
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detecting Collisions with Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detecting Collisions with the Paddles
    if r_paddle.distance(ball) < 50 and ball.xcor() > 340 or l_paddle.distance(ball) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()
        ball.increase_speed()

    # When r_paddle misses
    if ball.xcor() > 380 and ball.distance(r_paddle) > 50:
        ball.goto(0, 0)
        ball.paddle_bounce()
        score.l_score_update()

    # When l_paddle misses
    if ball.xcor() < -380 and ball.distance(l_paddle) > 50:
        ball.goto(0, 0)
        ball.paddle_bounce()
        score.r_score_update()

screen.exitonclick()
