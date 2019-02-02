#Linehold Sensor Module
import conf

def line():
    linearray = [0, 0]
    
    if conf.lineL == True:
        linearray[0] = 1
    else:
        linearray[0] = 0
        
    if conf.lineR == True:
        linearray[1] = 1
    else:
        linearray[1] = 0
    
    if conf.debug:
        print("LineL: {} LineR: {} ".format(linearray[0], linearray[1]))
    
    return linearray