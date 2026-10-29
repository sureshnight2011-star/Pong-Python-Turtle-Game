from turtle import Turtle

class WinningScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

    def left_paddle(self):
        self.write(arg="Player 1 won!", align="center", font=("Arial", 30, "normal"))

    def right_paddle(self):
        self.write(arg="Player 2 won!", align="center", font=("Arial", 30, "normal"))