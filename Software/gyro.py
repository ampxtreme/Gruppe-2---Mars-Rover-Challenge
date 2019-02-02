# Gyro Module
# basierend auf #Quellle: https://tutorials-raspberrypi.com/measuring-rotation-and-acceleration-raspberry-pi/
import smbus
import math
import conf
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c # Vermuteter Ausschalter füws mgmnt


BUS=smbus.SMBus(1)  # bus = smbus.SMBus(0) fuer Revision 1
bus=BUS

def powerOn():
    bus.write_byte_data(conf.addrGyro, power_mgmt_1, 0)

def powerOff():
    bus.write_byte_data(conf.addrGyro, power_mgmt_2, 0)

def read_byte(reg):
    return bus.read_byte_data(conf.addrGyro, reg)


def read_word(reg):
    h = bus.read_byte_data(conf.addrGyro, reg)
    l = bus.read_byte_data(conf.addrGyro, reg + 1)
    value = (h << 8) + l
    return value


def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)

def init():
    powerOn()

def getXYZ():

    xout = read_word_2c(0x43) / 131
    yout = read_word_2c(0x45) / 131
    zout = read_word_2c(0x47) / 131
    if(conf.debug):
        print("Gyro getXYZ: {} / {} / {}".format(xout,yout,zout))
    return (xout,yout,zout)

def getRotation():
    xout = read_word_2c(0x3b) / 16384.0
    yout = read_word_2c(0x3d) / 16384.0
    zout = read_word_2c(0x3f) / 16384.0
    if (conf.debug):
        print("Gyro getRotation: {} / {} / {}".format(xout, yout, zout))
    return (xout, yout, zout)

