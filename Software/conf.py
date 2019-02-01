# Config Modul

debug=True

#LEDs
intLED = 1
programmLED1=21
programmLED2=20
programmLED3=16
programmLED4=26


#Taster
tasterDig1=19
tasterDig2=13
tasterStop=5
tasterRun=6


#SoftwareSwitch Ports
swSwitchGPIO1=1
swSwitchGPIO2=2
swSwitchGPIO3=3
swSwitchRead=23
swSwitchWrite=24

addrSonicL=(1, 0, 0)
addrSonicR=(1, 1, 1)


#Bildverabeitun
camCropLT=(180, 220, 100, 240)
camColorLB = (12,100,100)
camColorUB = (32,255,255)
camDistance = 15


#I2C Adresses
addrGyro=0x68  # via i2cdetect