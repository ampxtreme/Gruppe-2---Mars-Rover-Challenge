# Sonic Lib
import helper
import conf
import time
import RPi.GPIO as GPIO

def read(pos):
    globals debug conf
    if pos == "L":
       helper.sensorswitch(conf.addrSonicL)
    if pos == "M":
       helper.sensorswitch(conf.addrSonicM)
    if pos == "R":
       helper.sensorswitch(conf.addrSonicR)

       # Trigger auf "high" setzen (Signal senden) // Copyright Jens Dutzi 2015 / Stand: 12.07.2015
       GPIO.output(conf.swSwitchWrite, True)
       time.sleep(0.00001)
       # Trigger auf "low setzen (Signal beenden)
       GPIO.output(swSwitchWrite, False)
       # Aktuelle Zeit setzen
       StartZeit = time.time()
       StopZeit = StartZeit

       # Warte bis "Echo" auf "low" gesetzt wird und setze danach Start-Zeit erneut
       while GPIO.input(conf.swSwitchRead) == 0:
           StartZeit = time.time()

       # Warte bis "Echo" auf "high" wechselt (Signal wird empfangen) und setze End-Zeit
       while GPIO.input(swSwitchWrite) == 1:
           StopZeit = time.time()

       # Abstand anhand der Signal-Laufzeit berechnen
       # Schallgeschwindigkeit: 343,50 m/s (bei 20°C Lufttemperatur)
       # Formel: /Signallaufzeit in Sekunden * Schallgeschwindigket in cm/s) / 2 (wg. Hin- und Rückweg des Signals)
       SignalLaufzeit = StopZeit - StartZeit
       dist = (SignalLaufzeit / 2) * 34350


    if debug:
        print("Sonic {} Read: {] cm", format(pos, dist))
    return dist