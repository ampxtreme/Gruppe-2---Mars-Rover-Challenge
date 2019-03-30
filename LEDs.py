import sys
sys.path.insert(0, '../../')
import helper
import conf
import smbus2
import time
#BUS=smbus2.SMBus(1)

helper.initLEDs()
helper.LEDs[2]=1
helper.updateLED()
while(1):
    helper.LEDs=[0, 0, 0, 0, 0, 0, 0, 0]
    helper.updateLED();
    print(helper.LEDs)
    time.sleep(.1)
    
    helper.LEDs=[1, 1, 1, 1, 1, 1, 1, 1]
    print(helper.LEDs)
    helper.updateLED();
    time.sleep(.1)

print(helper.LEDs)