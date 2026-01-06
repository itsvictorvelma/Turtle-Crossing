# input_state.py
# tracks which keys are currently being held down
# used instead of single keypress events


class InputState:
    def __init__(self):
        # dictionary maps key names to pressed state
        # true while key is held false when released

        self.keys = {
            "Up": False,
            "Down": False,
            "Left": False,
            "Right": False,
        }
