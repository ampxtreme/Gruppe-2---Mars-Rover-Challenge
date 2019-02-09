import conf
import time
import smbus2
import helper
import RPi.GPIO as GPIO


# [motor1P, motor1Rot, motor1Speed1, motor1Speed2],
GPIO.setmode(GPIO.BCM)
GPIO.setup(conf.pwm0, GPIO.OUT)
GPIO.setup(conf.pwm1, GPIO.OUT)
#GPIO.output(conf.pwm0,False)
#GPIO.output(conf.pwm1,False)
PWML = GPIO.PWM(conf.pwm0, 20)
PWMR = GPIO.PWM(conf.pwm1, 20)

BUS=smbus2.SMBus(1)  # bus = smbus.SMBus(0) fuer Revision 1

#     je 2 Bit ein Motor
BANK0=[1, 1, 1, 1, 1, 1, 1, 1]

#     motor  on 0-5 power0 , M4
BANK1=[0, 0, 0, 0, 0, 0, 1, 1]

#     motor  direction 0-5, M5
BANK2=[1, 0, 1, 1, 1, 0, 1, 1]

startDirection=[1, 0, 1, 1, 1, 0]

def init(): 

    intspeed=1
    BUS.write_byte_data(0x21, 0x06, 0b000000000)
    BUS.write_byte_data(0x21, 0x02, helper.convertStatusToI2c(BANK0))
    
    BUS.write_byte_data(0x20, 0x06, 0b00000000)
    BUS.write_byte_data(0x20, 0x02, helper.convertStatusToI2c(BANK1))
    
    BUS.write_byte_data(0x20, 0x07, 0b00000000)
    BUS.write_byte_data(0x20, 0x03, helper.convertStatusToI2c(BANK2))
    
    PWML.start(0)
    PWMR.start(0)
   # for m in range(0, 5):
    #    setSpeedLevel(m,intspeed)
    #    BANK1[m]=0
    #    i2cUpdate()
    #    time.sleep(0.5)
        #setSpeedLevel(m, 0)


def test():
    PWMR.ChangeDutyCycle(50)
    PWML.ChangeDutyCycle(50)
    for m in range(0, 6):
        setMotor(m, 3, 0)
        print(m, BANK0,BANK1,BANK2)
        time.sleep(1)
        setMotor(m, 0, 0)
    PWMR.ChangeDutyCycle(0)
    PWML.ChangeDutyCycle(0)
        
def i2cUpdate():
    BUS.write_byte_data(0x21, 0x02, helper.convertStatusToI2c(BANK0))
    BUS.write_byte_data(0x20, 0x02, helper.convertStatusToI2c(BANK1))
    BUS.write_byte_data(0x20, 0x03, helper.convertStatusToI2c(BANK2))
    

def testpwm(speed=3):
    drive("R", 0, speed)
    drive("L", 0, speed)
    for i in range(0, 100):
        PWMR.ChangeDutyCycle(i)
        PWML.ChangeDutyCycle(i)
        time.sleep(0.2)
        print("{} on Lvl {}".format(i, speed))


def speed(s):

    if s==1:
        return (1, 0)
    if s==2:
        return (0, 1)
    if s==3:
        return (0, 0)
    return (1, 1)

def setSpeedLevel(m, level):
    intspeed = speed(level)
    if m==0:
        BANK0[0]= intspeed[0]
        BANK0[1]= intspeed[1]
    elif m==1:
        BANK0[2]= intspeed[0]
        BANK0[3]= intspeed[1]
    elif m==2:
        BANK0[4]= intspeed[0]
        BANK0[5]= intspeed[1]
    elif m==3:
        BANK0[6]= intspeed[0]
        BANK0[7]= intspeed[1]
    elif m==4:
        BANK1[6]= intspeed[0]
        BANK1[7]= intspeed[1]  
    elif m==5:
        BANK2[6]= intspeed[0]
        BANK2[7]= intspeed[1]
  
    i2cUpdate()

def setMotor(m, PowerLvl=3, richtung=0):
    setSpeedLevel(m, PowerLvl)
    r=startDirection[m]
    if richtung==1 and r == 0:
        rset=1
    elif richtung ==1 and r ==1:
        rest=0
    elif richtung ==0:
        rset=r

    BANK2[m]=rset
    i2cUpdate()
    return

def drive(seite, dutyCycle=100, PowerLvl=3, richtung=0):
    mstart=0;
    if seite== "L":
        mstart=3;
        PWMR.ChangeDutyCycle(dutyCycle)
    else:
        PWML.ChangeDutyCycle(dutyCycle)

    for m in range(mstart,mstart+3):
        
        setSpeedLevel(m,PowerLvl)
        

    if conf.debug:
        print("Drive {} {} {} {}".format(seite, dutyCycle, PowerLvl, richtung))



def stop():
    for m in range(0,5):
        setSpeedLevel(m,0)
        i2cUpdate()
    if conf.debug:
        print("Drive: stop")