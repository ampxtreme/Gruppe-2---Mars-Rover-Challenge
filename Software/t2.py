#Track2: Bridge
import conf
import RPi.GPIO as GPIO
import linehold

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

def start():
    init()
    while GPIO.input(conf.tasterStop) == False:
        pass
    return True





