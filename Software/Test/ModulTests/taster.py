import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO
import time
import conf

GPIO.setmode(GPIO.BCM)

GPIO.setup(conf.tasterRun, GPIO.IN)
GPIO.setup(conf.tasterStop, GPIO.IN)



while True:
    print("Ports {} {}".format(conf.tasterRun, conf.tasterStop))
    print(GPIO.input(conf.tasterRun), GPIO.input(conf.tasterStop)) 
               
     
   