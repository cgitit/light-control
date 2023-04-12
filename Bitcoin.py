#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Demo for the TP-Link A19-LB130 RBGW WiFi bulb
'''

import time
from tplight import LB130
import requests
import json
import sys
import os

# create an instance of the light with its IP address
light = [
	[LB130("192.168.1.100"),
	LB130("192.168.1.101"),
	LB130('192.168.1.102'),
	LB130('192.168.1.103'),
	LB130('192.168.1.104'),
	LB130('192.168.1.105'),
	LB130('192.168.1.106')]

#Colors
def red():
	global light
	for x in light:
		x.hsb=(0,100,80)

def green():
	global light
	for x in light:
		x.hsb = (100,00,70)

def white():
	global light
	for x in light:
		x.temperature = 3800
		x.brightness = 40
def gold():
	global light
	for x in light:
		x.hsb = (35,100,70)
def blue():
	global light
	for x in light:
		x.hsb = (240,100,70)

def get_price():
	cur_price = float(requests.get("https://api.pro.coinbase.com/products/BTC-USD/ticker").json()["price"])
	print("Current Price: " + '\033[92m'+ str(cur_price) + '\033[0m')
	return(cur_price)

def initialize():
	white()
	global sell_price
	global spread
	global rebuy_price
	global count
	global coins
	global low_price
	global high_price
	global last_price
	global update_price
	global total

	get_price()
	sell_price = float(input("Sell price: ")) # 5500
	coins = float(input("How many coins: ")) # 2
	total = sell_price * coins # 11000
	spread = float(input("How much are you trying to make: ")) # 100
	rebuy_price = ((total - spread)/coins)
	count = 0
	#set the low price 2/3 way down the spread
	low_price = sell_price - ((sell_price - rebuy_price) * 0.75)
	#set high price 2/3 way above spread
	high_price = sell_price + ((sell_price - rebuy_price) * 0.75)
	last_price = 0.00
	update_price = 0.00

initialize()

def main():
	'''
	Main program function
	'''

while True:
	os.system("clear")

	global high_price
	global cur_price
	global low_price
	global count
	global update_price
	global spread
	global total

	print("\n")
	print("\n")
	print("\n")
	print("=========================")
	print("High Warning: " + "\033[33m" + str(high_price) + "\033[0m")
	print("\n")
	print("Last Price: " + str(last_price))
	cur_price = get_price()
	count += 1

	#every 5 min notify 
	if count % 5 == 0 and count >= 5:
		#price is rising within range
		if cur_price > update_price:
			gold()
			time.sleep(15)
			white()
			time.sleep(1)
		#price is falling within range
		elif cur_price < update_price:
			blue()
			time.sleep(15)
			white()
			time.sleep(1)
		update_price = last_price
	print("5 Min price update: " + str(update_price))
	print("\n")

	#If current price is greater than high price, flash red to green.
	if cur_price > high_price:
		high_price = cur_price
		green()
		time.sleep(2)
		gold()
		time.sleep(2)
		green()
		time.sleep(2)
		gold()
		time.sleep(2)
		green()
		time.sleep(2)
		white()

	#Or if current price is less than the low price, flash green to red
	elif cur_price < low_price:
		low_price = cur_price
		red()
		time.sleep(2)
		blue()
		time.sleep(2)
		red()
		time.sleep(2)
		blue()
		time.sleep(2)
		red()
		time.sleep(2)
		white()

	#Normal Light - When the price is in range, waiting for a trade
	else:
		white()
	
	#if current price is greater than the sell + spread
	if cur_price > (sell_price + spread):
		green()
		time.sleep(60)
	#Or if the current price is less than or equal to the rebuy price
	elif cur_price <= rebuy_price:
		red()
		break
		#time.sleep(600)
		#initialize()
	
	last_price = cur_price
	print("Low Warning: " + "\033[34m" + str(low_price) + "\033[0m")
	print("=========================")
	print("Sell Price: " + "\033[32m" + str(sell_price) + "\033[0m")
	print("Coins: " + str(coins))
	print("Total sale: " + str(total))
	print("ReBuy Price: " + "\033[31m" + str(rebuy_price) + "\033[0m")
	print("Profit: " + "\033[32m" + str(spread) + "\033[0m")
	print("-------------------------")
	print("Run count: " + "\033[37m" + str(count) + "\033[0m")
	print("-------------------------")
	print("Use tmux for headless - press CTRL-B then D")
	print("\033[32m" + "Green - 60 Seconds - Sell more Warning" + "\033[0m")
	print("\033[32m" + "Green/" + "\033[33m" + "Gold" + "\033[32m"  + " Flash - High Warning." + "\033[0m")
	print("\033[33m" + "Gold Single Flash - Price Up 5 min notification" + "\033[0m")
	print("\033[34m" + "Blue Single Flash - Price Down 5 min notification" + "\033[0m")
	print("\033[34m" + "Blue/" + "\033[31m" + "Red Flash - Low Warning." + "\033[0m")
	print("\033[31m" + "Red - Price met! Set next sell." + "\033[0m")
	print("White - Normal range.  Go find something to do.")
	if cur_price > (sell_price + spread):
		print("Sell More!")
		time.sleep(45)
	elif cur_price <= (rebuy_price):
		print("Buy More!")
		time.sleep(45)
	time.sleep(60)

if __name__ == "__main__":
	main()
