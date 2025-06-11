import random
import colorgram
from turtle import Turtle, Screen

def extract_colors(number_of_colors,brightness_factor):
    rgb_colors = []
    colors = colorgram.extract('image.jpg', int(number_of_colors))

    while len(rgb_colors) < 10:
        brightness_factor += 1
        print(f"You need at least 10 colours, increasing brightness factor to: {brightness_factor}")
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            brightness_sum = int(r + g + b)

            if brightness_sum < brightness_factor:
                rgb_colors.append((r, g, b))
            else:
                pass


    return rgb_colors

screen = Screen()
turtle = Turtle()
screen.colormode(255)
turtle.speed("fastest")

# Lesson requirements: Grid 10 x 10, Dot size 20, spacing 50.
grid_size = [10,10]
dot_size = 20
dot_spacing = 50
available_colors = extract_colors(30,500)
turtle.pensize(dot_size)

turtle.pu()

for x in range(grid_size[1] + 1):
    for y in range(grid_size[0]):
        turtle.pencolor(random.choice(available_colors))
        turtle.dot(dot_size)
        turtle.forward(dot_spacing)

    turtle.home()
    turtle.setheading(0)
    turtle.forward(x * dot_spacing)
    turtle.setheading(90)

turtle.home()

screen.exitonclick()