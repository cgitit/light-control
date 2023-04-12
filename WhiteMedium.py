#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Demo for the TP-Link A19-LB130 RBGW WiFi bulb
'''

import time
from tplight import LB130
from multiprocessing import Process
import random

def main():
	'''
	Main program function
	'''
	# create an instance of the light with its IP address
	light1 = LB130("192.168.1.100")
	light2 = LB130("192.168.1.101")
	light3 = LB130("192.168.1.102")
	light4 = LB130("192.168.1.103")
	light5 = LB130("192.168.1.104")
	light6 = LB130("192.168.1.105")
	light7 = LB130("192.168.1.106")

	# transition period
	light1.transition_period = 0
	light2.transition_period = 0
	light3.transition_period = 0
	light4.transition_period = 0
	light5.transition_period = 0
	light6.transition_period = 0
	light7.transition_period = 0

	# set the brightness to 50%
	light1.brightness = 30
	light2.brightness = 30
	light3.brightness = 30
	light4.brightness = 30
	light5.brightness = 30
	light6.brightness = 30
	light7.brightness = 30

	# cycle through the colours
	light1.temperature = 3800
	light2.temperature = 3800
	light3.temperature = 3800
	light4.temperature = 3800
	light5.temperature = 3800
	light6.temperature = 3800
	light7.temperature = 3800
	time.sleep(.5)


if __name__ == "__main__":
	main()
