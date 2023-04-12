#!/bin/env python3

from tplight import LB130
import random
import time
#import numpy

#Switch

light = [LB130("192.168.1.100"),
	LB130("192.168.1.101"),
	LB130("192.168.1.102"),
	LB130("192.168.1.103"),
	LB130("192.168.1.104"),
	LB130("192.168.1.105"),
	LB130("192.168.1.106"),]

light1 = LB130("192.168.1.100")
light2 = LB130("192.168.1.101")
light3 = LB130("192.168.1.102")
light4 = LB130("192.168.1.103")
light5 = LB130("192.168.1.104")
light6 = LB130("192.168.1.105")
light7 = LB130("192.168.1.106")

color_list = [0,45,80,118,180,252,320]

for each in light:
	each.brightness = 80
	each.saturation = 90

def switch():
	#color_list = [0,60,120,180,240,300]
	x = random.choice(color_list)
	light1.hue = random.choice(color_list)
	light2.hue = x
	light3.hue = random.choice(color_list)
	light4.hue = random.choice(color_list)
	light5.hue = random.choice(color_list)
	light6.hue = random.choice(color_list)
	light7.hue = x
	time.sleep(1)

while True:
	switch()
