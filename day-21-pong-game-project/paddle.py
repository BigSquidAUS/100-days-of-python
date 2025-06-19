from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,start_x):
        super().__init__()

        self.x_pos = start_x
        self.y_pos = 0

        self.shape("square")
        self.speed("fastest")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x_pos,self.y_pos)

    def move_up(self):
        self.y_pos += 40
        self.goto(self.x_pos,self.y_pos)

    def move_down(self):
        self.y_pos -= 20
        self.goto(self.x_pos,self.y_pos)