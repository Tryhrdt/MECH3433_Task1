import time
import robomaster
from robomaster import robot
global dist1, dist2, dist3, dist4

def arm_pos_handler(sub_info):
    pos_x, pos_y = sub_info
    print("Current pos: {0}, {1}\n".format(pos_x, pos_y))

def dist_sensor_handler(sub_info):
    dist1, dist2, dist3, dist4 = sub_info
    print("IR prox distance: {0}".format(dist1))

if __name__ == '__main__':
    # 如果本地IP 自动获取不正确，手动指定本地IP地址
    ep_robot = robot.Robot()

    # 指定连接方式为AP 直连模式
    ep_robot.initialize(conn_type='ap')

    # main code:
    ep_arm = ep_robot.robotic_arm
    ep_sensor = ep_robot.sensor
    ep_sensor.sub_distance(freq=5, callback=dist_sensor_handler)
    # ep_arm.sub_position(freq=5, callback=arm_pos_handler)
    ep_arm.recenter().wait_for_completed(timeout=10)
    # ep_arm.unsub_position()
    if dist1 == 0:
        ep_arm.gripper.close().wait_for_completed()
        ep_arm.move(y=100).wait_for_completed()
    
    ep_sensor.unsub_distance()



    ep_robot.close()
