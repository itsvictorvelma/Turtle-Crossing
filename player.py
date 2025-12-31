from turtle import Turtle

STARTING_POSITION = (0, 280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_HEIGHT = 20
PLAYER_WIDTH = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("orange")

    def move_up(self):
        if self.ycor() < (300 - PLAYER_HEIGHT):
            self.setheading(90)
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > (-300 + PLAYER_HEIGHT):
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() < (300 - PLAYER_WIDTH):
            self.setheading(0)
            self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() > (-300 + PLAYER_WIDTH):
            self.setheading(180)
            self.forward(MOVE_DISTANCE)
