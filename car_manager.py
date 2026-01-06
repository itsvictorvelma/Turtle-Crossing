# car_manager.py
# handles spawning and moving enemy cars
# cars get faster each level

from turtle import Turtle
import random


# colors picked to stand out on a dark background
# nothing fancy just easy on the eyes

COLORS = [
    "cyan",
    "turquoise",
    "mediumseagreen",
    "springgreen",
    "lime",
    "gold",
    "orange",
    "coral",
    "salmon",
    "orchid",
    "plum",
    "violet",
    "mediumorchid",
    "mediumslateblue",
    "skyblue",
    "dodgerblue",
]

# base movement values
# speed ramps up as levels increase

STARTING_MOVE_DISTANCE = 4
MOVE_INCREMENT = 4


class CarManager:
    # this class manages all cars on screen
    # it doesnt represent a single car

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []  # list holding every active car

    def create_car(self):
        # spawn cars randomly so they dont appear every frame
        # lower odds means fewer cars

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()

            # stretch square into a rectangle
            new_car.shapesize(stretch_wid=0.3, stretch_len=3)

            # random color and lane
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)

            # start off screen to the left
            new_car.goto(-360, random_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        # move every car forward at the current speed

        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        # increase speed when player clears a level
        # makes the game harder over time
        self.car_speed += MOVE_INCREMENT
