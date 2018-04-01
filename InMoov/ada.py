import serial
import time

right = serial.Serial('/dev/cu.usbserial-DJ004T2K', 38400)

time.sleep(3)

shut = "900,900,900,900,900"
open = "50,50,50,50,50"

right.write(shut + "\r")
