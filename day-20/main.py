





from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.create_food()
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.display()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset_snake()

    for segment in snake.segments :
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()









screen.exitonclick()
