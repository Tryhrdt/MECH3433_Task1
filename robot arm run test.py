import threading
import numpy as np
import cv2
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


def armset(xx, yy):  # writen by Mak Ka Tsun
    arm.moveto(x=xx, y=yy).wait_for_completed()

def grab():  # writen by Mak Ka Tsun
    print("gripper opened")
    hand.open(power=100)
    time.sleep(2)
    print("pos 1")
    armset(75, 56)
    time.sleep(1)
    print("pos 2")
    armset(200, -130)
    print("grip")
    hand.close(power=300)
    print("sleep")
    time.sleep(2)
    print("pos 3")
    armset(0, 10)
    armset(0, 10)
    armset(50,160)
    armset(50, 160)
    print("end grip")

def place_block_1(): #writen by Mak Ka Tsun
    print("pos 1")
    armset(50, 160)
    time.sleep(1)
    armset(75, 56)
    print("pos 2")
    armset(200, -120)
    time.sleep(1)
    hand.open(power=100)
    time.sleep(2)
    armset(75, 56)
    armset(50, 100)
    armset(50,160)


def place_block_2(): #writen by Mak Ka Tsun
    print("pos 1")
    armset(50, 160)
    time.sleep(1)
    armset(75, 56)
    print("pos 2")
    armset(50, 40)
    time.sleep(1)
    hand.open(power=100)
    time.sleep(2)
    armset(75, 56)
    armset(50, 100)
    armset(50,160)

def place_block_3(): #writen by Mak Ka Tsun
    hand.open(power=100)
    time.sleep(2)
    armset(50,160)

def flow():
    grab()
    car_move(0,0,90)
    place_block_1()
    car_move(0,0,-90)

    grab()
    car_move(0,0,90)
    time.sleep(2)
    car_move(.15,0,0)
    place_block_2()
    car_move(-.15, 0, 0)
    time.sleep(1)
    car_move(0,0,-90)

    grab()
    car_move(0,0,90)
    time.sleep(2)
    car_move(.3,0,0)
    place_block_3()
    car_move(-0.3,0,0)

#car_move(-.2,0,0)
flow()

ep_robot.close()
print('really end')