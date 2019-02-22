'''
PYTHON 2

Connect to Pixhawk to get mission data
Connect to UDP to get SDR data
Enter Control loop
'''
#imports------------------------------------------------
import socket
import struct
import time
from subprocess import call
from dronekit import connect, Command
#--------------------------------------------------------
def download_mission():
    """
    Downloads the current mission and returns it in a list.
    It is used to find our mission way points.
    """
    print " Download mission from vehicle"
    missionlist=[]
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()
    for cmd in cmds:
        missionlist.append(cmd)
    return missionlist

def isNearWaypoint(gps_location):
    """
    This function checks if we are within +/- 1 meter
    of a GPS waypoint
    """
    return True

def sendOverXBee(gps_location, azimuth):
    """
    This function calls a python 3 script to send
    data over the connected XBEE
    """
    # TODO: Make strings if not strings
    arg1 = ' '.join(str(f) for f in gps_location)
    arg2 = str(azimuth)
    exit_code = call("python3 LongDistanceSender.py " + arg1 + " " + arg2, shell=True)
    #print str(exit_code) + "\n"

if __name__ == "__main__":
    """
    Pixhawk setup:
    """
    #vehicle = connect('/dev/ttyACM0', wait_ready=True)
    #missionlist = download_mission()
    # Turn mission list into pairs of coordinates
    #for x in range(len(missionlist)):
    #    print missionlist[x]
    print "Skipping Pixhawk Connection \n"
    
    """
    UDP Setup:
    """
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.bind(("127.0.0.1",5005))
    print "Skipping UDP Connection \n"
    
    """
    Mission Loop:
    """
    while(True):
        # Update GPS Location
        #gps_location = vehicle.gps0
        gps_location = [81.12345, -91.54321]
        # If we are near a waypoint
        if(isNearWaypoint(gps_location)):
            # Get data from SDR via UDP
            #data, addr = sock.recvfrom(1472)
            #unpacked = struct.unpack('f', data)
            #azimuth = unpacked[0] % 360
            azimuth = 0.8554321
            sendOverXBee(gps_location, azimuth)
        
    
    
    
    
    
    
    
    

