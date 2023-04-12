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
	print("\nManual Settings \n"
	"--------------- \n"
	"Colors: \n"
	"Red: 0\n"
	"Orange: 35\n"
	"Yellow: 55\n"
	"Green: 115\n"
	"Light Blue: 175\n"
	"Blue: 230\n"
	"Purple: 275\n"
	"Violet: 300\n")

	hue_choice = int(input("Enter a color number from 0 to 360: "))
	bright_choice = int(input("Enter a brightness from 0 to 100 (0 is not off): "))

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
	light1.brightness = bright_choice
	light2.brightness = bright_choice
	light3.brightness = bright_choice
	light4.brightness = bright_choice
	light5.brightness = bright_choice
	light6.brightness = bright_choice
	light7.brightness = bright_choice

	# cycle through the colours
	light1.hue = hue_choice
	light2.hue = hue_choice
	light3.hue = hue_choice
	light4.hue = hue_choice
	light5.hue = hue_choice
	light6.hue = hue_choice
	light7.hue = hue_choice
	time.sleep(.5)


if __name__ == "__main__":
	main()
