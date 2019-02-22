import socket
import struct
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",5005))
print("connected")

while True:
    data, addr = sock.recvfrom(1472)
    unpacked = struct.unpack('f', data)
    grc_float = unpacked[0]
    grc_string = str(grc_float)
    ts = time.gmtime()
    ts_string = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    log_entry = "# " + ts_string + " : " + grc_string
    
    print(log_entry)
    log = open("grc_udp_sink_log.txt", "a")
    log.write(log_entry + "\n")
    log.close()
    