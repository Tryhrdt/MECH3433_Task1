import time
import math
from robomaster import robot


# class MarkerInfo:
#     def __init__(self, x, y, w, h, info):
#         self._x = x
#         self._y = y
#         self._w = w
#         self._h = h
#         self._info = info


markers = []
timer = 0


#   calculate distance based on marker width and trigo, cm
def calculate_distance(w):
    return 4 / math.tan(w * math.pi / 3)  # distance = (width/2) / tan(width * 120deg / 2 * pi / 180)


#   handler function for marker detection
#   [x-coord, y-coord, width of marker, height of marker, marker name]
def on_detect_marker(marker_info):
    global markers, timer
    # if len(marker_info) > 0:
    #     for i in marker_info:
    #         print("ID: {0}\nDistance: {1}".format(i[4], calculate_distance(i[2])))
    markers = marker_info
    timer = time.localtime()

    #   add global markers list of marker object


def ground_distance(w):
    height = 34.5
    return math.sqrt((calculate_distance(w) ** 2) - (height ** 2))  # pyth. theorem : hyp^2 - height^2 = base^2



# if __name__ == '__main__':
#     ep_robot = robot.Robot()
#     ep_robot.initialize(conn_type="ap")
#
#     ep_vision = ep_robot.vision
#     ep_camera = ep_robot.camera
#
#     ep_camera.start_video_stream(display=True)
#     ep_vision.sub_detect_info(name="marker", callback=on_detect_marker)
#
#     input("HI")
#     ep_robot.close()
