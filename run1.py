from movement import move, turn, move_backwards, motor

def run():

    move(5.9)
    turn(-90)
    move(27)
    turn(-89)
    move(0.5)
    turn(-8)
    motor(1, -2000, 1.5, "d")
    turn(10)
    move_backwards(5)
    turn(25)
    move_backwards(4.7)
    motor(1, 200, 1, "b")
    motor(-1, 200, 1.5, "b")
    move(5.9000001)
    turn(23)
    move_backwards(0.21)
    motor(1, 200, 2, "b")
