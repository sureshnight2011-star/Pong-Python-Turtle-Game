from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from turtle import Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Main:
    def __init__(self):
        self.left_paddle = Paddle(player="Player 1", x=-250, y=0)
        self.right_paddle = Paddle(player="Player 2", x=240, y=0)
        self.pong_ball = Ball()
        self.score_board = ScoreBoard()

        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Pong")
        self.screen.tracer(0)

        self.keys_pressed = {
            "Up": False,
            "Down": False,
            "w": False,
            "s": False,
        }

        def press_up(): self.keys_pressed["Up"] = True
        def release_up(): self.keys_pressed["Up"] = False

        def press_down(): self.keys_pressed["Down"] = True
        def release_down(): self.keys_pressed["Down"] = False

        def press_w(): self.keys_pressed["w"] = True
        def release_w(): self.keys_pressed["w"] = False

        def press_s(): self.keys_pressed["s"] = True
        def release_s(): self.keys_pressed["s"] = False

        self.screen.listen()

        self.screen.onkeypress(press_up, "Up")
        self.screen.onkeyrelease(release_up, "Up")
        self.screen.onkeypress(press_down, "Down")
        self.screen.onkeyrelease(release_down, "Down")

        self.screen.onkeypress(press_w, "w")
        self.screen.onkeyrelease(release_w, "w")
        self.screen.onkeypress(press_s, "s")
        self.screen.onkeyrelease(release_s, "s")

        self.game_is_on = True
        while self.game_is_on:
            time.sleep(0.01)

            if self.keys_pressed["Up"]:
                self.right_paddle.up()
            if self.keys_pressed["Down"]:
                self.right_paddle.down()

            if self.keys_pressed["w"]:
                self.left_paddle.up()
            if self.keys_pressed["s"]:
                self.left_paddle.down()

            self.screen.update()

        self.screen.exitonclick()

if __name__ == '__main__':
    main = Main()