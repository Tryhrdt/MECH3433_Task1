import robomaster
from robomaster import robot, sensor, gripper
import math, time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")
hull = ep_robot.chassis
ep_camera = ep_robot.camera

eye = sensor.DistanceSensor(ep_robot)
arm = ep_robot.robotic_arm
hand = ep_robot.gripper

def car_move(xx,yy,deg):
    ep_robot.chassis.move(x=xx, y=yy, z=deg, xy_speed=.5).wait_for_completed()

def arm_pos_handler(sub_info):
    print(sub_info)

def arm_pos():
    arm.sub_position(freq=5, callback=arm_pos_handler)

def armset(xx, yy):  # writen by Mak Ka Tsun
    arm.moveto(x=xx, y=yy).wait_for_completed()

def ini_arm_pos():
    armset(70,40)
    time.sleep(1)

def block_1_arm_pos():
    armset(180,-60)
    time.sleep(1)

def block_2_arm_pos():
    armset(180, 40)
    time.sleep(1)

def block_3_arm_pos():
    armset(140, 130)
    time.sleep(1)

def grab():  # writen by Mak Ka Tsun
    hand.open(power=100)
    time.sleep(2)
    block_1_arm_pos()
    hand.close(power=300)
    time.sleep(2)
    block_3_arm_pos()

def place_block(num):
    block_3_arm_pos() # highest position
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




arm_pos()
ini_arm_pos()
grab()
car_move(0,0,90)
place_block(1)
car_move(0,0,-90)
grab()
car_move(0,0,90)
place_block(2)
car_move(0,0,-90)
grab()
car_move(0,0,90)
place_block(3)
car_move(-.1, 0, 0)
time.sleep(1)
car_move(0,0,-90)

time.sleep(3)


ep_robot.close()
print('really end')