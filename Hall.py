import os
import RPi.GPIO as GPIO
import time

hal = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(hal, GPIO.OUT)
GPIO.output(hal, 1)

def HL(sig):
    if GPIO.GETRISE() == True:
        hal = True
        
