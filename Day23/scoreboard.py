from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.level = 0
        self.score_display()

    def score_display(self):
        self.write(arg=f"Level : {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over !", align="center", font=FONT)
