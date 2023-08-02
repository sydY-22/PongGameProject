from turtle import Turtle
import random

BALL_COLOR = "white"
BALL_COLORS = ["white", "red", "purple", "blue", "yellow", "green", "orange"]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.fillcolor(BALL_COLOR)
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        """Moves the ball."""
        new_x_axis = self.xcor() + self.x_move
        new_y_axis = self.ycor() + self.y_move
        self.goto(new_x_axis, new_y_axis)

    def bounce_y(self):
        """Bounces the ball vertically."""
        self.y_move *= -1

    def bounce_x(self):
        """Bounces the ball horizontally."""
        self.x_move *= -1
        self.increase_speed()

    def change_color(self):
        """Changes the color of the ball when bounced."""
        self.fillcolor(random.choice(BALL_COLORS))

    def reset_position(self):
        """Resets the position of the ball."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        """Increases the speed of the ball."""
        self.move_speed *= 0.9

