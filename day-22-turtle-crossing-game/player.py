from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("green")
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0,new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(0,new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)