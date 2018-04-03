import socket
import sys
import serial

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gather received data here
alldata = ''

# Open up a serial connection to the Ada hand
left = serial.Serial('/dev/cu.usbserial-DJ004RGL', 38400)

# Bind the socket to the port
server_address = ('localhost', 10001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                # print >>sys.stderr, 'sending data back to the client'
                # connection.sendall(data)
                alldata += data
            else:
                print >>sys.stderr, 'no more data from', client_address
                print "data received: " + alldata
                # Send to the Ada hand
                left.write(alldata)
                alldata = ''
                break
            
    finally:
        # Clean up the connection
        connection.close()
