from movement import *

def run():
    print("Running Mission 1...")
    turn(3.66)
    motor(-1, 27, 1, "d")
    move(25)
    move_backwards(10)
    move(8)
    motor(-1, 500, 1, "d")
    turn(40)
    move(14)
    motor(1, 250, 0.45, "d")
    move_backwards(14)
    turn(-40)
    move_backwards(23)
