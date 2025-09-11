hub = PrimeHub()
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.E)
distance_sensor = UltrasonicSensor(Port.E)
WHEEL_CIRCUMFERENCE_IN = 10.86614

def dist_move(desired_distance_in_inches, speed=200, tolerance_in_inches=0.5):
    desired_mm = desired_distance_in_inches * 25.4
    tolerance_mm = tolerance_in_inches * 25.4

    print(f"Target distance from object: {desired_mm:.1f} mm")

    while True:
        current_mm = distance_sensor.distance()

        if current_mm is None:
            print("Sensor read error.")
            break

        error = current_mm - desired_mm
        print(f"Current: {current_mm:.1f} mm | Error: {error:.1f} mm")

        # If within tolerance, stop
        if abs(error) <= tolerance_mm:
            print("Reached target distance. Stopping.")
            break

        # Direction: move forward or backward
        direction = 1 if error > 0 else -1
        left.run(direction * speed)
        right.run(direction * speed)

        wait(10)

    left.stop()
    right.stop()

def move(distance_in, speed=300, kp=3, ki=0.05, kd=0.4, tolerance=5):
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



def turn(target_angle, speed=400, kp=4.5, ki=0.03, kd=0.6, tolerance=2):
    integral = 0
    last_error = 0

    while True:
        error = target_angle - hub.imu.heading()
        if abs(error) <= tolerance:
            break

        if abs(error) < 15:
            integral += error
            integral = max(min(integral, 200), -200)

        derivative = error - last_error
        correction = kp * error + ki * integral + kd * derivative
        correction = max(min(correction, speed), -speed)

        left.run(correction)
        right.run(-correction)

        last_error = error
        wait(10)

    left.hold()
    right.hold()
