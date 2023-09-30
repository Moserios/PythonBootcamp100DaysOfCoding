from turtle import Turtle
import random
car_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
start_car_speed = 5
l_stream_y_position = random.choice(range(-260, -10))
r_stream_y_position = random.choice(range(10, 260))
l_stream_cars_start_position = (-400, l_stream_y_position)
r_stream_cars_start_position = (400, r_stream_y_position)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(car_colors))
        self.penup()
        self.new_random_car()
        self.car_speed = start_car_speed
        # self.move_speed = 0.1

    def new_random_car(self):
        random_y = random.randint(20, 250)
        choice = [-1, 1]
        random_direction = random.choice(choice)
        if random_direction == -1:
            random_y *= random_direction
            self.goto(-400, random_y)
        else:
            self.goto(400, random_y)
    def move(self):
        car_direction = self.car_speed
        if self.ycor() > 0:
            car_direction *= -1

        new_x = self.xcor() + car_direction
        self.goto(new_x, self.ycor())

    def speed_up(self):
        global start_car_speed
        start_car_speed += 1
