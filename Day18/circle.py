from turtle import Turtle, Screen

first_turtle = Turtle()
first_turtle.color("red")
for i in range(4):
    first_turtle.forward(100)
    first_turtle.left(90)

screen = Screen()
screen.exitonclick()
