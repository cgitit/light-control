#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Demo for the TP-Link A19-LB130 RBGW WiFi bulb

import time
from tplight import LB130

global light
global ct

light = [LB130('192.168.1.100'),
	LB130('192.168.1.101'),
	LB130('192.168.1.102'),
	LB130('192.168.1.103'),
	LB130('192.168.1.104'),
	LB130('192.168.1.105'),
	LB130('192.168.1.106')]

ct = float(input("Seconds between each color: "))

while True:
	#cycle time
	for each in light:

		each.brightness = 80
		each.saturation = 90
		# [0,60,120,180,240,300]

		each.hue = 0
		time.sleep(ct)
		each.hue = 45
		time.sleep(ct)
		each.hue = 118
		time.sleep(ct)
		each.hue = 180
		time.sleep(ct)
		each.hue = 252
		time.sleep(ct)
		each.hue = 320
		time.sleep(ct)
