from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make a guess", prompt="Who will win the race? ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
is_game_on = False


def starting_pos(y, color):
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(-230, y)
    return t


y = -100
for i in range(6):
    y += 30
    new_turtle = starting_pos(y, colors[i])
    turtles.append(new_turtle)


if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        random_distance = random.randint(1, 10)
        if turtle.xcor() >= 230:
            is_game_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won, the winning color is {winner} turtle")
            else:
                print(f"You've lost, the winning color is {winner} turtle")
        turtle.forward(random_distance)


screen.exitonclick()
