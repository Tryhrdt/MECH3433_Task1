# TODO write function for recognizing shapes in the frame

import time
import cv2
import robomaster
from robomaster import robot

if __name__ == "__main__":
    #   Using Wi-Fi Direct method to connect
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    # main code:
    # get camera stream:
    ep_camera = ep_robot.camera

    # get 200 frames
    ep_camera.start_video_stream(display=False)
    for i in range(0, 200):
        img = ep_camera.read_cv2_image()
        cv2.imshow("Robot", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()

    ep_robot.close()



# function to find shapes in the frame, returns a nested array of values in the format of [[{number of vertex}, {x-coord}, {y-coord}]...]
# def find_shape():
#     output_arr = []
#
#     return output_arr