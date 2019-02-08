#Rover XYZ Software V1.0
#by HoT - Home of Tomorrow | project at FH Kufstein
#2019
import time
import sys
import os
import RPi.GPIO as GPIO
import math

import t1
import t2
import t3
import t4
import conf
import helper
import drive
import smbus2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(conf.tasterRun, GPIO.IN)
GPIO.setup(conf.tasterStop, GPIO.IN)
if conf.pcb==False:
    GPIO.setup(conf.tasterDig1, GPIO.IN)
    GPIO.setup(conf.tasterDig2, GPIO.IN)
else:
    helper.initRotarySwitch()

drive.init()
helper.initSensorSwitch()
helper.initLEDs()
helper.LEDs[7]=1
helper.updateLED()
progDigit1=0
progDigit2=0
programmwahl = 0

while (True):
    try:
        if conf.pcb==False:
            # Programm Code lesen ohne PCB
            if GPIO.input(conf.tasterDig1):
                 progDigit1=1
            if GPIO.input(conf.tasterDig2):
                progDigit2=1
            if GPIO.input(conf.tasterRun):
                programmwahl=progDigit1*math.pow(2,0) + progDigit2*math.pow(2,1)+1
        else:
            if GPIO.input(conf.tasterRun)==False:
                programmwahl=helper.readRotarySwitch()

        #Start Programm
        if programmwahl==1:
            helper.LEDs[0]=1
            helper.updateLED()
            #t1.start()

        if programmwahl == 2:
            helper.LEDs[1]=1
            helper.updateLED()
            #t2.start()

        if programmwahl == 3:
            helper.LEDs[2]=1
            helper.updateLED()
            #t3.start()

        if programmwahl == 4:
            helper.LEDs[3]=1
            helper.updateLED()
            #t4.start()
       

        if GPIO.input(conf.tasterStop)==False:
          
            helper.LEDs[0]=0
            helper.LEDs[1]=0
            helper.LEDs[2]=0
            helper.LEDs[3]=0
            helper.updateLED()
            drive.stop()
            print("PROGRAMM EXIT")
            time.sleep(1)
            
            
            programmwahl=0
            progDigit1=0
            progDigit2=0


    except KeyboardInterrupt:
        
        programmwahl=0
        progDigit1=0
        progDigit2=0
        print("Keybord Interrupt")
        drive.stop()
        helper.LEDs[0]=0
        helper.LEDs[1]=0
        helper.LEDs[2]=0
        helper.LEDs[3]=0
        helper.updateLED()
       
        GPIO.cleanup()
        
        
        exit()