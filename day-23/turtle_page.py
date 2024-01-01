
from turtle import Turtle


class TimmyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.left(90)
        self.penup()
        self.goto(0, -280)

    def move_up(self):
        y_pos = self.ycor() + 10
        self.goto(0,y_pos)

