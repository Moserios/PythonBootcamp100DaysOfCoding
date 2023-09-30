from turtle import Turtle
MOVE_FORWARD = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start_position()
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + MOVE_FORWARD
        self.goto(0, new_y)

    def start_position(self):
        self.goto(0, -280)