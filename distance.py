import time
import math
from robomaster import robot

class MarkerInfo:
    def __init__(self, x, y, w, h, info):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._info = info

markers = []

def calculate_distance(w):
    return 2.8 / math.tan(w * math.pi / 3)

def on_detect_marker(marker_info):
    global markers
    print(marker_info)
    if len(marker_info) > 0:
        print("Distance: {0}".format(calculate_distance(marker_info[0][2])))
    markers = marker_info

       #add global markers list of marker object
if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_vision = ep_robot.vision
    ep_camera = ep_robot.camera

    ep_camera.start_video_stream(display=True)
    ep_vision.sub_detect_info(name="marker", callback=on_detect_marker)

    input("HI")
    ep_robot.close()
