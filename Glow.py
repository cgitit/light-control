#!/bin/env python3
from tplight import LB130
import random
import time

#hsb h = 0-360, 0-100, 0-100

global light
light = [LB130('192.168.1.100'),
	LB130('192.168.1.101'),
	LB130('192.168.1.102'),
	LB130('192.168.1.103'),
	LB130('192.168.1.104'),
	LB130('192.168.1.105'),
	LB130('192.168.1.106')]

global light1
global light2
global light3
global light4
global light5
global light6
global light7

light1 = LB130('192.168.1.100')
light2 = LB130('192.168.1.101')
light3 = LB130('192.168.1.102')
light4 = LB130('192.168.1.103')
light5 = LB130('192.168.1.104')
light6 = LB130('192.168.1.105')
light7 = LB130("192.168.1.106")

global h
global s
global b

# Menu for Glow Options
def glow_menu():
	print("Glow/Breathing selection: ")
	print("1.) Red")
	print("2.) Orange")
	print("3.) Yellow")
	print("4.) Green")
	print("5.) Cyan")
	print("6.) Blue")
	print("7.) Violet")
	print("8.) Green/Red")
	print("R.) Random")
	print("A.) All Colors")
	print("M.) Manual")
	glow_color = input("Select a color: ")
	print("Ctrl-C to return to menu.")
	return glow_color

def h_rand():
	h = random.randint(0,359)
	#print("The current glow color number is:" + str(h))
	return h


def breathe():
	global h
	count = 20
	gradient_list = []
	gradient_list.clear()
	while count < 100:
		gradient_list.append(count)
		count += 2
	while count > 30:
		gradient_list.append(count)
		count -= 2
	for x in gradient_list:
		light1.hsb = h, 100, x
		light2.hsb = h, 100, x
		light3.hsb = h, 100, x
		light4.hsb = h, 100, x
		light5.hsb = h, 100, x
		light6.hsb = h, 100, x
		light7.hsb = h, 100, x
		time.sleep(.01)

global glow_color
global h

glow_ = glow_menu()

while True:
	if glow_ == "1":
		h = 0
	elif glow_ == "2":
		h = 30
	elif glow_ == "3":
		h = 60
	elif glow_ == "4":
		h = 120
	elif glow_ == "5":
		h = 180
	elif glow_ == "6":
		h = 235
	elif glow_ == "7":
		h = 245
	elif glow_ == "8":
		c = [0,120]
		while True:
			for x in c:
				h = x
				breathe()
	elif glow_ == "A" or glow_ == "a":
		c = [0,30,60,120,180,235,300]
		while True:
			for x in c:
				h = x
				breathe()
	elif glow_ == "R" or glow_ == "r":
		h = h_rand()
	elif glow_ == "M" or glow_ == "m":
		h = int(input("Enter a number from 0-359: "))
	breathe()
