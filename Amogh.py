from movement import *

def run():
    move(17)
    turn(-147)
    for i in range(4):
        motor(1,600,1.5, "b")
        motor(-1,600,1.5, "b")
    turn(130)
    move(10.5)
    turn(25)
    move(3)
    turn(25)
    turn(-25)
    move(1.5)
    turn(-28)
    turn(25)
    move_backwards(2)
    turn(-90)
    move(17)
    turn(-50)
    move(20)
    turn(30)
    move(1000)
