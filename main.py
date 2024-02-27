# main code for Task 4
# dependencies: robomaster, distance.py, robot_grip_v2(redundant)
# main program is at the bottom of this file



import time
import cv2
import numpy as np
import robomaster
from robomaster import robot
# import robot_grip_v2 as rg        #   difficult to implement function, directly copied from robot_grip_v2 to main.py, writen by Mak Ka Tsun
import distance as d

current_x, current_y, current_z = (0, 0, 0)  # current position
markers = []
detect = False  # IR sensor detect object?


# handler function for EP positional data
def positional_data_handler(sub_info):
    global current_x, current_y, current_z
    current_x, current_y, current_z = sub_info

    current_x *= -1
    current_y *= -1
    current_z *= -1

    current_x = round(current_x, 3)
    current_y = round(current_y, 3)
    current_z = round(current_z, 3)  # print("{0}, {1}, {2}".format(current_x, current_y, current_z))


def ir_handler(sub_info):
    global detect
    if sub_info[0] == 0:
        detect = True
    else:
        detect = False  # print(detect)


# find index of the marker id
def get_index(in_list, marker_id):
    for i in in_list:
        if int(i[4]) == marker_id:      #   check if item 5 of that element matches the id we want
            return in_list.index(i)
    return -1

# align and find distance(cm)
def align_marker(number, append=True):
    # format : [x-coord, y-coord, width of marker, height of marker, marker name]
    while True:
        try:    #   disregard index errors so the program doesn't crash if the markers list changes unexpectedly
            if get_index(d.markers, number) == -1:
                # print(d.markers)
                time.sleep(0.05)    # if nothing is detected or the required marker is not found, 0.05s delay to
                # prevent while loop from degrading camera feed
                continue
            selected_info = d.markers[get_index(d.markers, number)]     #   information of the selected vision marker
            if 0.498 <= selected_info[0] <= 0.502:                      #   if marker is within the acceptable region of 0.004 size
                ep_chassis.drive_speed(y=0.01, timeout=0.001)           #   brake and stop chassis
                ep_chassis.drive_speed(y=-0.01, timeout=0.001)
                if append:                  #   appends selected info to the selected
                    markers.append(
                        [selected_info[4], (current_x + d.ground_distance(selected_info[2]) / 100), current_y])
                return
            elif selected_info[0] <= 0.498:                         #   move chassis to correct error
                ep_chassis.drive_speed(y=-0.1)
            elif selected_info[0] >= 0.502:
                ep_chassis.drive_speed(y=0.1)
        except:
            ep_chassis.drive_speed(y=0.01, timeout=0.001)           #   stop if an exception is raised
        finally:
            time.sleep(0.05)                                        #   wait 0.05s regardless
    return


def car_move(xx, yy, deg):
    ep_chassis.move(x=xx, y=yy, z=deg, xy_speed=.5).wait_for_completed()
    ep_chassis.drive_speed(x=-xx, y=-yy, timeout=0.001)


#   handler function to print arm position
def arm_pos_handler(sub_info):
    print(sub_info)


#   function to get arm position
def arm_pos():
    arm.sub_position(freq=5, callback=arm_pos_handler)


# move arm to position
def armset(xx, yy):
    arm.moveto(x=xx, y=yy).wait_for_completed()


# reset arm position (at rest)
def ini_arm_pos():
    armset(70, 40)
    time.sleep(1)


#  move arm to pickup/place block on ground
def block_1_arm_pos():
    armset(180, -60)
    time.sleep(1)


#   move arm to place 2nd block on top, no offset required
def block_2_arm_pos():
    armset(180, 40)
    time.sleep(1)


#   move arm to place 3rd block on top, chassis offset by 0.08m
def block_3_arm_pos():
    armset(140, 130)
    time.sleep(1)


#   close gripper
def grab():
    hand.open(power=100)
    time.sleep(2)
    block_1_arm_pos()
    hand.close(power=300)
    time.sleep(2)
    block_3_arm_pos()


