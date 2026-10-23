from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, player, x, y):
        super().__init__()
        self.player = player
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.x, self.y)