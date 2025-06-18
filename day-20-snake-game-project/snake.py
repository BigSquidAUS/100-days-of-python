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
        self.grid = 20
        self.can_turn = True
        #can_turn used to stop rapid key presses from causing illegal moves.
        #only 1 move per "move" cycle is allowed using this flag.

    def create_snake(self):
        for segment in range(STARTING_LENGTH):
            pos = int(-segment * 22),0
            self.add_segment(pos)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.pu()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.the_snake.append(snake_segment)

    def extend(self):
        #Add new segment to the snake.
        self.add_segment(self.the_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.the_snake) - 1, 0, -1):
            new_x = self.the_snake[seg_num - 1].xcor()
            new_y = self.the_snake[seg_num - 1].ycor()
            self.the_snake[seg_num].goto(new_x, new_y)
        self.head.forward(self.grid)
        self.can_turn = True

    def up(self):
        if self.head.heading() != DOWN and self.can_turn:
            self.head.setheading(UP)
            self.can_turn = False


    def down(self):
        if self.head.heading() != UP and self.can_turn:
            self.head.setheading(DOWN)
            self.can_turn = False

    def left(self):
        if self.head.heading() != RIGHT and self.can_turn:
            self.head.setheading(LEFT)
            self.can_turn = False

    def right(self):
        if self.head.heading() != LEFT and self.can_turn:
            self.head.setheading(RIGHT)
            self.can_turn = False