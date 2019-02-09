#Track3: Let it rain
import conf
import cam
import RPi.GPIO as GPIO
from simple_pid import PID
import drive

Kp = 2
Ki = 0
Kd = 0
setpoint = 0

pid = PID(Kp, Ki, Kd, setpoint)
pid.output_limits = (0, 100)

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

def start():
      
    while GPIO.input(conf.tasterStop):
        line = cam.lineDetection()
        try:
            difference = int(line[2])
        except TypeError:
            continue
        control = pid(difference)

        if difference>=0:
            
            drive.drive("R",50 -control/2)
            drive.drive("L",50 +control/2)
        else:
            drive.drive("L",50 -control/2)
            drive.drive("R",50 +control/2) 

        if conf.debug:
            print ("T3 Control:{}". format(control))
        
