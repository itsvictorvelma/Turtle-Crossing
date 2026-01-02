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

KEYS = ["Up", "Down", "Left", "Right"]

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

    car_manager.create_car()
    car_manager.move_cars()

    if input_state.keys["Up"]:
        player.move_up()

    if input_state.keys["Down"]:
        player.move_down()

    if input_state.keys["Right"]:
        player.move_right()

    if input_state.keys["Left"]:
        player.move_left()

    # Detect car collision

    screen.update()
    screen.ontimer(game_loop, 16)


screen.listen()
game_loop()
screen.mainloop()
