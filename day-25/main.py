







import turtle
from turtle import Screen,Turtle
import  pandas as pd
import  time


tim = Turtle()
screen = Screen()
screen.setup(700, 600)
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")

guessed_states = []
while len(guessed_states) < 51:
    guess = screen.textinput(f"{len(guessed_states) + 1}/50 states", "Enter name of state").title()
    if guess in data["state"].tolist() and guess not in guessed_states:
        guessed_states.append(guess)
        tim.penup()
        tim.home()
        tim.pendown()
        searched = data[data["state"] == guess]
        x_pos = int(searched["x"])
        y_pos = int(searched["y"])
        tim.hideturtle()
        tim.goto(x_pos, y_pos)
        time.sleep(0.2)
        tim.clear()
        tim.write(guess, move=False, align="center", font=("Arial", 8, "normal"))

screen.exitonclick()

