import conf
import time
import smbus
import RPi.GPIO as GPIO


# [motor1P, motor1Rot, motor1Speed1, motor1Speed2],

GPIO.setup(conf.pwm0, GPIO.OUT)
GPIO.setup(conf.pwm1, GPIO.OUT)
PWML = GPIO.PWM(conf.pwm0, 1500)
PWMR = GPIO.PWM(conf.pwm1, 1500)
BUS=smbus.SMBus(1)  # bus = smbus.SMBus(0) fuer Revision 1

def init(): 

    intspeed=1
    PWML.start(100)
    PWMR.start(100)
    for m in range(0, 5):
        setSpeedLevel(m,intspeed)
        BUS.write_byte_data(hex(conf.motors[m][1][0]), conf.motors[m][1][1], 0xFF) # Drehrichtung auf 1
        BUS.write_byte_data(hex(conf.motors[m][0][0]), conf.motors[m][0][1], 0xFF) # Power on
        time.sleep(0.5)
        setSpeedLevel(m, 0)


def test():
    for m in range(0, 3):
        for speed in range(1, 3):
            setMotor(m, speed, 1)
            time.sleep(1)
        setMotor(m, 0, 0)

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

def setSpeedLevel(motor, level):
    intspeed = speed(level)
    BUS.write_byte_data(hex(conf.motors[m][2][0]), conf.motors[m][0][1], hex(intspeed[0]))  # speed1
    BUS.write_byte_data(hex(conf.motors[m][3][0]), conf.motors[m][0][1], hex(intspeed[1]))  # speed2

def setMotor(m, PowerLvl=3, richtung=1):
    setSpeedLevel(m, PowerLvl)
    BUS.write_byte_data(hex(conf.motors[m][1][0]), conf.motors[m][1][1], Hex(richtung))
    return

def drive(seite, dutyCycle=100, PowerLvl=3, richtung=1):
    mstart=0;
    if seite== "R":
        mstart=4;
        PWMR.ChangeDutyCycle(dutyCycle)
    else:
        PWML.ChangeDutyCycle(dutyCycle)

    for m  in range(mstart,mstart+3):
        setSpeedLevel(m,PowerLvl)
        BUS.write_byte_data(hex(conf.motors[m][1][0]), conf.motors[m][1][1], Hex(richtung))

    if conf.debug:
        print("Drive {} {} {} {}".format(seite, dutyCycle, PowerLvl, richtung))



def stop():
    for m in range(0,5):
        setSpeedLevel(m,0)
    if conf.debug:
        print("Drive: stop")