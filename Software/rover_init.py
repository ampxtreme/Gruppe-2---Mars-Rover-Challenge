import time
import sys
import os
import RPi.GPIO as GPIO

import T1
import T2
import conf;
import math;

GPIO.setmode(GPIO.BCM)

int start_stop = 0
programmwahl = 0



GPIO.setup(conf.tasterRun, GPIO.IN)
GPIO.setup(conf.tasterDig1, GPIO.IN)
GPIO.setup(conf.tasterDig2, GPIO.IN)
GPIO.setup(conf.intLED, GPIO.OUT)

GPIO.output(conf.intLED, True)

progDigit1=0;
progDigit2=0;

while (start_stop == 0):

    // Programm Code lesen
    if GPIO.input(conf.tasterDig1):
        progDigit1=1;
    if GPIO.input(conf.tasterDig2):
        progDigit2=1;
    if GPIO.input(conf.tasterRun) and start_stop==0:
        start_stop==1;
        programmwahl=progDigit1**0 + progDigit2**1

        //Start Programm
        if programmwahl==1:
            GPIO.output(conf.programmLED1);

        if programmwahl == 2:
            GPIO.output(conf.programmLED2);

        if programmwahl == 3
            GPIO.output(conf.programmLED3;

        if programmwahl == 4:
            GPIO.output(conf.programmLED4);


    if GPIO.input(conf.tasterRun)==True and start_stop == 1:
        start_stop==0;
        programmwahl=0;
        progDigit1=0;
        progDigit2=0;
        GPIO.output(conf.programmLED1, False);
        GPIO.output(conf.programmLED2, False);
        GPIO.output(conf.programmLED3, False);
        GPIO.output(conf.programmLED4, False);