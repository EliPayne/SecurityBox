import os
import RPi.GPIO as GPIO
import time

relay = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, 1)

def Open():
    GPIO.output(relay, 0)
    print("Opening Lock")
    
def Close():
    GPIO.output(relay, 1)
    print("Closing Lock")