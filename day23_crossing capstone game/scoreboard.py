from turtle import Turtle


FONT = ("courier", 12, "normal")
ALIGNMENT = 'left'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-350, 280)
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(-0, 0)
        self.clear()
        self.write(f"      Game Over!\nYour final level: {self.score}", align="center", font=("courier", 28, "normal"))
        # self.update()