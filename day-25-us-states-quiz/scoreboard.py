from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = -1
        self.hideturtle()
        self.goto(-350,230)
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}")