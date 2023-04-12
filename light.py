#!/usr/bin/env python

#This is a light control menu for TPLINK

from tplight import LB130

def getIP():
    try:
        count = 0
        f = open("ip_config.cfg", "r")
        sLen = len(f.readline())
        s = f.readline()
        print(sLen)
        print(s)
    except:
        print("Error with file.")

getIP()
