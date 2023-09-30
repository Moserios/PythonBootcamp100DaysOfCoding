import random
from turtle import Turtle, Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time

def turn_off_game():
    screen.bye()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
all_cars = []
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(turn_off_game, "c")

sleep_time = 0
# car_speed = 5
game_is_on = True
ratio = 10
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    generate_a_car = random.randint(0, 100)
    if ratio == 0:
        ratio = 1
    if generate_a_car % ratio == 0:
        car = Car()
        all_cars.append(car)
    for car in all_cars:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
        if car.xcor() >= 400:
            sleep_time = 0.1
        if car.xcor() > 500:
            car_index = all_cars.index(car)
            del all_cars[car_index]


    if player.ycor() >= 290:
        player.start_position()
        scoreboard.next_level()
        car.speed_up()
        # sleep_time *= 0.9
        ratio -= 1



scoreboard.game_over()
screen.exitonclick()