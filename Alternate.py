#!/bin/env python3

from tplight import LB130
import random
import time
#import numpy

#Switch

light = [LB130("192.168.1.100"), LB130("192.168.1.101"), LB130("192.168.1.102"), LB130("192.168.1.103"),LB130("192.168.1.104"),LB130("192.168.1.105"),LB130("192.168.1.106")]

light1 = LB130("192.168.1.100")
light2 = LB130("192.168.1.101")
light3 = LB130("192.168.1.102")
light4 = LB130("192.168.1.103")
light5 = LB130("192.168.1.104")
light6 = LB130("192.168.1.105")
light7 = LB130("192.168.1.106")

group1 = [light1, light2, light4, light6]
group2 = [light3, light5, light7]

color_list = [0,120]
#color_list = [0,60,120,180,240,300]

for each in light:
	each.brightness = 60
	each.saturation = 90

def switch():
	x = random.choice(color_list)
	y = random.choice(color_list)
	light1.hue = x
	light2.hue = x
	light3.hue = y
	light4.hue = x
	light5.hue = y
	light6.hue = x
	light7.hue = x
	time.sleep(.5)

while True:
	switch()
