from turtle import Turtle
import random

COLORS = [
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
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 15
# CAR_WIDTH = 60
# CAR_HEIGHT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=0.5, stretch_len=3)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(-360, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
