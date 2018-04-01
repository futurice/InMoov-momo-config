import serial
import time

right = serial.Serial('/dev/cu.usbserial-DJ004T2K', 38400)

time.sleep(1)

shut = "900,900,900,900,900"
open = "50,50,50,50,50"

i = 0;

while True:
        if i == 2:
		break

        if i%2 == 0:
		right.write(shut + "\r")
        else:
		right.write(open + "\r")

        i += 1
        time.sleep(3)
