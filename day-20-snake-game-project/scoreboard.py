from turtle import Turtle
FONT = ("Arial", 12, "normal")
ALIGN = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGN, font=FONT)