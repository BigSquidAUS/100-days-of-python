import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win?\n"
                                                         "(Red, Orange, Yellow, Green, Blue or Purple)\n"
                                                         "Enter a colour: ")
number_of_turtles = 6
colours = ["red","orange","yellow","green","blue","purple"]
padding = 30
bottom_left = [-(screen.window_width() // 2) + padding, (-(number_of_turtles * padding) // 2) + padding]

turtles = []

def random_distance():
    return random.randint(0,10)

for n in range(0,number_of_turtles):
    t = Turtle(shape="turtle")
    t.pu()
    t.color(colours[n])
    t.goto(bottom_left[0],bottom_left[1]+(padding * n))
    turtles.append(t)

if user_bet:
    is_race_on = True

print(f"You bet on {user_bet.capitalize()} to win.")

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle.lower() == user_bet.lower():
                print(f"{winning_turtle.capitalize()} won.\nYay! Your Turtle won.")
            else:
                print(f"{winning_turtle.capitalize()} won.\nYou lost.\nWhat are you really gambling with? Gamble responsibly.")
            is_race_on = False
        turtle.forward(random_distance())


screen.exitonclick()