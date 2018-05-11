# -- coding: utf-8 --
# #############################################################################
#                           YOUR INMOOV CUSTOM
# Here you can add your own commands to play and test with inmoov
# If you udpate the whole script, don't worry, those commands are safe
# ##############################################################################

import socket
import sys

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Gather received data here
    alldata = ''

    # Bind the socket to the port
    server_address = ('localhost', 20000)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        connection, client_address = sock.accept()
        try:
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(32)

                if data:
                    alldata += data
                else:
                    eval(alldata)
                    alldata = ''
                    break
        finally:
            # Clean up the connection
            connection.close()

listen()
