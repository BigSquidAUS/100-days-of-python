import math
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

# Lesson requirements: Grid 10 x 10, Dot size 20, spacing 50.
turtle = Turtle()
grid_size = [7,25]
dot_size = 20
dot_spacing = 50
padding = dot_size * 2
available_colors = extract_colors(30,500)
turtle.pensize(dot_size)
turtle.speed("fastest")

screen = Screen()
screen_width = int((grid_size[1]-1) * dot_spacing + dot_size + math.ceil(dot_size / 2) + padding)
screen_height = int((grid_size[0]-1) * dot_spacing + dot_size + math.ceil(dot_size / 2) + padding)
screen.setup(screen_width,screen_height)

print(f"W: {screen_width}")
print(f"H: {screen_height}")

screen.colormode(255)


bottom_left_x = (-screen_width // 2) + (dot_size // 2) + padding//2
bottom_left_y = (-screen_height // 2) + dot_size + padding//2

turtle.pu()
turtle.goto(bottom_left_x,bottom_left_y)

for x in range(grid_size[1]):
    for y in range(grid_size[0]):
        turtle.pencolor(random.choice(available_colors))
        turtle.dot(dot_size)
        turtle.setheading(90)
        turtle.forward(dot_spacing)

    turtle.goto(bottom_left_x,bottom_left_y)
    turtle.setheading(0)
    turtle.forward((x + 1) * dot_spacing)

turtle.goto(bottom_left_x,bottom_left_y)

screen.exitonclick()