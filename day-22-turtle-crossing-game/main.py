import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.update()
player = Player()
score = Scoreboard()
cars = CarManager()
screen.update()

screen.onkey(player.move_up, key="w")
#screen.onkey(player.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.generate_car()

    for car in cars.the_cars:
        car.move_car(score.level)
        if car.xcor() <= -300:
            car.hideturtle()
            cars.the_cars.remove(car)
            print(f"Car despawned, the_cars len {len(cars.the_cars)}")

    if player.ycor() >= 290: # Player has reached the top of the screen.
        score.level_up()
        player.reset_position()
        cars.speed_up()
    screen.update()
