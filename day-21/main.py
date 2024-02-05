
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong_game")
screen.tracer(0)


screen.listen()
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time_slice = 0.1
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if paddle1.distance(ball) < 50 and ball.xcor() > 330:
        ball.reset_game()

    if paddle2.distance(ball) < 50 and ball.xcor() < -330:
        ball.reset_game()

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.score_l += 1
        scoreboard.clear()
        scoreboard.dispaly_score()

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.score_r += 1
        scoreboard.clear()
        scoreboard.dispaly_score()

screen.exitonclick()



