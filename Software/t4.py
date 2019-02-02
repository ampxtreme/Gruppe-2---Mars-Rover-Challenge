#Track4: Rock'n'Roll
import sonic
import conf
import cam
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

def start():
    #init()
    while GPIO.input(conf.tasterStop) == False:
        while sonic.read("test") >= conf.camDistance:
            print("geradeaus")
            
        obstacle = cam.objectDetection()
        print(obstacle)
        areaL = 0
        areaR = 0
        for element in obstacle:
            ocor = obstacle[element]
            if ocor[0] >= 140:
                areaR += (ocor[2]*ocor[3])
            else:
                areaL += (ocor[2]+ocor[3])
        
        if areaL > areaR:
            print("nach rechts fahren")
        else:
            print("nach links fahren")
    

def init():

    return

def Texit():
    
    return