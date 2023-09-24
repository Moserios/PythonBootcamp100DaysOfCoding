from turtle import Turtle
PADDLE_START_X_POSITION = 0
MOVE_DISTANE = 20


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        global PADDLE_START_X_POSITION
        PADDLE_START_X_POSITION = x_cor
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(x_cor, 0)

    def right_puddle_up(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.setpos(x=x_position, y=y_position + MOVE_DISTANE)

    def right_puddle_down(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.setpos(x_position, y_position - MOVE_DISTANE)

    def left_puddle_up(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.setpos(x=x_position, y=y_position + MOVE_DISTANE)

    def left_puddle_down(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.setpos(x_position, y_position - MOVE_DISTANE)

    # def left_puddle_up(self):
    #     for segment in range(0, len(self.paddle)):
    #         x_position = self.paddle[segment].xcor()
    #         y_position = self.paddle[segment].ycor()
    #         self.paddle[segment].setpos(x_position, y_position + MOVE_DISTANE)
    #
    # def left_puddle_down(self):
    #     for segment in range(0, len(self.paddle)):
    #         x_position = self.paddle[segment].xcor()
    #         y_position = self.paddle[segment].ycor()
    #         self.paddle[segment].setpos(x_position, y_position - MOVE_DISTANE)
