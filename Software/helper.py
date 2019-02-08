#Helper Module
import RPi.GPIO as GPIO
import conf

GPIO.setmode(GPIO.BCM)

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
    GPIO.setup(conf.programmLED1, GPIO.OUT)
    GPIO.setup(conf.programmLED2, GPIO.OUT)
    GPIO.setup(conf.programmLED3, GPIO.OUT)
    GPIO.setup(conf.programmLED4, GPIO.OUT)

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
        print("Read Rotary Switch: {} ".format(number))
    return number