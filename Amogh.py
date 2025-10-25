from movement import *

def run():
    move(17)
    turn(-147)
    for i in range(4):
        motor(1,600,1, "b")
        motor(-1,600,1, "b")
    turn(130)
    move(10.5)
    turn(25)
    move(2.5)
    turn(30)
    turn(-30)
    move(1)
    turn(-28)
    turn(25)
    move_backwards(2)
    turn(-90)
    move(18)
    turn(-50)
    move(25)
    turn(30)
    move(25)
