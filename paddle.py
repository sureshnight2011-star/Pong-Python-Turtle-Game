from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, player, x, y):
        super().__init__()
        self.player = player
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.penup()
        self.goto(self.x, self.y)

    def up(self):
        self.forward(5)

    def down(self):
        self.backward(5)