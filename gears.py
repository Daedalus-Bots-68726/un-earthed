from movement import move, turn, move_backwards, motor

def run():
    move(5.8)
    turn(-90)
    move(27)
    turn(-89)
    move(0.5)
    turn(-8)
    motor(1, -2000, 1.5)
    turn(10)
    move_backwards(5)
    turn(-90)
    move(30, speed=500)