#!/usr/bin/env python3
import sys
import cv2
import math
import time
import rospy
import numpy as np
import threading
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest
from std_srvs.srv import Empty
from jetmax_control.msg import SetServo
import hiwonder
import queue
import pupil_apriltags as apriltag
import yaml


"""
Apriltag 识别定位实验
将jetmax调整到摄像头朝下的形态
将id1及其他id的apriltag放于摄像头下方， 程序将识别apriltag并计算其他tag相对与id1的tag的位置
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
            self.T = np.array(self.camera_params['T'], dtype=np.float64).reshape(3, 1)
            self.R = np.array(self.camera_params['R'], dtype=np.float64).reshape(3, 1)
            r_mat = np.zeros((3, 3), dtype=np.float64)
            cv2.Rodrigues(self.R, r_mat)
            self.r_mat = r_mat

def camera_to_world(cam_mtx, r_mat, t, img_points):
    """
    通过图片坐标及相机内外参计算现实位置
    """
    inv_k = np.asmatrix(cam_mtx).I
    # invR * T
    inv_r = np.asmatrix(r_mat).I  # 3*3
    transPlaneToCam = np.dot(inv_r, np.asmatrix(t))  # 3*3 dot 3*1 = 3*1
    world_pt = []
    coords = np.zeros((3, 1), dtype=np.float64)
    for img_pt in img_points:
        coords[0][0] = img_pt[0][0]
        coords[1][0] = img_pt[0][1]
        coords[2][0] = 1.0
        worldPtCam = np.dot(inv_k, coords)  # 3*3 dot 3*1 = 3*1
        # [x,y,1] * invR
        worldPtPlane = np.dot(inv_r, worldPtCam)  # 3*3 dot 3*1 = 3*1
        # zc
        scale = transPlaneToCam[2][0] / worldPtPlane[2][0]
        # zc * [x,y,1] * invR
        scale_worldPtPlane = np.multiply(scale, worldPtPlane)
        # [X,Y,Z]=zc*[x,y,1]*invR - invR*T
        worldPtPlaneReproject = np.asmatrix(scale_worldPtPlane) - np.asmatrix(transPlaneToCam)  # 3*1 dot 1*3 = 3*3
        pt = np.zeros((3, 1), dtype=np.float64)
        pt[0][0] = worldPtPlaneReproject[0][0]
        pt[1][0] = worldPtPlaneReproject[1][0]
        pt[2][0] = 0
        world_pt.append(pt.T.tolist())
    return world_pt

def image_proc_a(img):
    frame_gray = cv2.cvtColor(np.copy(img), cv2.COLOR_RGB2GRAY)  # 将画面转为灰度图
    params = [state.K[0][0], state.K[1][1], state.K[0][2], state.K[1][2]]  # 相机内参
    tags = at_detector.detect(frame_gray, estimate_tag_pose=True, camera_params=params, tag_size=TAG_SIZE)  # 进行AprilTag的检测
    for tag in tags:
        corners = tag.corners.reshape(1, -1, 2).astype(int)  # 检测到的AprilTag的四个角的点
        center = tag.center.astype(int)  # AprilTag中心点

        cv2.drawContours(img, corners, -1, (255, 0, 0), 3)  # 画出外框
        cv2.circle(img, tuple(center), 5, (255, 255, 0), 10)  # 画出中心点

        rotM = tag.pose_R
        tvec = tag.pose_t

        if tag.tag_id == 1:  #如果是id1就将外参保存起来
            state.r_mat = rotM
            state.T = tvec
        else: 
            #如果如果不是id1 就计算相关对位置
            x, y, _ = camera_to_world(state.K, state.r_mat, state.T, tag.center.reshape((1,1,2)))[0][0]
            #计算欧拉角
            theta_z = math.atan2(rotM[1, 0], rotM[0, 0])*180.0/math.pi
            theta_y = math.atan2(-1.0*rotM[2, 0], math.sqrt(rotM[2, 1]**2 + rotM[2, 2]**2))*180.0/math.pi
            theta_x = math.atan2(rotM[2, 1], rotM[2, 2])*180.0/math.pi
            print("id:{}, x:{:0.2f}mm, y:{:0.2f}mm, angle:{:0.2f}deg".format(tag.tag_id, x, y, theta_z))
            s1 = "id:{}".format(tag.tag_id)
            s2 = "x:{:0.2f}mm, y:{:0.2f}mm".format(x, y)
            s3 = "angle:{:0.2f}deg".format(theta_z)
            cv2.putText(img, s1, (center[0] - 50, center[1]), 0, 0.7, (0, 255, 0), 2)
            cv2.putText(img, s2, (center[0] - 50, center[1]+20), 0, 0.7, (0, 255, 0), 2)
            cv2.putText(img, s3, (center[0] - 50, center[1] + 40), 0, 0.7, (0, 255, 0), 2)


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
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback, queue_size=1)
    if state.camera_params is None:
        rospy.logerr('Can not load camera parameters')
        sys.exit(-1)
    while not rospy.is_shutdown():
        image_proc_b()
