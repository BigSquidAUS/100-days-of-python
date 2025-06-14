from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.forward((-10))

def rotate_l():
    return tim.setheading(float(tim.heading()) + 6.0)

def rotate_r():
    return tim.setheading(float(tim.heading()) - 6.0)

def clear_screen():
    screen.reset()
    

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_l)
screen.onkey(key="d", fun=rotate_r)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()