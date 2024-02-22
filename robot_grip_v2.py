import robomaster
from robomaster import robot, sensor, gripper
import math, time



def car_move(xx, yy, deg):
    ep_robot.chassis.move(x=xx, y=yy, z=deg, xy_speed=.5).wait_for_completed()


def arm_pos_handler(sub_info):
    print(sub_info)


def arm_pos():
    arm.sub_position(freq=5, callback=arm_pos_handler)

# move arm to position
def armset(xx, yy):  # writen by Mak Ka Tsun
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
def grab():  # writen by Mak Ka Tsun
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


