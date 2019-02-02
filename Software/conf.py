# Config Modul 02.02. 11:00

debug=True
pcb=False # PCB vorhanden

#LEDs solllen über I1c
intLED = 1
programmLED1=21 # 
programmLED2=20 # 
programmLED3=16 # 
programmLED4=26 #

#I2C
i2csSDA=8
i2cSCL=9


i2cP1=(0x21, 1, 1)# Grüne LEDs, Programmwahl
i2cP2=(0x21, 1, 2)
i2cP3=(0x21, 1, 3)
i2cP4=(0x21, 1, 5)

i2cGelb1=(0x21, 1, 0)
i2cGelb2=(0x21, 1, 4)

i2cGreen1=(0x21, 1, 6)
i2cGreen2=(0x21, 1, 7)

addrGyro=0x68  # via i2cdetect 

#motors ic2 addr, Port, Pin Motor
motor1P=(0x20, 0, 0)#on/off
motor1Rot=(0x20, 1, 0)# rotation direction
motor1Speed1=(0x20, 0, 6)# 4 Stufen 
motor1Speed2=(0x20, 0, 7)# 4 Stufen 

motor2P=(0x20, 0, 1)
motor2Rot=(0x20, 1, 1)# rotation direction
motor2Speed1=(0x20, 1, 6)# 4 Stufen
motor2Speed2=(0x20, 1, 7)# 4 Stufen

motor3P=(0x20, 0, 2)
motor3Rot=(0x20, 1, 2)# rotation direction
motor3Speed1=(0x21, 0, 0)# 4 Stufen
motor3Speed2=(0x21, 0, 1)# 4 Stufen

motor4P=(0x20, 0, 3)
motor4Rot=(0x20, 1, 3)# rotation direction
motor4Speed1=(0x21, 0, 2)# 4 Stufen
motor4Speed2=(0x21, 0, 3)# 4 Stufen

motor5P=(0x21, 0, 4)
motor5Rot=(0x20, 1, 4)# rotation direction
motor5Speed1=(0x21, 0, 4)# 4 Stufen
motor5Speed2=(0x21, 0, 5)# 4 Stufen

motor6P=(0x20, 0, 5)
motor6Rot=(0x20, 1, 5)# rotation direction
motor6Speed1=(0x21, 0, 6)# 4 Stufen
motor6Speed2=(0x21, 0, 7)# 4 Stufen
motors=[
    [motor1P, motor1Rot, motor1Speed1, motor1Speed2],
    [motor2P, motor2Rot, motor2Speed1, motor2Speed2],
    [motor3P, motor3Rot, motor3Speed1, motor3Speed2],
    [motor4P, motor4Rot, motor4Speed1, motor4Speed2],
    [motor5P, motor5Rot, motor5Speed1, motor5Speed2],
    [motor6P, motor6Rot, motor6Speed1, motor6Speed2],
    [motor6P, motor6Rot, motor6Speed1, motor6Speed2]
    ]
pwm1=23
pwm0=26


#Taster
tasterDig1=19
tasterDig2=13
tasterStop=5  #pcb GPIO 21
tasterRun=6   #pcb GPIO 22 //vmtl rot

rotaryP1=(0, 0, 0, 0)
rotaryGPIOs=(27, 28, 29, 25) # GPIO READ Ports (klein nach Groß)


#SoftwareSwitch Ports Nr1
swSwitchGPIO1=2 # 
swSwitchGPIO2=3 #
swSwitchGPIO3=4 #
swSwitchRead=23 #pcb GPIO 0
swSwitchWrite=24 #pcb GPIO 1

addrSonicL=(1, 0, 0)
addrSonicR=(1, 1, 1)
addrSonicR=(1, 1, 1)

#SoftwareSwitch Ports Nr2
swSwitch2GPIO1=12 # 
swSwitch2GPIO2=13 #
swSwitch2GPIO3=14 #
swSwitch2Read=10 #
swSwitch2Write=11 #


#Bildverabeitun
camCropLT=(180, 220, 100, 240)
camColorLB = (12,100,100)
camColorUB = (32,255,255)
camDistance = 15

#linehold
lineVL = 5
lineVR = 6

#sonic
maxdistL = 50
maxdistM = 40
maxDistR = 50

#free GPIO
#7,24

#serial com 
serialTX=15
serialRX=16

