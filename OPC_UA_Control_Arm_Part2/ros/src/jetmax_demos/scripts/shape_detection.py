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
import apriltag
import yaml

ROS_NODE_NAME = "shape_detector"
IMAGE_PROC_SIZE = 640, 480
TAG_SIZE = 33.30
TARGET_POSITIONS = (((238, -70, 95), -18), ((238, -70, 135), -18), ((238, -70, 185), -18))


def camera_to_world(cam_mtx, r, t, img_points):
    inv_k = np.asmatrix(cam_mtx).I
    r_mat = np.zeros((3, 3), dtype=np.float64)
    cv2.Rodrigues(r, r_mat)
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


class ShapDetect:
    def __init__(self):
        self.is_running = False
        self.moving_block = None
        self.image_sub = None
        self.runner = None
        self.count = 0
        self.level = 0
        self.lock = threading.RLock()
        self.camera_params = None
        self.K = None
        self.R = None
        self.T = None

    def reset(self):
        self.is_running = False
        self.moving_block = None
        self.image_sub = None
        self.runner = None
        self.count = 0
        self.level = 0

    def load_camera_params(self):
        self.camera_params = rospy.get_param('/camera_cal/block_params', self.camera_params)
        if self.camera_params is not None:
            self.K = np.array(self.camera_params['K'], dtype=np.float64).reshape(3, 3)
            self.R = np.array(self.camera_params['R'], dtype=np.float64).reshape(3, 1)
            self.T = np.array(self.camera_params['T'], dtype=np.float64).reshape(3, 1)


def rotation_mtx_to_euler(R):
    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
    singular = sy < 1e-6
    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0
    return np.array([x, y, z])


def image_proc(img):
    frame_gray = cv2.cvtColor(np.copy(img), cv2.COLOR_RGB2GRAY)  # 将画面转为灰度图
    _, thresh = cv2.threshold(frame_gray, 127, 255, cv2.THRESH_BINARY)  # 二值化
    # 平滑
    eroded = cv2.erode(thresh, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    # 获取轮廓
    contours = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2]
    # 去除小面积轮廓
    contours = list(filter(lambda c: math.fabs(cv2.contourArea(c)) > 500, contours))

    # 遍历所有轮廓
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)  # 对轮廓曲线进行多边形拟合
        cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)  # 画出轮廓
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        # 根据输出的点数判断形状
        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # 三角形
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            print(aspect_ratio)
            # 计算长宽比来1确定时正方形还是长方形
            if 0.90 <= aspect_ratio < 1.1:
                cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # 正方形
            else:
                cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # 长方形
        elif len(approx) == 5:
            cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # #五边形
        elif len(approx) == 10:
            cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # 五角星
        else:
            cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # 圆形

    img_h, img_w = img.shape[:2]
    cv2.line(img, (int(img_w / 2 - 10), int(img_h / 2)), (int(img_w / 2 + 10), int(img_h / 2)), (0, 255, 255), 2)
    cv2.line(img, (int(img_w / 2), int(img_h / 2 - 10)), (int(img_w / 2), int(img_h / 2 + 10)), (0, 255, 255), 2)
    return img


def image_callback(ros_image):
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    frame_result = image.copy()
    frame_result = image_proc(frame_result)
    bgr_image = cv2.cvtColor(frame_result, cv2.COLOR_RGB2BGR)
    cv2.imshow('result', bgr_image)
    cv2.waitKey(1)


if __name__ == '__main__':
    state = ShapDetect()
    jetmax = hiwonder.JetMax()
    sucker = hiwonder.Sucker()
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
    try:
        rospy.spin()
    except KeyboardInterrupt:
        sys.exit(0)
