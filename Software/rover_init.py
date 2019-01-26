import time
import sys
import os
import RPi.GPIO as GPIO

import T1
import T2

GPIO.setmode(GPIO.BCM)

start_stop = 0
programmwahl = None

taster_start = 1
taster_programmwahl = 2
led_initfertig = 3

GPIO.setup(taster_start, GPIO.IN)
GPIO.setup(taster_programmwahl, GPIO.IN)
GPIO.setup(led_initfertig, GPIO.OUT)

GPIO.output(led_initfertig, True)

while (start_stop == 0):

    if GPIO.input(taster_programmwahl) == False:
        programmwahl = 1
    else:
        programmwahl = 0

    if GPIO.input(taster_start) == False:
        start_stop = 1





