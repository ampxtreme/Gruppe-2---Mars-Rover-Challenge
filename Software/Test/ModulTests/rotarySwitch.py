import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO
import conf

GPIO.setmode(GPIO.BCM)
import helper

helper.initRotarySwitch()

while True:
    try:

    print(helper.readRotarySwitch())

    except KeyboardInterrupt:
        GPIO.cleanup()

