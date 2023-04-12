#!/bin/env python3

import os
import sys

def menu():
    print("1.) Ordered Series Lighting \n"
    "2.) Glow \n"
    "3.) White Medium Solid \n"
    "4.) Cycle Modes\n"
    "5.) Synced Random Change \n"
    "6.) Alternate \n"
    "7.) On or Off \n"
    "C.) Chase Light \n"
    "M.) Manual Entry \n"
    "B.) Bitcoin \n"
    "Q.) Exit \n\n"

    "- Make sure all lights are ON!\n"
    "- Lights may take a moment to settle into the pattern choice.\n")

def main():
    try:
        while True:
            #os.system('cls')
            print("\nLight Control")
            print("-------------")
            menu()
            warn = "Press Ctr-C to exit"
            selection = input("Option: ")
            if selection == "1":
                print(warn)
                os.system("python3 sync.py")
            elif selection == "2":
                print(warn)
                os.system("python3 Glow.py")
            elif selection == "3":
                print(warn)
                os.system("python3 WhiteMedium.py")
            elif selection == "4":
                print(warn)
                os.system("python3 Cycle.py")
            elif selection == "5":
                os.system("python3 Switch.py")
            elif selection == "6":
                os.system("python3 Alternate.py")
            elif selection == "7":
                os.system("python3 On_Off.py")
            elif selection == "B" or selection == "b":
                os.system("python3 Bitcoin.py")
            elif selection == "C" or selection == "c":
                os.system("python3 ChaseLight.py")
            elif selection == "m" or selection == "M":
                os.system("python3 Manual.py")
            elif selection == "q" or selection == "Q":
                sys.exit()
            else:
                main()

    except KeyboardInterrupt:
        main()
main()
