# from turtle import *
#
# tim = Turtle()
# screen = Screen()
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def turn_off():
#     screen.bye()
#
# def restart():
#     tim.reset()
#
#
# screen.listen()
# screen.onkey(move_forward, key="w")
# screen.onkey(move_backward, key="s")
# screen.onkey(turn_left, key="a")
# screen.onkey(turn_right, key="d")
# screen.onkey(turn_off, key="b")
# screen.onkey(restart, key="c")
# screen.exitonclick()


################# Turtle race ###############
from turtle import *
import random
screen = Screen()

screen.setup(500,400)
user_choice = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-125, -75, -25, 25, 75, 125]
names = ['leo', 'raf', 'mic', 'dan', 'tim', 'tom']
name_pos = 0
y_pos = 0
color_index = 0
is_race_on = False
all_racers = []

for _ in range(6):
    names[name_pos] = Turtle(shape="turtle")
    names[name_pos].color(colors[color_index])
    names[name_pos].penup()
    names[name_pos].goto(x=-230, y=y_position[y_pos])
    all_racers.append(names[name_pos])
    name_pos += 1
    y_pos += 1
    color_index += 1

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_racers:
        if turtle.xcor() > 210:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print("You won!")
            else:
                print(f"You lost. The winner is {winner}")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)


def turn_off():
    screen.bye()

screen.listen()
screen.onkey(turn_off, key="c")
screen.exitonclick()
