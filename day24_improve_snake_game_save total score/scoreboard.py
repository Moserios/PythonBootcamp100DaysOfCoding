from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.highscore = 0
        self.color("white")
        self.update_scoreboard()
        self.read_highscore()


    def read_highscore(self):
        with open("data.txt") as file:
            self.highscore = int(file.read())
            file.close()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.highscore}", False, align="center", font=("Arial", 10, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        self.save_highscore()



    # def game_over(self):
    #
    #     self.goto(0, 0)
    #     self.write(f"Game Over", False, align="center", font=("Arial", 18, "normal"))