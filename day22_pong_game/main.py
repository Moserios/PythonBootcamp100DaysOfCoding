from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()


def turn_off():
    screen.bye()


screen.listen()
screen.onkey(r_paddle.right_puddle_up, "Up")
screen.onkey(r_paddle.right_puddle_down, "Down")
screen.onkey(l_paddle.left_puddle_up, "w")
screen.onkey(l_paddle.left_puddle_down, "s")

screen.onkey(turn_off, "c")

game_on = True
# rebound = 0

while game_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        # rebound += 1
        # print(rebound)
        ball.paddle_bounce()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # rebound += 1
        # print(rebound)
        ball.paddle_bounce()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.wall_bounce()

    if ball.xcor() > 380 and ball.ycor() in range(-280, 280):
        # print("ball out")
        scoreboard.increase_left_score()
        ball.home()
        y_pos = [-1, 1]
        ball.reset(-1, random.choice(y_pos))
        # sleep = 0.1

    if ball.xcor() < -380 and ball.ycor() in range(-280, 280):
        # print("ball out")
        scoreboard.increase_right_score()
        ball.home()
        y_pos = [-1, 1]
        ball.reset(-1, random.choice(y_pos))

screen.exitonclick()
