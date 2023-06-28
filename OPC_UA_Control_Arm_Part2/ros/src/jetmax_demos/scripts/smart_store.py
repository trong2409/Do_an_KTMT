#!/usr/bin/env python3
import sys
import cv2
import math
import time
import rospy
import numpy as np
import threading
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest
from std_srvs.srv import Empty
from jetmax_control.msg import SetServo
import hiwonder
import queue
import pupil_apriltags as apriltag
import yaml


"""
智慧仓储
"""

ROS_NODE_NAME = "smart_store"
TAG_SIZE = 33.30


class AprilTagDetect:
    def __init__(self):
        self.camera_params = None
        self.runner = None
        self.K = None
        self.R = None
        self.T = None


    def load_camera_params(self):
        self.camera_params = rospy.get_param('/camera_cal/block_params', self.camera_params)
        if self.camera_params is not None:
            self.K = np.array(self.camera_params['K'], dtype=np.float64).reshape(3, 3)
            self.R = np.array(self.camera_params['R'], dtype=np.float64).reshape(3, 1)
            self.T = np.array(self.camera_params['T'], dtype=np.float64).reshape(3, 1)


def moving(tag_id, distance):
    for i in range(tag_id):
        hiwonder.buzzer.on()
        rospy.sleep(0.1)
        hiwonder.buzzer.off()
        rospy.sleep(0.1)
    rospy.sleep(0.8)
    hiwonder.pwm_servo1.set_position(100, 0.5)
    rospy.sleep(2)
    jetmax.set_position((120, 0, 180), 1.5)
    rospy.sleep(1.6)
    if tag_id == 1:
        jetmax.set_position((120, 0, 150), 0.7)
        rospy.sleep(0.7)
    elif tag_id == 2:
        jetmax.set_position((120, 0, 50), 1.2)
        rospy.sleep(1.2)
    else:
        pass
    cur = list(jetmax.position)
    cur[0] += 70
    jetmax.set_position(cur, 1)
    rospy.sleep(1)
    hiwonder.pwm_servo1.set_position(130, 0.5)
    rospy.sleep(1)
    cur = list(jetmax.position)
    cur[0] -= 70
    jetmax.set_position(cur, 1)
    rospy.sleep(1)
    jetmax.go_home(2)
    rospy.sleep(2)
    state.runner = None


def image_proc_a(img):
    if state.runner is not None:
        return img
    frame_gray = cv2.cvtColor(np.copy(img), cv2.COLOR_RGB2GRAY)  # 将画面转为灰度图
    params = [state.K[0][0], state.K[1][1], state.K[0][2], state.K[1][2]]  # 相机内参
    tags = at_detector.detect(frame_gray, estimate_tag_pose=True, camera_params=params, tag_size=TAG_SIZE)  # 进行AprilTag的检测
    if not tags:
        hiwonder.buzzer.off()
    for tag in tags:
        corners = tag.corners.reshape(1, -1, 2).astype(int)  # 检测到的AprilTag的四个角的点
        center = tag.center.astype(int)  # AprilTag中心点

        cv2.drawContours(img, corners, -1, (255, 0, 0), 3)  # 画出外框
        cv2.circle(img, tuple(center), 5, (255, 255, 0), 10)  # 画出中心点

        point_3d = np.array([[16.65, -16.65, 0], 
            [-16.65,-16.65, 0], 
            [-16.65, 16.65, 0], 
            [16.65, 16.65, 0]], dtype=np.double)
        point_2d = np.array([tag.corners[0].astype(int),
                             tag.corners[1].astype(int),
                             tag.corners[2].astype(int),
                             tag.corners[3].astype(int)],
                             dtype=np.double)

        dist_coefs = np.array([0,0,0,0], dtype=np.double)
        found, rvec, tvec = cv2.solvePnP(point_3d, point_2d, state.K,  None)
        rotM = cv2.Rodrigues(rvec)[0]
        camera_position = -np.matrix(rotM).T * np.matrix(tvec)
        distance = -camera_position.T.tolist()[0][2]
        print("TAG_ID:{}, Distance: {:0.2f}mm".format(tag.tag_id, distance))
        if distance < 100 and tag.tag_id < 3:
            state.runner = threading.Thread(target=moving, args=(tag.tag_id, distance), daemon=True)
            state.runner.start()
            break


    img_h, img_w = img.shape[:2]
    cv2.line(img, (int(img_w / 2 - 10), int(img_h / 2)), (int(img_w / 2 + 10), int(img_h / 2)), (0, 255, 255), 2)
    cv2.line(img, (int(img_w / 2), int(img_h / 2 - 10)), (int(img_w / 2), int(img_h / 2 + 10)), (0, 255, 255), 2)
    return img


def image_proc_b():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    frame_result = image.copy()
    frame_result = image_proc_a(frame_result)
    bgr_image = cv2.cvtColor(frame_result, cv2.COLOR_RGB2BGR)
    cv2.imshow('result', bgr_image)
    cv2.waitKey(1)


def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass


if __name__ == '__main__':
    state = AprilTagDetect()
    jetmax = hiwonder.JetMax()
    sucker = hiwonder.Sucker()
    at_detector = apriltag.Detector()
    image_queue = queue.Queue(maxsize=1)
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    jetmax.go_home()
    hiwonder.pwm_servo1.set_position(130, 0.5)
    rospy.sleep(1)
    state.load_camera_params()
    if state.camera_params is None:
        rospy.logerr('Can not load camera parameters')
        sys.exit(-1)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)
    while not rospy.is_shutdown():
        image_proc_b()
