# import colorgram
# colors = colorgram.extract("./painting.jpg", 30)
# all_colors = []
# rgb_tuple = ()
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_tuple = (red, green, blue)
#     all_colors.append(rgb_tuple)
#
# print(all_colors)
import random
from turtle import Turtle, Screen
color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]
t = Turtle()
screen = Screen()
screen.colormode(255)
# print(random.choice(color_list))
t.penup()
t.hideturtle()
t.speed("fastest")
t.setposition(-300, -200)


def draw_row():
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)


for _ in range(5):
    draw_row()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    draw_row()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

screen.exitonclick()