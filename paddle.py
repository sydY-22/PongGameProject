from turtle import Turtle
PADDLE_COLOR = "white"


class Paddle(Turtle):

    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.shape("square")
        self.create_paddle()

    def create_paddle(self):
        """Creates the paddle."""
        self.left(90)
        self.penup()
        self.goto(self.x_axis, self.y_axis)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(PADDLE_COLOR)

    def move_up(self):
        """Moves the paddle up."""
        self.forward(20)

    def move_down(self):
        """Moves the paddle down."""
        self.backward(20)

