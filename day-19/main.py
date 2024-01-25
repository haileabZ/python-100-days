
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.forward(-20)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_drawing():
    tim.home()
    tim.clear()

turtle.listen()

turtle.onkey(move_forward,"w")
turtle.onkey(move_backward,"s")
turtle.onkey(move_counter_clockwise,"a")
turtle.onkey(move_clockwise,"d")
turtle.onkey(clear_drawing,"c")

screen.exitonclick()

