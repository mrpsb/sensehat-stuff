#!/usr/bin/env python

from sense_hat import SenseHat

s = SenseHat()
datalist = ()

# Grab info from the various sensors and cram them into a list

# Temp
temp = int(s.get_temperature())

# Pressure
pres = int(s.get_pressure())

# Humidity
humid = int(s.get_humidity())

prepstring = "T:{0}c H:{1}% P:{2}mb".format(temp,humid,pres)
print prepstring
s.show_message(prepstring,0.05,(255,0,255))

