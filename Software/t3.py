#Track3: Let it rain
import conf
import cam
import RPi.GPIO as GPIO
from simple_pid import PID
import drive

Kp = 1
Ki = 0.1
Kd = 0.05
setpoint = 1

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
        print(control)
        control2=control

        if control >= 100:
            control2=100

        delta = 100-control
        
        if delta <= 0:
            delta = 0
        
        print(control2)
        print(delta)
    
        drive.drive("L", control2)
        drive.drive("R", delta)

        if conf.debug:
            print ("T3 Control:{}, {}". format(control, delta))
        
        
def init():
    return
def Texit():
    drive.stop()
    return
