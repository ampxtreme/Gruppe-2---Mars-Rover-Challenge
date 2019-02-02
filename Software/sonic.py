# Sonic Lib
import helper
import conf
import time
import RPi.GPIO as GPIO

def readDist(pos):
        
    if pos != "test":
        if pos == "L":
           helper.sensorswitch(conf.addrSonicL)
           
        if pos == "M":
           helper.sensorswitch(conf.addrSonicM)
           
        if pos == "R":
           helper.sensorswitch(conf.addrSonicR)

    else:
        helper.initSensorSwitch()

    # Trigger auf "high" setzen (Signal senden) // Copyright Jens Dutzi 2015 / Stand: 12.07.2015
    GPIO.output(conf.swSwitchWrite, True)
    time.sleep(0.00001)
    # Trigger auf "low setzen (Signal beenden)
    GPIO.output(conf.swSwitchWrite, False)
    # Aktuelle Zeit setzen
    StartZeit = time.time()
    StopZeit = StartZeit

    # Warte bis "Echo" auf "low" gesetzt wird und setze danach Start-Zeit erneut
    while GPIO.input(conf.swSwitchRead) == 0:
        StartZeit = time.time()

    # Warte bis "Echo" auf "high" wechselt (Signal wird empfangen) und setze End-Zeit
    while GPIO.input(conf.swSwitchRead) == 1:
        StopZeit = time.time()

    # Abstand anhand der Signal-Laufzeit berechnen
    # Schallgeschwindigkeit: 343,50 m/s (bei 20°C Lufttemperatur)
    # Formel: /Signallaufzeit in Sekunden * Schallgeschwindigket in cm/s) / 2 (wg. Hin- und Rückweg des Signals)
    SignalLaufzeit = StopZeit - StartZeit
    dist = round((SignalLaufzeit / 2) * 34350, 2)
    
    if conf.debug:
        print("Sonic {} Read: {} cm".format(pos, str(dist)))
    
    return dist



def read(pos):
    maxdist = 0
    status = 0
    distance = readDist(pos)
    
    if pos == "L":
        maxdist = conf.maxdistL
           
    if pos == "M":
        maxdist = conf.maxdistM
           
    if pos == "R":
        maxdist = conf.maxdistR
           

    if distance > maxdist:
        status = 0
    
    if distance <= maxdist:
        status = 1

    if conf.debug:
        print("Sonic {} Read: {} cm".format(pos, str(dist)))
    
    return status