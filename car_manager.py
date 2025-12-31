from turtle import Turtle
import random

turtle_colors = [
    # Basic colors
    "black",
    "white",
    "red",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    # Extended named colors
    "gray",
    "grey",
    "lightgray",
    "darkgray",
    "orange",
    "brown",
    "pink",
    "purple",
    "violet",
    "gold",
    "silver",
    "navy",
    "skyblue",
    "turquoise",
    "teal",
    "lime",
    "olive",
    "maroon",
    "coral",
    "salmon",
    "khaki",
    "plum",
    "orchid",
    "indigo",
    "beige",
    "tan",
    "chocolate",
    # Tk color variants
    "lightblue",
    "lightgreen",
    "lightyellow",
    "lightpink",
    "darkblue",
    "darkgreen",
    "darkred",
    "darkorange",
    "darkviolet",
    "mediumblue",
    "mediumseagreen",
    "mediumorchid",
    "mediumslateblue",
]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 15


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.color(random.choice(turtle_colors))
        self.goto(x=(-230, -230))
        self.dx = 5
        self.dy = 5

    def row(self):
        for new_car in range(14):
            new_car = CarManager()
            new_car.forward(self.dx)
