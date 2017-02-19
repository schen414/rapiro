#!/usr/bin/env python
 
import time, serial

ser = serial.Serial('/dev/ttyAMA0', 57600, timeout=1)
ser.open()

ser.write("#PS02A180T010")
time.sleep(1.5)
ser.write("#PS03A050T010")
time.sleep(1.5)
ser.write("#PS05A000T010")
time.sleep(1.5)
ser.write("#PS06A130T010")
time.sleep(1.5)

ser.write("#PS00A160S01A000T010")
time.sleep(1.5)
ser.write("#PS00A090S01A000T010")
time.sleep(1.5)

ser.write("#PS00A160S01A000T010")
time.sleep(1.5)
ser.write("#PS00A090S01A090T010")
time.sleep(1.5)


#ser.write("#PS02A220T010")
#time.sleep(1)
#ser.write("#PS02A180T010")
#time.sleep(1)
#ser.write("#PS02A220T010")
#time.sleep(1)

ser.write("#M0")

ser.close()
