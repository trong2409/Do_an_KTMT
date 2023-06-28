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
探测Apriltag
"""

ROS_NODE_NAME = "apriltag_detector"
TAG_SIZE = 33.30


class AprilTagDetect:
    def __init__(self):
        self.camera_params = None
        self.K = None
        self.R = None
        self.T = None


    def load_camera_params(self):
        self.camera_params = rospy.get_param('/camera_cal/block_params', self.camera_params)
        if self.camera_params is not None:
            self.K = np.array(self.camera_params['K'], dtype=np.float64).reshape(3, 3)
            self.R = np.array(self.camera_params['R'], dtype=np.float64).reshape(3, 1)
            self.T = np.array(self.camera_params['T'], dtype=np.float64).reshape(3, 1)


def image_proc_a(img):
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
        print("tag id: {}, center: x:{} y:{}".format(tag.tag_id, center[0], center[1]))


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
    state.load_camera_params()
    if state.camera_params is None:
        rospy.logerr('Can not load camera parameters')
        sys.exit(-1)
    rospy.ServiceProxy('/jetmax/go_home', Empty)()
    rospy.Publisher('/jetmax/end_effector/sucker/command', Bool, queue_size=1).publish(data=False)
    rospy.Publisher('/jetmax/end_effector/servo1/command', SetServo, queue_size=1).publish(data=90, duration=0.5)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)
    while not rospy.is_shutdown():
        image_proc_b()
