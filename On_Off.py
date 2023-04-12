#!/bin/env python3

from tplight import LB130
import random
import time
import json

#hsb h = 0-360, 0-100, 0-100

def read_ip():
	with open('ip_list.cfg') as json_file:
		data = json.load(json_file)
		return data

light = []
data = read_ip()
for each in range(len(data['IP_LIST'])):
	x = str(data['IP_LIST'][int(each)])
	temp_ip = "192.168.1.%s" % (x)
	light.append(LB130(temp_ip))

def menu():
	print("1.) All Lights (IP's) On \n"
	"2.) All Lights (IP's) Off \n"
	"3.) Specific Light On/Off \n"
	"4.) Strobe \n"
	"Q.) Quit \n")

def blink():
	for each in light:
		each.off()
	time.sleep(.18)
	for each in light:
		each.on()

def main():
	while True:
		global light
		menu()
		selection = input("Option: ")
		print(selection)
		print(light)
		if selection == "1":
			for each in light:
				each.on()
		elif selection == "2":
			for each in light:
				each.off()
		elif selection == "3":
			print(light)
			y = input("Which IP: ")
			q = input("Enter 1 for ON, 2 for OFF: ")
			z = "192.168.1.%s" % y
			if len(y) > 0:
				if len(y) <= 3:
					if q == "1":
						LB130(z).on()
					elif q == "2":
						LB130(z).off()
					else:
						print("Invalid Input")
				else:
					print(y + " is an invalid input")
		elif selection == "4":
			while True:
				blink()
		elif selection == "Q" or selection == "q":
			break
		else:
			main()

main()
