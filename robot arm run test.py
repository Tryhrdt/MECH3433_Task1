import threading
import torch
import numpy as np
import cv2
from robomaster import robot, sensor
import math, time

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")
hull = ep_robot.chassis
ep_camera = ep_robot.camera

eye = sensor.DistanceSensor(ep_robot)
arm = ep_robot.robotic_arm
hand = ep_robot.gripper

def armset(xx, yy):  # writen by Mak Ka Tsun
    arm.moveto(x=xx, y=yy).wait_for_completed()

def grab():  # writen by Mak Ka Tsun
    armset(75, 56)
    print("1")
    armset(89, 141)
    print("2")
    armset(218, -100)
    print("Deploy grab")
    hand.close(power=300)
    print("3")
    time.sleep(2)
    armset(89, 141)

grab()
armset(75, 56)

ep_robot.close()
print('really end')