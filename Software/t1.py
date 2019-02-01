#Track1: Ramp module

def start():
    init()
    return true


def init():
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    return

def Texit():
    GPIO.output(18, GPIO.LOW)
    return


