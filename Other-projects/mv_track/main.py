from gpiozero import DistanceSensor
from gpiozero.pins.native import NativePin
import time

# Set the GPIO pins for the ultrasonic sensor
trigger_pin_number = 23
echo_pin_number = 24

# Create NativePin instances for the pins
trigger_pin = NativePin(trigger_pin_number)
echo_pin = NativePin(echo_pin_number)

# Create a DistanceSensor instance
sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)

def measure_distance():
    # Measure the distance
    distance = sensor.distance * 100
    distance = round(distance, 2)
    return distance

try:
    while True:
        # Measure the distance
        dist = measure_distance()

        # Check if the object is too close
        if dist < 10:  # Adjust the threshold distance as needed
            print("Object is too close!")

        # Delay before the next measurement
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
