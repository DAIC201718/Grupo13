import  RPi.GPIO as GPIO
import time
import gpsdData
import enviarMail

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    inputValue = GPIO.input(12)
    if (inputValue == False):
        print("Button press")
        coordinate = gpsdData.main()
        latitude = coordinate['latitude']
        longitude = coordinate['longitude']

        enviarMail.sendemail(from_addr    = 'findmymoto13@gmail.com', 
                  to_addr_list = ['dcasado@deusto.es'],
                  cc_addr_list = [''],
                  subject      = 'HELP FindMyMoto', 
                  message      = 'Help my location is %f, %f' % (latitude, longitude),
                  login        = 'findmymoto13@gmail.com', 
                  password     = 'grupo13mamm')
        enviarMail.sendemail(from_addr    = 'findmymoto13@gmail.com', 
                  to_addr_list = ['maria.barredo@opendeusto.es'],
                  cc_addr_list = [''],
                  subject      = 'HELP FindMyMoto', 
                  message      = 'Help my location is %f, %f' % (latitude, longitude),
                  login        = 'findmymoto13@gmail.com', 
                  password     = 'grupo13mamm')


    time.sleep(3)
