#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Demo for the TP-Link A19-LB130 RBGW WiFi bulb
'''

import time
from tplight import LB130
import random

def main():
	# Main program function
	print("""Chase Light Settings
		---------------
		Colors:
		---------------
		Red: 0
		Orange: 35
		Yellow: 55
		Green: 115
		Light Blue: 175
		Blue: 230
		Purple: 275
		Violet: 300
		Random: R
		""")

	hue_choice = input("Enter a background color number from 0 to 360: ")
	if hue_choice == "R" or hue_choice == "r":
		hue_choice = random.randint(0,360)
		chase_choice = random.randint(0,360)
		bright_choice = random.randint(0,100)
	else:
		hue_choice = int(hue_choice)
		chase_choice = int(input("Enter a chase color number from 0 to 360: "))
		bright_choice = int(input("Enter a brightness from 0 to 100 (0 is not off): "))
	speed = float(input("Enter a speed from .01 sec to 60 seconds: "))

	# create an instance of the light with its IP address
	light1 = LB130("192.168.1.100")
	light2 = LB130("192.168.1.101")
	light3 = LB130("192.168.1.102")
	light4 = LB130("192.168.1.103")
	light5 = LB130("192.168.1.104")
	light6 = LB130("192.168.1.105")
	light7 = LB130("192.168.1.106")

	# set the brightness
	light1.brightness = bright_choice
	light2.brightness = bright_choice
	light3.brightness = bright_choice
	light4.brightness = bright_choice
	light5.brightness = bright_choice
	light6.brightness = bright_choice
	light7.brightness = bright_choice

	print("Press Ctrl-C to exit")
	while True:
		# cycle through the colours
		light5.hue = hue_choice
		light7.hue = hue_choice
		#time.sleep(.01)
		light5.hue = chase_choice
		light7.hue = chase_choice
		time.sleep(speed)

		light5.hue = hue_choice
		light7.hue = hue_choice
		time.sleep(speed)

		light6.hue = hue_choice
		light6.hue = chase_choice
		time.sleep(speed)

		light6.hue = hue_choice
		light4.hue = hue_choice
		light4.hue = chase_choice
		time.sleep(speed)

		light4.hue = hue_choice
		light3.hue = hue_choice
		light3.hue = chase_choice
		time.sleep(speed)

		light3.hue = hue_choice
		light2.hue = hue_choice
		light2.hue = chase_choice
		time.sleep(speed)

		light2.hue = hue_choice
		light1.hue = hue_choice
		light1.hue = chase_choice
		time.sleep(speed)

		light1.hue = hue_choice
		time.sleep(speed)

if __name__ == "__main__":
	main()
