









from turtle import Turtle
from random import choice, randint


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(self.random_color())
        self.shapesize(stretch_wid=1, stretch_len= 2)
        self.penup()
        self.random_position()

    def random_color(self):
        colors = ["red", "blue", "yellow", "green", "black", "purple", "pink", "violet"]
        return choice(colors)

    def random_position(self):
        x_pos = randint(300, 2000)
        y_pos = randint(-250, 250)
        self.goto(x_pos, y_pos)

    def move(self):
        self.forward(-10)



