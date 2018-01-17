#! /usr/bin/python

# Import the libraries we need
import RPi.GPIO as GPIO
import temperatura as temp
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the LED GPIO number
LED = 27

# Set the LED GPIO pin as an output
GPIO.setup(LED, GPIO.OUT)

while True:
    temperature = temp.getTemperature()
    print '%.2f' % (temperature)
    if temperature > 24.00:
        # Turn the GPIO pin on
        print ("on")
        GPIO.output(LED,True)
    else:
        print ("off")
        # Turn the GPIO pin off
        GPIO.output(LED,False)
    time.sleep(1)
#GPIO.cleanup()
