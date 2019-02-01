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
