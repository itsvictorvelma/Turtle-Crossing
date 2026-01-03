from turtle import Turtle

STARTING_POSITION = (0, 280)
MOVE_DISTANCE = 6
FINISH_LINE_Y = 280
PLAYER_HEIGHT = 20
PLAYER_WIDTH = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.color("white")
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        if self.ycor() < (300 - PLAYER_HEIGHT):
            self.setheading(90)
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > (-300 + PLAYER_HEIGHT):
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() >= 300 - PLAYER_HEIGHT:
            return True

        else:
            return False

    def go_to_start(self):
        self.goto(0, -300 + PLAYER_HEIGHT)
