from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

# Initialize hub
hub = PrimeHub()

# Motors (set reversed if wheels spin opposite directions)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)

# Distance sensor
dist_sensor = UltrasonicSensor(Port.F)

# Function to drive forward
def drive_forward(speed=300):
    left_motor.run(speed)
    right_motor.run(speed)

# Function to stop
def stuff():
    # Notes (frequencies in Hz)
    notes = [
        330, 330, 294, 330, 330, 294, 330, 370,  # Opening
        392, 370, 330, 294, 330 # Main motif repeat
    ]

    durations = [
        300, 150, 150, 300, 150, 150, 150, 150,
        150, 150, 300, 300, 600
    ]

    # Play the fanfare
    for i in range(len(notes)):
        hub.speaker.beep(notes[i], durations[i])
        wait(50)  # brief pause between notes# tiny pause between notes


def stop():
    left_motor.hold()
    right_motor.hold()

# Function to turn (left turn here)
def turn_left(speed=300, time=800):
    left_motor.run(-speed)
    right_motor.run(speed)
    wait(time)
    stop()

# Main loop
while True:
    distance = dist_sensor.distance()  # in millimeters

    if distance is not None and distance < 150:  # if object < 15 cm
        stop()
        print("Obstacle detected at", distance, "mm")
        # Back up a little
        left_motor.run_time(-300, 500)
        right_motor.run_time(-300, 500)
        # Turn left
        turn_left()
        stuff()
    else:
        drive_forward(300)

    wait(100)  # small pause