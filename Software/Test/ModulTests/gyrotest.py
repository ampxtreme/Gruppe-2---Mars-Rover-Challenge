import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO
import conf

GPIO.setmode(GPIO.BCM)
import gyro

gyro.init()

while True:
    try:
        print("ROT: {]".format(gyro.getRotation()))
        print("xyz: {}".format(gyro.getXYZ()))
    except KeyboardInterrupt:
        GPIO.cleanup()

