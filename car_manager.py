from turtle import Turtle
import random

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
STARTING_MOVE_DISTANCE = 4
MOVE_INCREMENT = 7
# CAR_WIDTH = 60
# CAR_HEIGHT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=0.3, stretch_len=3)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(-360, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
