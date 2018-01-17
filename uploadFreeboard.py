#!/bin/python

import acelerometro
import temperatura
import gpsdData

import dweepy
import time

while True:
    speed = acelerometro.velocidad()
    temperature = temperatura.getTemperature()

    coordinate = gpsdData.main()
    latitude = coordinate['latitude']
    longitude = coordinate['longitude']
    # print "el resultado es : ", result

    data = {
           'speed': speed,
           'temperature': temperature,
           'latitude': latitude,
           'longitude': longitude,
    }

    print ("json"),data

    dweepy.dweet_for('grupo_13', {'json': data})
    {
         u'content': {u'json': u'result'},
         u'thing': u'this_is_a_thing'
    }
    time.sleep(0.3)
