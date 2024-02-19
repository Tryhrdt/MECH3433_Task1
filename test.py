import time
import robomaster
from robomaster import robot


def arm_pos_handler(sub_info):
    pos_x, pos_y = sub_info
    print("Current pos: {0}, {1}\n".format(pos_x, pos_y))


if __name__ == '__main__':
    # 如果本地IP 自动获取不正确，手动指定本地IP地址
    ep_robot = robot.Robot()

    # 指定连接方式为AP 直连模式
    ep_robot.initialize(conn_type='ap')

    # main code:
    ep_arm = ep_robot.robotic_arm
    ep_arm.sub_position(5, callback=arm_pos_handler)
    time.sleep(1)
    ep_arm.recenter().wait_for_completed()
    ep_arm.move(x=200, y=-100).wait_for_completed()

    ep_arm.unsub_position()

    ep_robot.close()
