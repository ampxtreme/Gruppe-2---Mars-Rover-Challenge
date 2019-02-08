#Helper Module
import RPi.GPIO as GPIO
import conf
import smbus2
import math


BUS=smbus2.SMBus(1)  # bus = smbus.SMBus(0) fuer Revision 1

GPIO.setmode(GPIO.BCM)

LEDs=[0, 0, 0, 0, 0, 0, 0, 0]

def sensorswitch(addr):

    GPIO.output(conf.programmLED1, addr[0])
    GPIO.output(conf.programmLED1, addr[1])
    GPIO.output(conf.programmLED1, addr[2])
    if conf.debug:
        print("senorSwitch: addr {}", format(addr))

def initSensorSwitch():
    GPIO.setup(conf.swSwitchGPIO1, GPIO.OUT)
    GPIO.setup(conf.swSwitchGPIO1, GPIO.OUT)
    GPIO.setup(conf.swSwitchGPIO1, GPIO.OUT)
    GPIO.setup(conf.swSwitchRead, GPIO.IN)
    GPIO.setup(conf.swSwitchWrite, GPIO.OUT)

def initLEDs():
    
    if conf.pcb!=True:
        GPIO.setup(conf.programmLED1, GPIO.OUT)
        GPIO.setup(conf.programmLED2, GPIO.OUT)
        GPIO.setup(conf.programmLED3, GPIO.OUT)
        GPIO.setup(conf.programmLED4, GPIO.OUT)
    else:
        BUS.write_byte_data(0x21, 0x07, 0b00000000)
    
def convertStatusToI2c(liste):
    summe=0
    exp=0
    for i in liste:
        summe=summe+i*pow(2, exp)
        exp=exp+1
    return summe

def updateLED():
    print(convertStatusToI2c(LEDs))
    BUS.write_byte_data(0x21, 0x03, convertStatusToI2c(LEDs))

def initRotarySwitch():
    for gpio in conf.rotaryGPIOs:
        GPIO.setup(gpio, GPIO.IN)


def readRotarySwitch():

    d1 = GPIO.input(conf.rotaryGPIOs[0])
    d2 = GPIO.input(conf.rotaryGPIOs[1])
    d3 = GPIO.input(conf.rotaryGPIOs[2])
    d4 = GPIO.input(conf.rotaryGPIOs[3])

    number=1+ d1*math.pow(2,0) + d2*math.pow(2,1) + d3*math.pow(2,2) + d4*math.pow(2,3)

    if conf.debug:
        print("Read Rotary Switch: {} {} {} {} {}".format(number, d1, d2, d3, d4))
    return number