from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.pos = (x, y)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.pos)

    def up(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y + 10)

    def down(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y - 10)
