from movement import *

def run():
    move(17)
    turn(-147)
    for i in range(4):
        motor(1,600,1, "b")
        motor(-1,600,1, "b")
    # Silo is done
    turn(130)
    move(10.5)
    turn(25)
    move(3.5)
    turn(25, 500)
    # Forge is done
    turn(-30)
    move(0.2)
    turn(-20)
    # Who Lived Here is done
    turn(20)
    move_backwards(3.5)
    turn(-90)
    move_backwards(16)
    turn(-90)
    move_backwards(4.5)
    turn(-60)
    motor(1, 80, 1, "b")
    turn(75)
    motor(-1, 100, 1, "b")
    turn(-75)
    move(300)