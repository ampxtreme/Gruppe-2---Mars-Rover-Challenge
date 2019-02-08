#Track4: Rock'n'Roll
import sonic
import conf
import cam
import gyro
import drive
import RPi.GPIO as GPIO
from simple_pid import PID

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

Kp = 1
Ki = 0.1
Kd = 0.05
setpoint = 1 #gyro nullpunkt

pid = PID(Kp, Ki, Kd, setpoint)
pid.output_limits = (0, 100)

def start():
    while GPIO.input(conf.tasterStop):
        sonicarray = [sonic.read("L"), sonic.read("M"), sonic.read("R")]
        #gyro abfragen
        
        if sonicarray == [0, 0, 0]:
            #regeln auf gyro mitte
            #difference = gyronullpunkt - gyro
            #control = pid(difference)
            
        elif (sonicarray == [1, 0, 0]) or (sonicarray == [0, 0, 1]) or (sonicarray == [1, 1, 0]) or (sonicarray == [0, 1, 1]):
            #stehen bleiben
            correction()
          
            
        elif sonicarray == [1, 1, 1]:
            #stehen bleiben
                        
            correction()
            
            #links/rechts von mitte? (gyro)
            #circleRoutine()


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
        factor = areaL/areaR
        
            
    if areaR > areaL and sonicarray != [0, 0, 0]:
        #nach links fahren abhängig von flächengröße
        factor = areaR/areaL
    

def circleRoutine(pos):
    if pos == "L":
        pass
    
    if pos == "R":
        pass

def test():
    while GPIO.input(conf.tasterStop) == False:
        if sonic.read("test") == 0:
            print("geradeaus")
        
        if sonic.read("test") == 1: 
            