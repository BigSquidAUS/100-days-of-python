from turtle import Turtle

STARTING_LENGTH = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.the_snake = []
        self.create_snake()
        self.head = self.the_snake[0] # The head of the snake.

    def create_snake(self):
        for segment in range(STARTING_LENGTH):
            snake_segment = Turtle(shape="square")
            snake_segment.pu()
            snake_segment.color("white")
            snake_segment.setx((-segment * 22))
            self.the_snake.append(snake_segment)

    def move(self, grid):
        for seg_num in range(len(self.the_snake) - 1, 0, -1):
            new_x = self.the_snake[seg_num - 1].xcor()
            new_y = self.the_snake[seg_num - 1].ycor()
            self.the_snake[seg_num].goto(new_x, new_y)
        self.head.forward(grid)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)