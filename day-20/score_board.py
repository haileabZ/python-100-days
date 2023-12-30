
from turtle import Turtle
FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.display()
        self.hideturtle()

    def display(self):
        self.clear()
        self.color("white")
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
            self.write(f"Score: {self.score}  high-score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over: ", align=ALIGNMENT, font=FONT)


