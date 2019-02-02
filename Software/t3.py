#Track3: Let it rain
import conf
import cam
import RPi.GPIO as GPIO
from simple_pid import PID

Kp = 1
Ki = 0.1
Kd = 0.05
setpoint = 1

pid = PID(Kp, Ki, Kd, setpoint)

GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.tasterStop, GPIO.IN)

def start():
      
    while GPIO.input(conf.tasterStop) == False:
        line = cam.lineDetection()
        try:
            difference = int(line[2])
        except TypeError:
            continue
        control = pid(difference)
        print (control)       
        
        
def init():
    return
def Texit():
    
    return
