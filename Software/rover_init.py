import time
import sys
import os
import RPi.GPIO as GPIO

#import T1
#import T2
import t3
import t4
import conf
import math
import helper

GPIO.setmode(GPIO.BCM)

GPIO.setup(conf.tasterRun, GPIO.IN)
GPIO.setup(conf.tasterStop, GPIO.IN)
GPIO.setup(conf.tasterDig1, GPIO.IN)
GPIO.setup(conf.tasterDig2, GPIO.IN)
GPIO.setup(conf.intLED, GPIO.OUT)
GPIO.setup(conf.programmLED1, GPIO.OUT)
GPIO.setup(conf.programmLED2, GPIO.OUT)
GPIO.setup(conf.programmLED3, GPIO.OUT)
GPIO.setup(conf.programmLED4, GPIO.OUT)
helper.initSensorSwitch()
GPIO.output(conf.intLED, True)

progDigit1=0
progDigit2=0
programmwahl = 0

while (True):
    try:

        # Programm Code lesen
        if GPIO.input(conf.tasterDig1):
            progDigit1=1
        if GPIO.input(conf.tasterDig2):
            progDigit2=1
        if GPIO.input(conf.tasterRun):
            programmwahl=progDigit1*math.pow(2,0) + progDigit2*math.pow(2,1)+1

        #Start Programm
        if programmwahl==1:
            GPIO.output(conf.programmLED1, True)

        if programmwahl == 2:
            GPIO.output(conf.programmLED2, True)

        if programmwahl == 3:
            GPIO.output(conf.programmLED3, True)
            t3.start()

        if programmwahl == 4:
            GPIO.output(conf.programmLED4, True)
            t4.start()
       

        if GPIO.input(conf.tasterStop):
          
            GPIO.output(conf.programmLED1, False)
            GPIO.output(conf.programmLED2, False)
            GPIO.output(conf.programmLED3, False)
            GPIO.output(conf.programmLED4, False)
            print("PROGRAMM EXIT")
            time.sleep(1)
            
            
            programmwahl=0
            progDigit1=0
            progDigit2=0


    except KeyboardInterrupt:
        
        programmwahl=0
        progDigit1=0
        progDigit2=0
        GPIO.output(conf.programmLED1, False)
        GPIO.output(conf.programmLED2, False)
        GPIO.output(conf.programmLED3, False)
        GPIO.output(conf.programmLED4, False)
        GPIO.cleanup()
        
        
        exit()