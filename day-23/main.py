












from turtle import Screen
from turtle_page import TimmyTurtle
from cars import Car
from score import Score

import time


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

tim = TimmyTurtle()
score = Score()

all_cars = []

for _ in range(35):
   new_car = Car()
   all_cars.append(new_car)


screen.onkey(tim.move_up, "Up")

game_is_on = True
is_won = True
while game_is_on:
   screen.update()
   time.sleep(0.1)
   for car in all_cars:
      car.move()
      if tim.distance(car) < 20:
         game_is_on = False
         score.game_over(not is_won)

   if tim.ycor() > 270:
      game_is_on = False
      score.game_over(is_won)






screen.exitonclick()
