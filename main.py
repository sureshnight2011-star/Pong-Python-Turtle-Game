from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from turtle import Screen

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Main:
    def __init__(self):
        paddle1 = Paddle(player="Player 1", x=-250, y=0)
        paddle2 = Paddle(player="Player 2", x=240, y=0)
        pong_ball = Ball()
        score_board = ScoreBoard()

        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Pong")
        self.screen.tracer(0)

        self.screen.onkeypress(paddle1.up, "w")
        self.screen.onkeypress(paddle1.down, "s")
        self.screen.onkeypress(paddle2.up, "Up")
        self.screen.onkeypress(paddle2.down, "Down")
        self.screen.listen()

        self.screen.exitonclick()

if __name__ == '__main__':
    main = Main()