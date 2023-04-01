from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.carList = []
        self.speed = STARTING_MOVE_DISTANCE

    def create(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.carList.append(car)

    def move(self):
        for car in self.carList:
            car.backward(self.speed)

    def level_up(self):
        self.speed += STARTING_MOVE_DISTANCE
