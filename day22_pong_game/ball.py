from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x_pos = self.xcor() + self.x_move
        new_y_pos = self.ycor() + self.y_move
        self.goto(new_x_pos, new_y_pos)

    def wall_bounce(self):
        self.y_move *= -1


    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.95

    def reset(self, x_direct, y_direct):
        self.x_move *= x_direct
        self.y_move *= y_direct
        self.ball_speed = 0.1
