from movement import *

def run():
    move(17)
    turn(-145)
    for i in range(3):
        motor(1,600,1.5, "b")
        motor(-1,200,1.5, "b")
    turn(130)
    move(10.5)
    turn(25)
    move(2.5)
    turn(18)
    turn(-25)
    move(1)
    turn(-30)
    turn(25)
    move_backwards(30)
    turn(90)
    move(5)