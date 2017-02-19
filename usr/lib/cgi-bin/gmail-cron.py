#!/usr/bin/env python
 
import os, feedparser, time, serial

ser = serial.Serial('/dev/ttyAMA0', 57600, timeout=1)
ser.open()

DEBUG = 0
 
USERNAME = ""     # just the part before the @ sign, add yours here
PASSWORD = ""     
 
NEWMAIL_OFFSET = 0        # my unread messages never goes to zero, yours might
 
newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

text_file = open('/home/pi/Rapiro/output.txt', 'a')
text_file.write ("You have new emails!\n")
text_file.close()
 
if newmails > NEWMAIL_OFFSET:
	os.system('mpg321 -q mailsound.mp3')
	ser.write("#PR255G000B000T003")
	os.system('mpg321 -q gundam_alert.mp3')
	ser.write("#PR000G000B255T003")
	time.sleep(.5)
	ser.write("#PR255G000B000T003")
	time.sleep(.5)
	ser.write("#PR000G000B255T003")
	time.sleep(.5)
	ser.write("#PR255G000B000T003")
	os.system('mpg321 -q gundam_alert.mp3')
	ser.write("#PR000G000B255T003")
	time.sleep(.5)
	ser.write("#PR255G000B000T003")
	time.sleep(.5)
	ser.write("#PR000G000B255T003")
	time.sleep(.5)
	ser.write("#PR255G000B000T003")
	os.system('mpg321 -q gundam_alert.mp3')
	ser.write("#PR000G000B255T003")
	time.sleep(.5)
	ser.write("#PR255G000B000T003")
	time.sleep(.5)
	ser.write("#PR000G000B255T003")
	time.sleep(.5)
	ser.write("#PR255G000B000T003")
	os.system('mpg321 -q gundam_alert.mp3')
else:
	ser.write("#PS00A135R000G000B255T005")
	time.sleep(1)
	ser.write("#PS00A045R255G000B000T010")
	time.sleep(1)
	ser.write("#PS00A135R000G000B255T010")
	time.sleep(1)
	ser.write("#PS00A045R255G000B000T010")
	time.sleep(1)
	ser.write("#PS00A090R000G000B255T005")

ser.write("#M0")

ser.close()
