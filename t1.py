#Track1: Ramp module
import conf
import RPi.GPIO as GPIO
import drive


GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

def start():
    while GPIO.input(conf.tasterStop) == False:
        drive.drive("L")
        drive.drive("R")

    return True



