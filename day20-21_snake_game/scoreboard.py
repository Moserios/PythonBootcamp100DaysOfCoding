import turtle
from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,350)
        self.color("white")

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 18, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):

        self.goto(0, 0)
        self.write(f"Game Over", False, align="center", font=("Arial", 18, "normal"))