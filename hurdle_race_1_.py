def reacher():
    for i in range(6):
        if i == 0:
            move()
            turn_left()
            move()
            turn_right()
            move()
            turn_right()
            move()
        elif i != 0:
            turn_left()
            move()
            turn_left()
            move()
            turn_right()
            move()
            turn_right()
            move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


reacher()

# Hurdle Four
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front() and right_is_clear():
        turn_right()
    if wall_in_front():
        turn_left()
    if wall_in_front() and not right_is_clear():
        turn_right()
    if not wall_in_front() and right_is_clear():
        turn_right()
        move()
    if not front_is_clear:
        turn_left()
        turn_left()
        move()

    if right_is_clear():
        turn_right()
        move()

    move()
