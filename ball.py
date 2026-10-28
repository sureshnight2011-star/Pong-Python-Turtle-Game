from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.dx = 1
        self.dy = 1
        self.shapesize(stretch_wid=1, stretch_len=1)