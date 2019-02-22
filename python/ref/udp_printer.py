import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",5005))

print("connected")

while True:
    data, addr = sock.recvfrom(1472)
    unpacked = struct.unpack('f', data)
    azimuth = unpacked[0] % 360
    print(type(data))
    print("recieved: " + str(data))
    print("unpacked: " + str(azimuth))