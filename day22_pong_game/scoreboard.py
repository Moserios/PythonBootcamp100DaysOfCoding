from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.left_player_score, align="center", font=("Arial", 28, "normal"))
        self.goto(100, 260)
        self.write(self.right_player_score, align="center", font=("Arial", 28, "normal"))

    def increase_left_score(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_player_score += 1
        self.update_scoreboard()