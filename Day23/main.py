import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
screen.listen()
car_manager = CarManager()
player = Player()
screen.onkey(key="Up", fun=player.move)
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()

    is_at_finish = player.end()
    if is_at_finish == True:
        car_manager.level_up()
        scoreboard.level_up()
        scoreboard.score_display()

    for car in car_manager.carList:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()


