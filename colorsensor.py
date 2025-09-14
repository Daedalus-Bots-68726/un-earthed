from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait
sensor = ColorSensor(Port.B)

def color():
    # Main loop to detect and print color
    while True:
        detected = sensor.color()
        reflection = sensor.reflection()  # Brightness 0–100

        if reflection < 15:
            detected="Color.BLACK"

        print("Detected:", detected, "| Reflection:", reflection)

        wait(1000)
