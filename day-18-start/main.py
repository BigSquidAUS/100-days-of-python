import math
import random
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.color("#4e8752")
tim.speed("fastest")

color_palette = ["navy","sea green","saddle brown","khaki","medium slate blue","light coral","light green","dodger blue","sandy brown","rosy brown"]
screen.colormode(255)

def rand_color_value():
    value = ()  # ( ) denote "tuple"
    for _ in range(3):
        value += (random.randint(0, 255)),
    return value

def challenge_01():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def challenge_02():
    for _ in range(15):
        tim.pd()
        tim.forward(10)
        tim.pu()
        tim.forward(10)

def challenge_03():
    for s in range(3,10):
        tim.pencolor(rand_color_value())
        angle = float(360 / s)
        for _ in range(s):
            tim.right(angle)
            tim.forward(100)

def challenge_04(): # Random Walk
    tim.pensize(12)
    tim.speed("fastest")
    step_size = 25
    diagonal_dirs = [45, 135, 225, 315]

    for _ in range(500):
        random_dir = random.choice([0, 45, 90, 135, 180, 225, 270, 315])
        tim.pencolor(rand_color_value())
        tim.setheading(random_dir)

        if random_dir in diagonal_dirs:
            tim.forward(step_size / math.sqrt(2))
        else:
            tim.forward(step_size)

def challenge_05():
    tim.speed("fastest")
    for n in range(0,360,5):
        tim.pencolor(rand_color_value())
        tim.setheading(n)
        tim.circle(200)

challenge_05()

screen.exitonclick()