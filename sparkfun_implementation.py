class Robot:
    def __init__(self):
        self.gps = UbloxGps(hard_port=9000)
    
    def getLocation(self):
        return self.gps.do_stuff()

    def tick(self):
        loc = self.getLocation()
        #do things

def main():
    robot = Robot()
    while True:
        robot.tick()

################
# Dependency Injection

class Robot:
    def __init__(self, gps):
        self.gps = gps

    def getLocation(self):
        return self.gps.do_stuff()

    def tick(self):
        loc = self.getLocation()
        #do things

def main():
    # gps = UbloxGps(hard_port=9000)
    gps = MyTestGps()
    robot = Robot(gps)
    while True:
        robot.tick()

##########

class Robot:
    def tick(self, current_location):
        # do things
        pass


def main():
    robot = Robot()
    gps = UbloxGps(9000)

    while True:
        location = gps.getLocation()
        robot.tick(location)

import math
import struct

def set_imu_alignment(self, yaw:float, pitch:float, roll:float):
    # convert to fixed point
    z = int(math.round(yaw*1e2)).to_bytes(4, "little")
    y = int(math.round(pitch*1e2)).to_bytes(4, "little")
    x = int(math.round(roll*1e2)).to_bytes(4, "little")

    version = 0
    doAutoMntAlg = False

    bitfield = struct.pack('<I?xx', version, doAutoMntAlg)

    payload = bitfield + z + y + x
    self.send_message(sp.ESF_CLS, self.esf_ms.get('ALG'), payload)