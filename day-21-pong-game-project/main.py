from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)
# ^ Turns off the screen animation. Requires manually refreshing the screen (screen.update())
screen.listen()

scoreboard = Scoreboard()
paddle_r = Paddle(start_x = 380)
paddle_l = Paddle(start_x = -390)
ball = Ball()

screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")

screen.onkey(paddle_l.move_up,"w")
screen.onkey(paddle_l.move_down,"s")

game_is_on = True
while game_is_on:
    if ball.ycor() >= 290: # Ball hit top wall.
        ball.move(hit="top")
    elif ball.ycor() <= -290: # Ball hit bottom wall.
        ball.move(hit="bottom")
    elif ball.distance(paddle_r) <= 50 and ball.xcor() > 365: # Ball hit right paddle.
        ball.move(hit="paddle_r")
        ball.ball_speed_factor += ball.increase_speed_by
    elif ball.distance(paddle_l) <= 50 and ball.xcor() < -365: # Ball hit left paddle.
        ball.move(hit="paddle_l")
        ball.ball_speed_factor += ball.increase_speed_by
    elif ball.xcor() > 380: # Ball went off right side of screen.
        ball.reset_position()
        scoreboard.score("L")
    elif ball.xcor() < -380: # Ball went off left side of screen.
        ball.reset_position()
        scoreboard.score("R")
    else:
        ball.move(hit="none")

    screen.update() #Runs on a loop because screen.tracer is set to 0.

screen.exitonclick()