from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
ball = Ball()

screen.tracer(0)
score = Scoreboard()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()

screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)

screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

is_game_on = True
while is_game_on:
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -330):
        ball.deflect()

    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.deflect()
        score.l_point()
        score.update_score()

    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.deflect()
        score.r_point()
        score.update_score()



screen.exitonclick()
