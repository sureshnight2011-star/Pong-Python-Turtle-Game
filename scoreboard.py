from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.goto(0, 250)

    def initialize(self):
        self.write(arg=f"{self.left_score} : {self.right_score}", align="center", font=("Arial", 30, "normal"))

    def left_score_update(self):
        self.clear()
        self.left_score += 1
        self.write(arg=f"{self.left_score} : {self.right_score}", align="center", font=("Arial", 30, "normal"))
        return

    def right_score_update(self):
        self.clear()
        self.right_score += 1
        self.write(arg=f"{self.left_score} : {self.right_score}", align="center", font=("Arial", 30, "normal"))
        return