BUTTON_PIN = 14
LED_PIN = 2
SERVO_PIN = 25


import sys
import RPi.GPIO as GPIO
from time import sleep
import cv2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)
cam = cv2.VideoCapture(0)
print("push 3 times")
GPIO.output(LED_PIN, False)
click_cnt = 0
while click_cnt < 3:
    GPIO.output(LED_PIN, False)
    inputValue = GPIO.input(BUTTON_PIN)
    if(inputValue == True):
        GPIO.output(LED_PIN, True)
        click_cnt = click_cnt + 1
        print(click_cnt)
    sleep(1)
while(True):
    ret, img = cam.read()
    cv2.imshow('my_cam', img)
    if cv2.waitKey(10) == 27:
	    break
cam.release()
cv2.destroyAllWindows()
print("done")
GPIO.cleanup()
