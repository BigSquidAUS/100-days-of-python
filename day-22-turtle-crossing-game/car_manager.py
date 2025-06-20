import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
MAX_CARS = 20
SPEED_VARIATION = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.the_cars = []
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.rand_speed_variance = random.randint(1,SPEED_VARIATION)
        self.speed = STARTING_MOVE_DISTANCE + self.rand_speed_variance

    def generate_car(self):
        rand_y = random.randint(-250, 270)
        spawn_chance = random.randint(0,100)

        if len(self.the_cars) >= MAX_CARS:
            pass

        elif spawn_chance > 75:
            new_car = CarManager()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.goto(280,rand_y)
            new_car.showturtle()
            #print(new_car.ycor())
            self.the_cars.append(new_car)

    def move_car(self, current_level):
        self.new_speed = current_level * MOVE_INCREMENT + self.speed
        self.new_x = self.xcor() - self.new_speed
        self.goto(self.new_x,self.ycor())

    def speed_up(self):
        self.speed += MOVE_INCREMENT
        #print(f"Speed: {self.speed}")

    def car_collision_area(self):
        return self.xcor() - 20, self.ycor()