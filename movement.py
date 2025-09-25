from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = PrimeHub()
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.E)
motor_d = Motor(Port.D)
motor_b = Motor(Port.B)

WHEEL_CIRCUMFERENCE_IN = 10.86614

def move(distance_in, speed=300):
    kp = max(1.5, 4.0 - speed / 300)  # keep proportional always > 1.5
    ki = max(0.02, 0.1 - speed / 5000)  # let integral do a bit more
    kd = 0.2 + speed / 1200  # gentler growth with speed
    tolerance = min(6, max(2, speed // 150))
    degrees_to_run = (distance_in / WHEEL_CIRCUMFERENCE_IN) * 360
    hub.imu.reset_heading(0)
    left.reset_angle(0)
    right.reset_angle(0)

    integral = 0
    last_error = 0

    while True:
        avg_degrees = (abs(left.angle()) + abs(right.angle())) / 2
        if avg_degrees >= degrees_to_run - tolerance:
            break
        raw_heading = hub.imu.heading()
        error = (raw_heading + 180) % 360 - 180

        if abs(error) < 10:
            integral += error
            integral = max(min(integral, 100), -100)

        derivative = error - last_error
        correction = kp * error + ki * integral + kd * derivative

        remaining = degrees_to_run - avg_degrees
        if remaining < 50:
            speed_adj = max(100, int(speed * (remaining / 50)))
        else:
            speed_adj = speed

        left.run(speed_adj - correction)
        right.run(speed_adj + correction)

        last_error = error
        wait(10)

    left.hold()
    right.hold()

def move_backwards(distance_in, speed=300, kp=3, ki=0.05, kd=0.4, tolerance=5):
    degrees_to_run = (distance_in / WHEEL_CIRCUMFERENCE_IN) * 360
    hub.imu.reset_heading(0)
    left.reset_angle(0)
    right.reset_angle(0)

    integral = 0
    last_error = 0

    while True:
        avg_degrees = (abs(left.angle()) + abs(right.angle())) / 2
        if avg_degrees >= degrees_to_run - tolerance:
            break

        error = hub.imu.heading()

        if abs(error) < 10:
            integral += error
            integral = max(min(integral, 100), -100)

        derivative = error - last_error
        correction = kp * error + ki * integral + kd * derivative

        remaining = degrees_to_run - avg_degrees
        if remaining < 50:
            speed_adj = max(100, int(speed * (remaining / 50)))
        else:
            speed_adj = speed

        # Flip direction for backwards AND flip correction
        left.run(-(speed_adj + correction))
        right.run(-(speed_adj - correction))

        last_error = error
        wait(10)

    left.hold()
    right.hold()

def normalize_angle(angle):
    """Wraps any angle into the range [-180, 180]."""
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle


def turn(target_angle, speed=400, kp=4.5, ki=0.03, kd=0.6, tolerance=1):
    hub.imu.reset_heading(0)
    integral = 0
    last_error = 0

    while True:
        # Calculate error and normalize it
        error = normalize_angle(target_angle - hub.imu.heading())

        # Stop if close enough
        if abs(error) <= tolerance:
            break

        # Integrate only when close (prevents runaway)
        if abs(error) < 15:
            integral += error
            integral = max(min(integral, 200), -200)

        derivative = error - last_error
        correction = kp * error + ki * integral + kd * derivative

        # Scale down correction if we're close
        if abs(error) < 10:
            correction *= 0.3

        # Limit correction
        correction = max(min(correction, speed), -speed)

        left.run(correction)
        right.run(-correction)

        last_error = error
        wait(10)

    # Hold final position
    left.hold()
    right.hold()

def motor(direction, speed, time, motor):
    speed = direction * speed
    if motor == "b":
        motor_b.run(speed)
        wait(time * 1000)
        motor_b.stop()

    if motor == "d":
        motor_d.run_time(speed, time * 1000)

