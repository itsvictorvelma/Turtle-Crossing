# scoreboard.py
# handles level display and game over text
# kept simple on purpose

from turtle import Turtle


# text settings
# courier is easy to read and consistent

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 0

        self.hideturtle()
        self.penup()

        # top left-ish position
        # adjusted so text doesnt clip the screen
        self.goto(-210, 240)

        self.pencolor("white")

        # start at level 1
        self.increase_level()

    def increase_level(self):
        # clears old text and writes the new level
        # called every time player crosses successfully

        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # display final message in the center
        # freezes level count

        self.clear()
        self.goto(0, 0)
        self.write(
            f"GAME OVER... LEVEL {self.level}",
            align=ALIGNMENT,
            font=FONT,
        )
