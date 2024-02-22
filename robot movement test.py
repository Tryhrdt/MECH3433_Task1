import robomaster
from robomaster import robot
from robomaster import version
from robomaster import led
import time
from robomaster import gripper

sdk_versio = version.__version__
print("sdk version:", sdk_versio)

if __name__ == '__main__':
        # 如果本地IP 自动获取不正确，手动指定本地IP地址
        ep_robot = robot.Robot()

        # 指定连接方式为AP 直连模式
        ep_robot.initialize(conn_type='ap')

        SN = ep_robot.get_sn()
        print("Robot SN:", SN)
        version = ep_robot.get_version()
        print("Robot version: {0}".format(version))


        ep_robot.set_robot_mode(mode=robot.GIMBAL_LEAD)
        ep_led = ep_robot.led
        ep_led.set_led(comp=led.COMP_ALL, r=148, g=60, b=219, effect=led.EFFECT_ON)
        ep_chassis = ep_robot.chassis
        x_val = 1
        ep_chassis.move(x=x_val, y=.5, z=90, xy_speed=1).wait_for_completed()
        #ep_chassis.move(x=x_val, y=.5, z=120, xy_speed=1).wait_for_completed(timeout=1.5)
        #robomaster.gripper.Gripper.close(power=50)
        #robomaster.gripper.Gripper.sub_status(freq=5,callback=None)


        ep_robot.close()