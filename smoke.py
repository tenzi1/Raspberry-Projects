from time import sleep
import RPi.GPIO as GPIO
SENSOR = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarning = False
GPIO.setup(SENSOR, GPIO.IN)
while True:
    state = GPIO.INPUT(SENSOR)
    if state == False:
        print("gas deteected")
    else:
        print("gas not detected")
    sleep(0.5)