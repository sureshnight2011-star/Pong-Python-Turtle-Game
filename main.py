# Things to Add:
# 1. Implement the ramp up speed feature.
# 2. Implement the target max score feature.
# 3. Play Again Feature
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from turtle import Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_SCORE = 10

class Main:
    def __init__(self):
        # Creating the objects to use in the game loop.
        self.left_paddle = Paddle(player="Player 1", x=-250, y=0)
        self.right_paddle = Paddle(player="Player 2", x=240, y=0)
        self.pong_ball = Ball()
        self.score_board = ScoreBoard()

        # Setting up the screen.
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Pong")
        self.screen.tracer(0)

        # A dictionary for if the keys were pressed or not.
        self.keys_pressed = {
            "Up": False,
            "Down": False,
            "w": False,
            "s": False,
        }

        # The functions for pressing and releasing each key.
        def press_up(): self.keys_pressed["Up"] = True
        def release_up(): self.keys_pressed["Up"] = False

        def press_down(): self.keys_pressed["Down"] = True
        def release_down(): self.keys_pressed["Down"] = False

        def press_w(): self.keys_pressed["w"] = True
        def release_w(): self.keys_pressed["w"] = False

        def press_s(): self.keys_pressed["s"] = True
        def release_s(): self.keys_pressed["s"] = False

        # The (on key press) and (on key release) functions for setting each key to the function.
        # self.screen.listen used only once to listen to the keys.
        self.screen.listen()

        self.screen.onkeypress(press_up, "Up")
        self.screen.onkeyrelease(release_up, "Up")
        self.screen.onkeypress(press_down, "Down")
        self.screen.onkeyrelease(release_down, "Down")

        self.screen.onkeypress(press_w, "w")
        self.screen.onkeyrelease(release_w, "w")
        self.screen.onkeypress(press_s, "s")
        self.screen.onkeyrelease(release_s, "s")

        # Called this to set up the initial score on the top of the window.
        self.score_board.initialize()

        # Main game loop for running the game.
        self.game_is_on = True
        while self.game_is_on:
            # Set the x and y coordinate, so the ball can move after every loop.
            self.pong_ball.setx(self.pong_ball.xcor() + self.pong_ball.dx)
            self.pong_ball.sety(self.pong_ball.ycor() + self.pong_ball.dy)
            # Pong ball to wall collision check
            if self.pong_ball.ycor() >= (SCREEN_HEIGHT / 2) - 10:
                self.pong_ball.dy *= -1
            elif self.pong_ball.ycor() <= (SCREEN_HEIGHT / -2) + 10:
                self.pong_ball.dy *= -1

            # Pong ball to paddle collision check
            if self.pong_ball.xcor() == (SCREEN_HEIGHT / -2) + 65 and (self.left_paddle.ycor() - 50 <= self.pong_ball.ycor() <= self.left_paddle.ycor() + 50):
                self.pong_ball.dx *= -1
            elif self.pong_ball.xcor() == (SCREEN_HEIGHT / 2) - 75 and (self.right_paddle.ycor() - 50 <= self.pong_ball.ycor() <= self.right_paddle.ycor() + 50):
                self.pong_ball.dx *= -1

            # If ball goes past either paddle, point for the other player, and update the score.
            if self.pong_ball.xcor() < SCREEN_WIDTH / -2:
                self.pong_ball.setx(0)
                self.pong_ball.sety(0)
                self.pong_ball.dx *= -1
                self.pong_ball.dy *= -1
                self.score_board.right_score_update()
            elif self.pong_ball.xcor() > SCREEN_WIDTH / 2:
                self.pong_ball.setx(0)
                self.pong_ball.sety(0)
                self.pong_ball.dx *= -1
                self.pong_ball.dy *= -1
                self.score_board.left_score_update()

            # Setting up the wall boundaries for the left paddle.
            if self.left_paddle.ycor() >= (SCREEN_HEIGHT / 2) - 50:
                self.left_paddle.sety((SCREEN_HEIGHT / 2) - 50)
            elif self.left_paddle.ycor() <= (SCREEN_HEIGHT / -2) + 50:
                self.left_paddle.sety((SCREEN_HEIGHT / -2) + 50)

            # Setting up the wall boundaries for the right paddle.
            if self.right_paddle.ycor() >= (SCREEN_HEIGHT / 2) - 50:
                self.right_paddle.sety((SCREEN_HEIGHT / 2) - 50)
            elif self.right_paddle.ycor() <= (SCREEN_HEIGHT / -2) + 50:
                self.right_paddle.sety((SCREEN_HEIGHT / -2) + 50)

            # Checking if the keys are pressed or not for the right paddle.
            if self.keys_pressed["Up"]:
                self.right_paddle.up()
            elif self.keys_pressed["Down"]:
                self.right_paddle.down()

            # Checking if the keys are pressed or not for the left paddle.
            if self.keys_pressed["w"]:
                self.left_paddle.up()
            elif self.keys_pressed["s"]:
                self.left_paddle.down()

            # Updating the screen after every loop in the while loop.
            self.screen.update()

            # time.sleep used to control the speed of the gameplay.
            time.sleep(0.01)

if __name__ == '__main__':
    main = Main()