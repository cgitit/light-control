#!/bin/env python

from tplight import LB130
import random
import time

global light
global light1
global light2
global light3
global light4
global light5
global light6
global light7

light = [LB130("192.168.1.100"),
	LB130("192.168.1.101"),
	LB130("192.168.1.102"),
	LB130("192.168.1.103"),
	LB130("192.168.1.104"),
	LB130("192.168.1.105"),
	LB130("192.168.1.106")]

light1 = LB130("192.168.1.100")
light2 = LB130("192.168.1.101")
light3 = LB130("192.168.1.102")
light4 = LB130("192.168.1.103")
light5 = LB130("192.168.1.104")
light6 = LB130("192.168.1.105")
light7 = LB130("192.168.1.106")

def sync():
	print("Sync")
	global light
	for each in light:

		each.brightness = 80
		each.saturation = 90

		ct = .5
		each.hue = 0
		time.sleep(ct)
		each.hue = 60
		time.sleep(ct)
		each.hue = 120
		time.sleep(ct)
		each.hue = 180
		time.sleep(ct)
		each.hue = 240
		time.sleep(ct)
		each.hue = 300

def switch():
	print("Switch")
	color_list = [0,60,120,180,240,300]

	for each in light:
		each.brightness = 80
		each.saturation = 90
	for each in range(15):
		light1.hue = random.choice(color_list)
		light2.hue = random.choice(color_list)
		light3.hue = random.choice(color_list)
		light4.hue = random.choice(color_list)
		light5.hue = random.choice(color_list)
		light6.hue = random.choice(color_list)
		light7.hue = random.choice(color_list)
		time.sleep(.35)

def glow():
	print("Glow")
	h = random.randint(0,360)

	# gradiant
	count = 20
	gradient_list = []
	gradient_list.clear()
	while count < 100:
		gradient_list.append(count)
		count += 2
	while count > 30:
		gradient_list.append(count)
		count -= 2
	#count to 100 by 5 starting at 5
	# then count down to 5 by 5
	for each in range(2):
		for x in gradient_list:
			light1.hsb = h, 100, x
			light2.hsb = h, 100, x
			light3.hsb = h, 100, x
			light4.hsb = h, 100, x
			light5.hsb = h, 100, x
			light6.hsb = h, 100, x
			light7.hsb = h, 100, x
			time.sleep(.005)

def chase():
	print("Chase")
	for each in range(5):
		hue_choice = random.randint(0,359)
		chase_choice = random.randint(0,359)
		times = [.5, .75, 1]
		speed = random.choice(times)

		for x in light:
			x.hue = hue_choice

		light1.hue = chase_choice
		time.sleep(speed)

		light1.hue = hue_choice
		light2.hue = chase_choice
		time.sleep(speed)

		light2.hue = hue_choice
		light3.hue = chase_choice
		time.sleep(speed)

		light3.hue = hue_choice
		light4.hue = chase_choice
		time.sleep(speed)

		light4.hue = hue_choice
		light5.hue = chase_choice
		time.sleep(speed)

		light5.hue = hue_choice
		light6.hue = chase_choice
		time.sleep(speed)

		light6.hue = hue_choice
		light7.hue = chase_choice
		time.sleep(speed)

		light7.hue = hue_choice

while True:
	rand_choice = random.randint(1,4)
	if rand_choice == 1:
		sync()
	elif rand_choice == 2:
		glow()
	elif rand_choice == 3:
		chase()
	elif rand_choice == 4:
		switch()
	time.sleep(1)
