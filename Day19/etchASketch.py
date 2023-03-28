from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def counter_clockwise():
    t.left(10)


def clockwise():
    t.right(10)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
