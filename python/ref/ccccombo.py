# Take data from UDP and pass it over Zigbee, dumb pass through

import socket
import struct
from digi.xbee.devices import XBeeDevice

device = XBeeDevice("/dev/ttyUSB0", 9600)
print("XBee Connected.\n")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",5005))
print("UDP Connected.\n")

device.open()
#device.send_data_broadcast("Hello World!")


while True: #change to "while data"
    data, addr = sock.recvfrom(1472)
    unpacked = struct.unpack('f', data)
    azimuth = unpacked[0] % 360
    print(type(data))
    print("recieved: " + str(data))
    print("unpacked: " + str(azimuth))
    
    device.send_data_broadcast(str(azimuth))
    
