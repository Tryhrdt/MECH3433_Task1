# main code for Task 4

import cv2
import numpy as np
import robomaster
from robomaster import robot

current_x, current_y, current_z = (0,0,0)
detect = False

# handler function for EP positional data
def positional_data_handler(sub_info):
    global current_x, current_y, current_z
    current_x, current_y, current_z = sub_info

    current_x *= -1
    current_y *= -1
    current_z *= -1

    current_x = round(current_x, 3)
    current_y = round(current_y, 3)
    current_z = round(current_z, 3)
    print("{0}, {1}, {2}".format(current_x, current_y, current_z))

# handler fuction for EP vision data (bowtie)
# format : [x-coord, y-coord, width of marker, height of marker, marker name]
# coord system = (0-1)
# dimension of marker is in coordinates
# Example: [[0.4375, 0.46806, 0.38438, 0.71389, '2']]
def vision_info_handler(sub_info):
    print(sub_info)

def ir_handler(sub_info):
    global detect
    if sub_info[0] < 30:
        detect = True
    else:
        detect = False
    print(detect)

# Define robot object
if __name__ == "__main__":
    #   Using Wi-Fi Direct method to connect
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    # initialize objects:
    ep_chassis  = ep_robot.chassis
    ep_camera   = ep_robot.camera
    ep_vision   = ep_robot.vision
    ep_ir       = ep_robot.sensor



    # initialize coordinate system
    # x = x-coord, y = y-coord, z = rotation in deg
    ep_chassis.sub_position(cs=0, freq=10, callback=positional_data_handler)

    # initialize vision system
    ep_vision.sub_detect_info(name="marker", color="red", callback=vision_info_handler)

    # ep_chassis.move(x=0.6, y=-0.6, z=0, xy_speed=1).wait_for_completed()

    # enable camera screen for debug
    ep_camera.start_video_stream(display=True)

    # enable IR
    ep_ir.sub_distance(freq=20, callback=ir_handler)



    '''TODO
    Find closest vision marker,
    if vision marker is to the left, move left
    if vision marker is to the right, move right
    implement PID?
    check align
    if align, get distance to vision marker
    calculate speed to move towards vision maker safely
    while moving check if speed is ok with distance data
    slow down when ir detect
    close gripper, move back to original position and move horizontally to the next marker given by alex's code
    calculate distance, move according to distance and initial correction data?
    stop
    open gripper
    move back
    then go to next vision marker
    repeat
    move back to 0,0
    end
    '''



    input("Press any button to quit:")
    ep_camera.stop_video_stream()

    ep_robot.close()
