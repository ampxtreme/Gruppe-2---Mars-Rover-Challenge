#Track4: Rock'n'Roll
import sonic
import conf
import cam

def start():
    #init()
    
    while True:
        while sonic.read("test") >= conf.camDistance:
            print("geradeaus")
            
        obstacle = cam.objectDetection()
        print(obstacle)
    
    

def init():

    return

def Texit():
    
    return