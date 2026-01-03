from turtle import Screen
from player import Player
from input_state import InputState
from car_manager import CarManager

# SCREEN SETUP

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")

# Turn off auto refresh

screen.tracer(0)

# Disable window resizing (keeps collision math from drifting)

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)

# PLAYER

player = Player()

# CarManager

car_manager = CarManager()

# MOVEMENT

input_state = InputState()

KEYS = ["Up", "Down"]

for key in KEYS:
    input_state.keys[key] = False
    screen.onkeypress(lambda k=key: input_state.keys.__setitem__(k, True), key)
    screen.onkeyrelease(lambda k=key: input_state.keys.__setitem__(k, False), key)

# GAME LOOP

game_is_on = True


def game_loop():
    global game_is_on

    if not game_is_on:
        return

    if input_state.keys["Up"]:
        player.move_up()

    if input_state.keys["Down"]:
        player.move_down()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect car collision

    for car in car_manager.all_cars:
        if car.distance(player) < 17:
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()

    screen.update()
    screen.ontimer(game_loop, 16)


screen.listen()
game_loop()
screen.mainloop()
