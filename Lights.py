#!/usr/bin/env python3

import os
import sys

#which set to run
def menu():
	print("1.) All \n"
	"2.) Downstairs Only \n"
	"3.) Custom Config \n"
	"Q.) Quit \n")

def main():
	try:
		while True:
			menu()
			selection = input("Option: ")
			if selection == "1":
				os.system("python3 List2.py")
			elif selection == "2":
				os.system("python3 List.py")
			elif selection == "3":
				os.system("python3 List3.py")
			elif selection == "Q" or selection == "q":
				break
			else:
				main()

	except KeyboardInterrupt:
		main()
main()
