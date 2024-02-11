


import turtle
from turtle import Turtle, Screen
from tkinter import messagebox
from random import randint

screen = Screen()
user_choice=""

def move_randomly(obj):
    speed = randint(0,10)
    obj.penup()
    obj.forward(speed)


position = [100, 70, 40, 10]
colors = ["red","blue","green","purple"]
turtles = []

for i in range(4):
    tim = Turtle()
    tim.color(colors[i])
    tim.shape("turtle")
    tim.penup()
    tim.setpos(-300,position[i])
    turtles.append(tim)

user_choice = screen.textinput("betting", "choose a color to bet!")
while user_choice.lower().strip() not in colors:
    user_choice = screen.textinput("betting", "choose a color to bet!")

is_not_ended = True
x_coordinates=[]

while is_not_ended:
     for t in turtles:

        if t.xcor() > 230:
            for i in turtles:
                x_coordinates.append(i.xcor())
            winning_color =colors[x_coordinates.index(max(x_coordinates))]
            is_not_ended = False
            if user_choice == winning_color:
                messagebox.showinfo("tutle bet", f"turtle {winning_color} won the game\n you won the game!")
            else:
                messagebox.showinfo("tutle bet", f"turtle {winning_color} won the game\n you lose")

        else:
                move_randomly(t)




turtle.exitonclick()