#   unified function to place block at different points, 1=ground, 2= on top, 3=last block
def place_block(num):
    block_3_arm_pos()  # highest position
    if num == 1:
        block_1_arm_pos()
    elif num == 2:
        block_2_arm_pos()
    elif num == 3:
        car_move(.08, 0, 0)
        block_3_arm_pos()
    hand.open(power=100)
    time.sleep(2)
    ini_arm_pos()


def pick(number):
    offset = 0          #   offset settings for placing the last block
    if number == 3:
        offset = 0.2
    align_marker(number)    #   align to the selected block
    print(markers)                              #debug
    print(markers[number - 1][1] - current_x)
    block_1_arm_pos()                           #   raise arm to pickup block at ground level
    ep_chassis.move(x=markers[number - 1][1] - current_x - 0.18 + offset, y=0, xy_speed=0.7).wait_for_completed()       #move forward to grab block
    ep_chassis.drive_speed(x=0.1)               # slow down for final approach
    time.sleep(0.5)                             # hard coded approach
    ep_chassis.drive_speed(x=-0.5, timeout=0.01)    #   brake and stop chassis
    time.sleep(0.5)
    print("ok")
    grab()                                      # predefined action to close gripper and raise block
    ini_arm_pos()                               # move arm to give the camera maximum visibility
    ep_chassis.move(x=-(markers[number - 1][1] - current_x) / 2, y=0, xy_speed=0.7).wait_for_completed()    # move back to initial x position (starting line)
    ep_chassis.drive_speed(x=0.5, timeout=0.01)         #   brake and stop chassis
    time.sleep(0.5)                                     #   sleep to let everything settle down
    return


def placer(number):
    align_marker(2)                         #   align to the base block no. "2"
    print(markers)                          #   debug
    print(markers[1][1] - current_x)
    if number == 2:                         #   offset settings for different blocks, IMU error may be predictable
        block_2_arm_pos()
        ep_chassis.move(x=(markers[1][1] - current_x - 0.18), y=0, xy_speed=0.7).wait_for_completed()
    else:
        block_3_arm_pos()
        ep_chassis.move(x=(markers[1][1] - current_x - 0.13), y=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.drive_speed(x=0.1)           #   slows down for final approach
    time.sleep(0.5)
    ep_chassis.drive_speed(x=-0.5, timeout=0.001)   #   brake and stop chassis
    time.sleep(0.5)
    print("ok")
    hand.open(power=100)                    #   open gripper to drop the block
    time.sleep(1)
    ep_chassis.move(x=-(markers[number - 1][1] - current_x) / 2, y=0, xy_speed=0.7).wait_for_completed()    #   go back to starting line
    ep_chassis.drive_speed(x=0.5, timeout=0.01)                                                             # brake and stop
    return


# Define robot object
if __name__ == "__main__":
    #   Using Wi-Fi Direct method to connect
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    # initialize objects:
    ep_chassis = ep_robot.chassis
    ep_camera = ep_robot.camera
    ep_vision = ep_robot.vision
    ep_ir = ep_robot.sensor
    arm = ep_robot.robotic_arm
    hand = ep_robot.gripper

    # initialize coordinate system
    # x = x-coord, y = y-coord, z = rotation in deg
    ep_chassis.sub_position(cs=0, freq=10, callback=positional_data_handler)

    # initialize vision system
    ep_vision.sub_detect_info(name="marker", color="red", callback=d.on_detect_marker)

    # enable camera screen for debug
    ep_camera.start_video_stream(display=True)

    # enable IR
    ep_ir.sub_distance(freq=20, callback=ir_handler)

    # reset arm position
    hand.open()     #   open gripper
    ini_arm_pos()   #   return arm to initial position to see the area better

    # main program
    pick(1)     #   grab block 1
    placer(2)   #   place at block 2
    pick(3)     #   grab block 3
    placer(3)   # place block 3   (could be more generalized but there was no function to detect the blocks already
    # placed so this was hardcoded)

    ep_camera.stop_video_stream()   #   stop camera feed
    ep_robot.close()                #   disconnect and release robomaster resources
