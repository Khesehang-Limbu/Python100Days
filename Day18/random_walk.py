import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
directions = [0, 90, 180, 270]

tim.speed(0)
tim.pensize(15)
screen.colormode(255)

for _ in range(200):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rgb = (r, g, b)
    tim.color(rgb)
    tim.setheading(random.choice(directions))
    tim.forward(random.randint(20, 30))

screen.exitonclick()
