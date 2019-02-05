import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO
import conf

GPIO.setmode(GPIO.BCM)
import drive


print("init drives")
drive.init()

def leftTurn(time=5)
    drive.drive("L", 50, 2, 0)
    drive.drive("R", 50, 2, 1)
    time.sleep(time)
    drive.stop()

#0-5

# Auskommentieren, was man testen mag!

# mortot, speed lvl, richtung 0,1
drive.setMotor(0, 2, 0 )

#drive.test()

#drive.testpwm()

#leftTurn(1)

