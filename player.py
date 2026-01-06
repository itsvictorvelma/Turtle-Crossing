# player.py
# controls the player turtle
# movement is vertical only just like frogger

from turtle import Turtle

# constants for positioning and bounds
# keeps magic numbers out of the methods

STARTING_POSITION = (0, 280)
MOVE_DISTANCE = 6
FINISH_LINE_Y = 280
PLAYER_HEIGHT = 20
PLAYER_WIDTH = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()

        # basic turtle setup
        self.shape("turtle")

        # shrink the turtle a bit so collisions feel fair
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)

        self.penup()
        self.color("white")

        # always facing up by default
        self.setheading(90)

        self.go_to_start()

    def move_up(self):
        # move up but dont let player leave the screen
        # top boundary check

        if self.ycor() < (300 - PLAYER_HEIGHT):
            self.setheading(90)
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        # move down with bottom boundary check

        if self.ycor() > (-300 + PLAYER_HEIGHT):
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        # check if player reached the top
        # used to trigger next level

        if self.ycor() >= 300 - PLAYER_HEIGHT:
            return True
        else:
            return False

    def go_to_start(self):
        # reset player back to the bottom
        # called at game start and after each level

        self.goto(0, -300 + PLAYER_HEIGHT)
