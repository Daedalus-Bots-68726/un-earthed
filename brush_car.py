from movement import *

def run():
    print("Running Mission 1...")
    turn(10.75)
    move(23)
    turn(-130)
    turn(177)
    move(8)
    turn(180)
    motor(1, 500, 1, "d")
    move_backwards(4)
    turn(-3)
    motor(-1, 500, 1, "d")
    move(8)
    turn(-45)
    move(23)
