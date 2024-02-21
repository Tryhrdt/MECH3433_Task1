import robomaster
from robomaster import robot, sensor, gripper
import math, time
ir_dist = 100

def dist_handler(sub_info):
    ir_dist = int(sub_info[0])
    print(ir_dist)

def car_move(xx,yy,deg):
    ep_robot.chassis.move(x=xx, y=yy, z=deg, xy_speed=.5).wait_for_completed()

def armset(xx, yy):  # writen by Mak Ka Tsun
    arm.moveto(x=xx, y=yy).wait_for_completed()

def servomove(xx, yy):
    ep_robot.servo.moveto(index=1, angle=xx)
    ep_robot.servo.moveto(index=2, angle=yy)

def angle(deg):
    return ep_robot.servo.get_angle(index=deg)

def grip_block(x):
    print("gripper opened")
    hand.open(power=100)
    time.sleep(3)
    print("pos 1")
    armset(75, 56)
    time.sleep(1)
    print("pos 2")
    if x == 1:
        print("block pos 1")
        armset(200, -130)
    elif x == 2:
        print("block ps 2")
        armset(50, 40)
    elif x == 3:
        print("block pos 3")
        armset(50, 160)
    print("grip")
    hand.close(power=300)
    time.sleep(2)
    armset(0, 10)
    armset(0, 10)
    armset(50, 160)
    armset(50, 160)
    print("end grip")

def grip_flow():
    grip_block(3)
    hand.open(power=300).wait_for_completed()

if __name__ == "__main__":
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    hull = ep_robot.chassis
    ep_camera = ep_robot.camera
    ep_ir     = ep_robot.sensor
    ep_ir.sub_distance(freq=20, callback=dist_handler)
    eye = sensor.DistanceSensor(ep_robot)
    arm = ep_robot.robotic_arm
    hand = ep_robot.gripper

    armset(200, -130)

    ep_camera.start_video_stream(display=True)
    print("ir_dist:", ir_dist)
    hull.drive_speed(x=0.1, timeout=10)
    while True:
        if ir_dist < 100:
            break
    print("object detected")
    hull.drive_speed(x=-1, timeout=0.001)
    ep_camera.stop_video_stream()





    ep_robot.close()
    print('really end')