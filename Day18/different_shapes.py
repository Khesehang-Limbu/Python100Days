from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
n = 3
completed = False
screen.colormode(255)
while not completed:
    for i in range(n):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        rgb = (r, g, b)
        tim.color(rgb)
        tim.right(int(360/n))
        tim.forward(100)
    n += 1
    if n==10:
        completed=True


screen.exitonclick()