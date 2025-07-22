def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while True:
        if wall_on_right():
            move()
        else:
            break
    turn_right()
    move()
    turn_right()
    while True:
        if front_is_clear():
            move()
        else:
            turn_left()
            break


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# Solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


