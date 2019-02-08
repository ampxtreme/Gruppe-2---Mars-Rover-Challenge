#Linehold Sensor Module
import conf
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.lineVL, GPIO.IN)
GPIO.setup(conf.lineVR, GPIO.IN)


def line():
    linearrayV = [0, 0]
    
    if GPIO.input(conf.lineVL) == True:
        linearrayV[0] = 1
    else:
        linearrayV[0] = 0
        
    if GPIO.input(conf.lineVR) == True:
        linearrayV[1] = 1
    else:
        linearrayV[1] = 0
    
    if conf.debug:
        print("LineL: {} LineR: {} ".format(linearrayV[0], linearrayV[1]))
    
    return linearrayV