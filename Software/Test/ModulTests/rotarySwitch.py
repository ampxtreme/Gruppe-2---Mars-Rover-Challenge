import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO
import conf

GPIO.setmode(GPIO.BCM)
import helper

helper.initRotarySwitch()
#GPIO.setup(25, GPIO.IN)#
#GPIO.setup(27, GPIO.IN)
#GPIO.setup(28, GPIO.IN)
#GPIO.setup(29, GPIO.IN)
while True:
    try:
        print(helper.readRotarySwitch())

    except KeyboardInterrupt:
        GPIO.cleanup()

