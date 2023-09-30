import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score



screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

def turn_off():
    screen.bye()


screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(turn_off, key="c")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    score.update_scoreboard()
    snake.move()

    #collision detection with food
    if snake.segments[0].distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.enlarge()

    # collision detection with walls
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        # game_on = False
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:  #python slicing
        if snake.segments[0].distance(segment) < 10:
            # game_on = False
            # score.game_over()
            score.reset()
            snake.reset()

# score.game_over()
score.reset()

screen.exitonclick()