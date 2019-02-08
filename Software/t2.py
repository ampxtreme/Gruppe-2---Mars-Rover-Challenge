#Track2: Bridge
import conf
import RPi.GPIO as GPIO
import linehold
import gyro
import drive

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)
speedI = 50
speedA = 100

def start():
    init()
    while GPIO.input(conf.tasterStop):
        lane = linehold.line()
        
        if lane[0] == 1 and lane[1] == 1:
            #geradeaus
            drive.drive("L", 75, 2)
            drive.drive("R", 75, 2)
        
        elif lane[0] == 0 and lane[1] == 1:
            #nach rechts korrigieren
            drive.drive("L", speedA, 2)
            drive.drive("R", speedI, 2)
        
        elif lane[0] == 1 and lane[1] == 0:
            #nach links korrigieren
            drive.drive("L", speedI, 2)
            drive.drive("R", speedA, 2)