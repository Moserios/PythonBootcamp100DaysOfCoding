from turtle import *
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for position in POSITIONS:
            self.add_tail(position)

    def add_tail(self, position):
        randname = Turtle(shape="square")
        randname.penup()
        randname.goto(position)
        randname.color("white")
        self.segments.append(randname)

    def enlarge(self):
        self.add_tail(self.segments[-1].position())


    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)


    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)


    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

