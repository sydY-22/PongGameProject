from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Syd's Pong Game!")
# pauses animations on the screen.
screen.tracer(0)

# create both the paddles.
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# create the ball.
ball = Ball()

# show the scoreboard.
scoreboard = Scoreboard()

# listen for user input.
screen.listen()
# left paddle controls.
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
# right paddle controls.
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # shows the animations on the screen.
    screen.update()
    ball.move_ball()
    # detect collision with the walls.
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
        ball.change_color()
    # detect collision with paddles.
    if (ball.distance(r_paddle) < 45 and ball.xcor() > 320) or (ball.distance(l_paddle) < 45 and ball.xcor() < -320):
        ball.bounce_x()
        ball.change_color()

    # detect misses for each paddle.
    if ball.xcor() >= 400:
        ball.reset_position()
        scoreboard.left_points()

    if ball.xcor() <= -400:
        ball.reset_position()
        scoreboard.right_points()

screen.exitonclick()
