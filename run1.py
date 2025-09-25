from movement import move, turn, move_backwards, motor

def run():
    move(6.4)
    turn(-90)
    move(27)
    turn(-89)
    move(0.5)
    turn(-5)
    motor(1, -2000, 2, "d")
    turn(-2)
    turn(10)
    move_backwards(5)
    turn(25)
    move_backwards(4.7)
    motor(1, 200, 1, "b")
    motor(-1, 200, 1.5, "b")

