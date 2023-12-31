
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score_r = 0
        self.score_l = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.dispaly_score()

    def dispaly_score(self):
        self.write(f"{self.score_l} : {self.score_r}", align="center", font=("arial", 25, ""))


