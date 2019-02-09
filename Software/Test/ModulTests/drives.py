import  sys
sys.path.insert(0, '../../')
import RPi.GPIO as GPIO
import conf
import time

GPIO.setmode(GPIO.BCM)
import drive
print(drive.BANK0, drive.BANK1, drive.BANK2)

print("init drives")

drive.init()

def leftTurn(time=5):
    drive.drive("L", 50, 2, 0)
    drive.drive("R", 50, 2, 1)
    time.sleep(time)
    drive.stop()

#0-5
print(drive.BANK0, drive.BANK1, drive.BANK2)

# Auskommentieren, was man testen mag!
#drive.drive("L", 100,3)
#drive.drive("R", 50,3)
# mortot, speed lvl, richtung 0,1
#drive.setMotor(5, 2, 0 )



print(drive.BANK0, drive.BANK1, drive.BANK2)
#drive.testpwm()

drive.test()
#drive.set
#drive.testpwm()

time.sleep(4)
#leftTurn(1)
drive.setSpeedLevel(0, 0)
drive.PWMR.stop()
drive.PWML.stop()

GPIO.cleanup()
