import sys
sys.path.insert(0, '../../')
import helper
import conf
import smbus2
BUS=smbus2.SMBus(1)

helper.initLEDs()
helper.LEDs[2]=1
helper.updateLED()
#helper.BUS.write_byte_data(0x21, 0x03, 127)

print(helper.LEDs)