import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
import conf
import helper
import time

helper.initLEDs();

GPIO.output(conf.programmLED1, True)
GPIO.output(conf.programmLED2, True)
GPIO.output(conf.programmLED3, True)
GPIO.output(conf.programmLED4, True)

GPIO.output(conf.programmLED1, True)
time.sleep(1)
GPIO.output(conf.programmLED2, True)
time.sleep(1)
GPIO.output(conf.programmLED3, True)
time.sleep(1)
GPIO.output(conf.programmLED4, True)
time.sleep(1)
Print("Test end")