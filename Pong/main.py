import turtle
from turtle import listen, Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
turtle.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Score()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


turtle.listen()
turtle.onkey(r_paddle.paddle_up, "w")
turtle.onkey(r_paddle.paddle_down, "s")
turtle.onkey(l_paddle.paddle_up, "i")
turtle.onkey(l_paddle.paddle_down, "k")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 370:
        ball.restart()
        scoreboard.l_point()
    elif ball.xcor() < -370:
        ball.restart()
        scoreboard.r_point()

    ball.move()


screen.exitonclick()