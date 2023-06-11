from stanfordkarel import *
"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while not left_is_blocked():
        put_beeper_Line()
        reset_Position()
    put_beeper_Line()


def put_beeper_Line():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def reset_Position():
    turn_Around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()


def turn_Around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    run_karel_program()
