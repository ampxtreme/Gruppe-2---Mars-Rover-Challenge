import conf
import time
import smbus2
import helper
import RPi.GPIO as GPIO


# [motor1P, motor1Rot, motor1Speed1, motor1Speed2],
GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.pwm0, GPIO.OUT)
GPIO.setup(conf.pwm1, GPIO.OUT)

PWML = GPIO.PWM(conf.pwm0, 1500)
PWMR = GPIO.PWM(conf.pwm1, 1500)

BUS=smbus2.SMBus(0)  # bus = smbus.SMBus(0) fuer Revision 1

#     motor  on 0-5 power0 , power 1 Left
BANK1=[0, 0, 0, 0, 0, 0, 0, 0]

#     motor  direction 0-5, power0 , power 1 Left
BANK2=[0, 0, 0, 0, 0, 0, 0, 0]

def init(): 

    intspeed=1
    BUS.write_byte_data(0x21, 0x06, 0b00000000)
    BUS.write_byte_data(0x21, 0x02, 0b11111111)
    
    BUS.write_byte_data(0x20, 0x06, 0b11111111)
    BUS.write_byte_data(0x20, 0x07, 0b11111111)
    
    PWML.start(100)
    PWMR.start(100)
    for m in range(0, 5):
        setSpeedLevel(m,intspeed)
        BANK1[m]=1
        i2cUpdate()
        time.sleep(0.5)
        setSpeedLevel(m, 0)


def test():
    for m in range(0, 5):
        for speed in range(1, 3):
            setMotor(m, speed, 1)
            time.sleep(1)
        setMotor(m, 0, 0)
        
def i2cUpdate():
    BUS.write_byte_data(0x20, 0x02, helper.convertStatusToI2c(BANK1))
    BUS.write_byte_data(0x20, 0x03, helper.convertStatusToI2c(BANK2))

def testpwm(speed=3):
    drive("R", 0, speed)
    drive("L", 0, speed)
    for i in range(0, 100):
        PWMR.ChangeDutyCycle(i)
        PWML.ChangeDutyCycle(i)
        time.sleep(0.2)
        print("{} on Lvl {}".format(i, SpeedLevel))


def speed(s):

    if s==1:
        return (0, 1)
    if s==2:
        return (1, 0)
    if s==3:
        return (1, 1)
    return (0, 0)

def setSpeedLevel(m, level):
    intspeed = speed(level)
    if m <= 3:
        BANK1[6]= intspeed[0]
        BANK1[7]= intspeed[1]
    else:
        BANK2[6]= intspeed[0]
        BANK2[7]= intspeed[1]
    i2cUpdate()

def setMotor(m, PowerLvl=3, richtung=0):
    setSpeedLevel(m, PowerLvl)
    BANK2[m]=richtung
    i2cUpdate()
    return

def drive(seite, dutyCycle=100, PowerLvl=3, richtung=1):
    mstart=0;
    if seite== "R":
        mstart=4;
        PWMR.ChangeDutyCycle(dutyCycle)
    else:
        PWML.ChangeDutyCycle(dutyCycle)

    for m in range(mstart,mstart+3):
        print(m)
        setSpeedLevel(m,PowerLvl)
        BUS.write_byte_data(conf.motors[m][1][0], conf.motors[m][1][1], richtung)

    if conf.debug:
        print("Drive {} {} {} {}".format(seite, dutyCycle, PowerLvl, richtung))



def stop():
    for m in range(0,5):
        setSpeedLevel(m,0)
        i2cUpdate()
    if conf.debug:
        print("Drive: stop")