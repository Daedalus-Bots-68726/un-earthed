from movement import *

def run():
    print("hello")
    move(6.4)
    turn(-90)
    move(26.75)
    turn(-90)
    move(1)
    motor(1, -2000, 2, "d")
    turn(10)
    move_backwards(5)
    turn(16)
    move_backwards(4.7)
    motor(1, 200, 1, "b")
    motor(-1, 200, 1.5, "b")
    move(5)
    turn(-125)
    move(25)
    turn(120)
    move_backwards(2)
    for i in range(3):
        motor(1, 200, 1.5, "b")
        motor(-1,200,1.5,"b")
    turn(140)
    move(4)
    turn(10)
    move(10)
    turn(25)
    turn(-25)
    move(-0.75)
    turn(-100,100)


