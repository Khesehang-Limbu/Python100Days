from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Using Python")
screen.tracer(0) #This method will either stop or start the animation. To get the normal animation flow, we must use the screen.update() method
screen.listen()

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        scoreboard.print_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()
