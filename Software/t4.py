#Track4: Rock'n'Roll
import sonic
import conf
import cam
import gyro
import drive
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

corrF=30
speed=40
def start():
    while GPIO.input(conf.tasterStop):
        sonicarray = [sonic.read("L"), sonic.read("M"), sonic.read("R")]
        
        
        if sonicarray[0] or sonicarray[1] or sonicarray[2]:
            correction()
        else:
            drive.drive("L",speed)
            drive.drive("R",speed)
        


def correction():
    sonicarray = [sonic.read("L"), sonic.read("M"), sonic.read("R")]
    obstacle = cam.objectDetection()
    areaL = 0
    areaR = 0
    factor = 1
    for element in obstacle:
        ocor = obstacle[element]
        if ocor[0] >= 140:
            areaR += (ocor[2]*ocor[3])
        else:
            areaL += (ocor[2]+ocor[3])
        
    if areaL > areaR and sonicarray != [0, 0, 0]:
        #nach rechts fahren abhängig von flächengröße
        factor = areaR/areaL
        drive.drive("L",speed + corrF*factor)
        drive.drive("R",speed - corrF*factor)
        
            
    if areaR > areaL and sonicarray != [0, 0, 0]:
        #nach links fahren abhängig von flächengröße
        factor = areaL/areaR
        drive.drive("R",50 + corrF*factor)
        drive.drive("L",50 - corrF*factor)


def test():
    while GPIO.input(conf.tasterStop) == False:
        if sonic.read("test") == 0:
            print("geradeaus")
        
        if sonic.read("test") == 1: 
            return