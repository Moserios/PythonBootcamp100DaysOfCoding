# import turtle
# from turtle import * #Turtle, Screen
# import random
# turtle.colormode(255)
#
# tim = Turtle()



# tim.shape("turtle")
# tim.color("springgreen")
# tim.pencolor("blue")

# screen.setup (width=800, height=800, startx=150, starty=500)

#### Movements (Geometry figures)

# line_color = ["red", "orange", "blue", "green", "yellow", "brown", "grey", "violet", "chocolate", "purple"]
# sides = 3
# length_run = 100
# color_index = 0
# while sides < 13:
#     tim.pencolor(line_color[color_index])
#     for _ in range(sides):
#         tim.forward(length_run)
#         tim.right(angle = 360 / sides)
#     sides += 1
#     color_index += 1

################ Random movements #################
# line_color = ["red", "orange", "blue", "green", "pink", "brown", "grey", "violet", "chocolate", "purple"]

# movement = [tim.forward(100), tim.backward(100)]
# angle = [tim.right(100), tim.left(100)]

# while True:
#     # random.choice(line_color)
#     random.choice(movement)
#     random.choice(angle)

########
#
# tim.width(3)
# tim.speed(0)
# def random_rgb_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_set = (r, g, b)
#     return color_set
#
# def draw_a_circle(shift):
#     for _ in range(int(360 / shift)):
#         tim.pencolor(random_rgb_color())
#         tim.circle(200)
#         tim.right(shift)
#
# draw_a_circle(5)
#
# screen = turtle.Screen()
# screen.exitonclick()

############################a modern art paint ###########

import colorgram
import random
import turtle
from turtle import * #Turtle, Screen
turtle.colormode(255)
tim = Turtle()
tim.penup()

# Extract 6 colors from an image.

# colors = colorgram.extract('new_image2.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
screen = turtle.Screen()
tim.hideturtle()
screen.screensize(650, 650)
tim.speed(0)
# screen.setup (width=650, height=650, startx=150, starty=150)

color_list = [(176, 48, 69), (23, 106, 155), (34, 136, 69), (220, 163, 89), (10, 62, 132), (208, 73, 97), (224, 84, 53), (159, 85, 39), (99, 165, 207), (123, 195, 176), (41, 163, 108), (180, 158, 55), (5, 100, 51), (232, 203, 61), (131, 37, 46), (239, 204, 2), (54, 53, 53), (170, 208, 204), (7, 57, 108), (74, 41, 50), (107, 100, 166), (178, 148, 155), (15, 66, 37), (168, 24, 21), (3, 98, 115), (55, 152, 183)]


start_x = -225
start_y = -225
x_shift = 50
y_shift = 50
dot_size = 20

for _ in range(10):
    tim.setx(start_x)
    tim.sety(start_y)
    tim.dot(dot_size, random.choice(color_list))
    for _ in range(9):
        tim.forward(x_shift)
        tim.dot(dot_size, random.choice(color_list))
    start_y += y_shift

screen.exitonclick()
# print(rgb_colors)