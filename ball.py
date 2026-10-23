from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)