from turtle import Turtle

class Label(Turtle):
    def __init__(self,text,x,y):
        label = text.title()
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(x, y)
        self.write(label)