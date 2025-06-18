import time
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
grid_size = 20

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    #Add scoreboard
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.extend()

    #Detect collision with wall:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    #Detect collision with tail:
    for segment in snake.the_snake[1:]: # List slicing. Position 1 to the end of the list. (ie: Skip the head of the snake)
        if snake.head.distance(segment) < 5:
            game_is_on = False
            print("Collided with tail")
            score.game_over()

screen.exitonclick()