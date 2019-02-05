import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO
import conf

GPIO.setmode(GPIO.BCM)
import linehold

while True:
    try:

        print(linehold.line())


    except KeyboardInterrupt:
        GPIO.cleanup()
