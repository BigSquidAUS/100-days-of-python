from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_dir = 1
        self.y_dir = 1
        self.increase_speed_by = 0.05 # Amount to increase ball speed by every time it hits a paddle.
        self.ball_speed_factor = 0.5 # Initial ball speed.

    def move(self,hit):
        time.sleep(0.007)

        if hit == "top":
            self.y_dir = -1

        elif hit == "bottom":
            self.y_dir = 1

        if hit == "paddle_r":
            self.x_dir = -1

        elif hit == "paddle_l":
            self.x_dir = 1

        self.goto(self.xcor() + ((1 + self.ball_speed_factor) * self.x_dir), self.ycor() + ((1 + self.ball_speed_factor) * self.y_dir))

    def reset_position(self):
        self.goto(0,0)
        self.x_dir *= -1
        self.ball_speed_factor = 0.5