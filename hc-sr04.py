TRIG = 23
ECHO = 24

import sys
from hcsr04sensor import sensor
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
for i in range(5):
    value = sensor.Measurment(TRIG, ECHO)
    raw_dist = value.raw_distance()
    distance_cm = value.distance_metric(raw_dist)
    print(i, "\t", distance_cm)
    sleep(0.3)
print("done")
GPIO.cleanup()