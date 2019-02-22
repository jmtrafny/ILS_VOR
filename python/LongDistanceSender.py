from digi.xbee.devices import XBeeDevice
import sys
import time

# Generate timestamp:
ts = time.gmtime()
ts_string = time.strftime("%Y-%m-%d %H:%M:%S", ts)

'''
Gather data from sys.argv:
    [1]: Lattitude
    [2]: Longitude
    [3]: Azimuth
    
Outgoing json format:
    "{msg_type: 'vor', time: '2019-02-21 00:30:22', lat: float, long: float, azimuth: float}"
'''
lat = sys.argv[1]
long = sys.argv[2]
azimuth = sys.argv[3]
send_string = "{msg_type: 'vor', time: '" + ts_string + \
              "', lat: " + lat + \
              ", long: " + long + \
              ", azimuth: " + azimuth + "}"

device = XBeeDevice("/dev/ttyUSB0", 9600)
device.open()
device.send_data_broadcast(send_string)
device.close()
