from turtle import Turtle

FONT = ("Impact", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the Scoreboard."""
        self.clear()
        self.goto(-300, 225)
        self.write(self.left_score, align="center", font=FONT)
        self.goto(300, 225)
        self.write(self.right_score, align="center", font=FONT)

    def left_points(self):
        """Increments the left scoreboard."""
        self.left_score += 1
        self.update_scoreboard()

    def right_points(self):
        """Increments the right scoreboard."""
        self.right_score += 1
        self.update_scoreboard()
