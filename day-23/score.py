
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()

    def game_over(self, is_won):
        if is_won:
            self.write("You Won!", align="center", font=("courier", 25, "normal"))
        else:
            self.write("You Lose!", align="center", font=("courier", 25, "normal"))
