from turtle import Turtle, Screen
import random
t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed(0)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        t.color(rgb)
        t.circle(100)
        t.left(size_of_gap)

draw_spirograph(5)
screen.exitonclick()
