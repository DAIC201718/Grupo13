#import time

def getTemperature():
    #while 1:
    tempfile = open("/sys/bus/w1/devices/28-000009968a64/w1_slave")
    thetext = tempfile.read()
    tempfile.close()
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    return temperature

    #time.sleep(1)

temperature = getTemperature()
#print temperature
