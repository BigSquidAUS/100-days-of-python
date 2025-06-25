from turtle import Turtle
FONT = ("Arial", 12, "normal")
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        with open("data.txt") as data_file:
            self.data_high_score = data_file.read()

        self.score = 0
        self.high_score = int(self.data_high_score)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def update(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGN, font=FONT)