# main game file
# entry point for the turtle crossing project
# this is just a small practice game not production code

from turtle import Screen
from player import Player
from input_state import InputState
from car_manager import CarManager
from scoreboard import Score


# screen setup
# fixed size so coords stay consistent
# black background for contrast

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")

# turn off auto refresh
# we control updates manually in the game loop

screen.tracer(0)

# lock window size
# resizing messes with collision math and positions

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)


# game objects
# each class handles its own behavior

level = Score()  # handles level text and game over
player = Player()  # the turtle you control
car_manager = CarManager()  # spawns and moves cars
input_state = InputState()  # keeps track of which keys are held


# input setup
# using key state instead of single key presses
# this allows smooth movement while holding keys

KEYS = ["Up", "Down"]

for key in KEYS:
    input_state.keys[key] = False

    # key down sets state true
    screen.onkeypress(lambda k=key: input_state.keys.__setitem__(k, True), key)

    # key up resets state
    screen.onkeyrelease(lambda k=key: input_state.keys.__setitem__(k, False), key)


# game loop state
# once false the game stops updating

game_is_on = True


def game_loop():
    # main update loop
    # uses ontimer instead of while true

    global game_is_on

    if not game_is_on:
        return

    # movement based on held keys
    if input_state.keys["Up"]:
        player.move_up()

    if input_state.keys["Down"]:
        player.move_down()

    # car logic
    car_manager.create_car()
    car_manager.move_cars()

    # collision check
    # simple distance based hit detection

    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            level.game_over()
            game_is_on = False
            return

    # level clear check
    # player reached the top

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        level.increase_level()

    # draw everything
    screen.update()

    # roughly 60 fps
    screen.ontimer(game_loop, 16)


# start listening for input and launch loop

screen.listen()
game_loop()
screen.mainloop()
