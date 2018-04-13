#!/usr/bin/env python

"""
A script for opening a TCP socket from which ASCII input is
forwarded to a serial port which will control an Ada hand.
"""

from __future__ import print_function

import socket
import sys
import serial

_SERIAL_DEVICE_NAME = "/dev/cu.usbserial-DJ004RGL"

__author__ = "Teemu Turunen"
__license__ = "BSD"

def syntax(execname):
    print("Syntax: %s" % execname)
    sys.exit(1)

def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Gather received data here
    alldata = ''

    # Open up a serial connection to the Ada hand
    right = serial.Serial(_SERIAL_DEVICE_NAME, 38400)

    # Bind the socket to the port
    server_address = ('localhost', 20000)
    print("Starting up on %s port %d" % server_address, file=sys.stderr)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print("Waiting for a connection ...", file=sys.stderr)
        connection, client_address = sock.accept()
        try:
            print("Connection from '%s:%d'." %  client_address, file=sys.stderr)
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(32)
                print("Received: %s" %  data, file=sys.stderr)

                if data:
                    # print >>sys.stderr, 'sending data back to the client'
                    # connection.sendall(data)
                    alldata += data
                else:
                    print("No more data from '%s:%d'." %  client_address, file=sys.stderr)
                    print("Data received: '%s'." %  alldata, file=sys.stderr)

                    # Send to the Ada hand
                    right.write(alldata)
                    alldata = ''
                    break
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 1:
        syntax(sys.argv[0])

    main()
