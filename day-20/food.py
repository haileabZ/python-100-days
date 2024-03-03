












from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.create_food()


    def create_food(self):
        self.x = randint(-280, 280)
        self.y = randint(-280, 280)
        self.goto(self.x, self.y)





