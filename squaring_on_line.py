# Import Pybricks
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait

# Initialize hub
hub = PrimeHub()

# Motors (adjust ports as needed)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

# Two downward-facing color sensors
left_sensor = ColorSensor(Port.C)
right_sensor = ColorSensor(Port.D)

def square_on_line(speed=150):
    """
    Move forward until one sensor sees black,
    then stop that motor and keep the other going
    until both sensors are on black.
    """
    left_done = False
    right_done = False

    # Step 1: Move forward until one sensor hits black
    left_motor.run(speed)
    right_motor.run(speed)

    while not (left_done or right_done):
        if left_sensor.color() == Color.BLACK:
            left_motor.stop()
            left_done = True
        if right_sensor.color() == Color.BLACK:
            right_motor.stop()
            right_done = True
        wait(10)

    # Step 2: Keep moving the other motor until it also finds black
    while not (left_done and right_done):
        if not left_done:
            left_motor.run(speed)
            if left_sensor.color() == Color.BLACK:
                left_motor.stop()
                left_done = True
        if not right_done:
            right_motor.run(speed)
            if right_sensor.color() == Color.BLACK:
                right_motor.stop()
                right_done = True
        wait(10)

    hub.speaker.beep()

# Example usage
square_on_line(speed=200)
