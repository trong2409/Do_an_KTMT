#!/usr/bin/env python3
import math
import rospy
import time
import queue
import threading
from sensor_msgs.msg import Image
import cv2
import numpy as np
import hiwonder
import sys

ROS_NODE_NAME = 'mecanum_ball_tracking'
DEFAULT_X, DEFAULT_Y, DEFAULT_Z = 0, 100 + 8.14, 0
ORG_PIXEL_X, ORG_PIXEL_Y = 320, 240

en_mot = hiwonder.motor.EncoderMotorController(1, 3)
hiwonder.pwm_servo1.set_position(50, 100)
hiwonder.pwm_servo1.set_position(50, 100)


class BallTracking:
    def __init__(self):
        self.lock = threading.RLock()
        self.servo_x = 500
        self.servo_y = 500

        self.color_x_pid = hiwonder.PID(0.15, 0.005, 0.0005)
        self.color_y_pid = hiwonder.PID(0.15, 0.005, 0.0005)

        self.target_color_range = None
        self.target_color_name = None
        self.last_color_circle = None
        self.lost_target_count = 0

        self.is_running = False

        self.fps = 0.0
        self.tic = time.time()


def ball_tracking(image):
    org_image = np.copy(image)
    image = cv2.resize(image, (320, 240))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)  # RGB转LAB空间
    image = cv2.GaussianBlur(image, (5, 5), 5)

    with state.lock:
        target_color_range = state.target_color_range
        target_color_name = state.target_color_name

    if target_color_range is not None:
        mask = cv2.inRange(image, tuple(target_color_range['min']), tuple(target_color_range['max']))  # 二值化
        eroded = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  # 腐蚀
        dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  # 膨胀
        contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # 找出轮廓
        contour_area = map(lambda c: (c, math.fabs(cv2.contourArea(c))), contours)  # 计算各个轮廓的面积
        contour_area = list(filter(lambda c: c[1] > 100, contour_area))  # 剔除>面积过小的轮廓
        circle = None
        if len(contour_area) > 0:
            if state.last_color_circle is None:
                contour, area = max(contour_area, key=lambda c_a: c_a[1])
                circle = cv2.minEnclosingCircle(contour)
            else:
                (last_x, last_y), last_r = state.last_color_circle
                circles = map(lambda c: cv2.minEnclosingCircle(c[0]), contour_area)
                circle_dist = list(map(lambda c: (c, math.sqrt(((c[0][0] - last_x) ** 2) + ((c[0][1] - last_y) ** 2))),
                                       circles))
                circle, dist = min(circle_dist, key=lambda c: c[1])
                if dist < 100:
                    circle = circle

        if circle is not None:
            state.lost_target_count = 0
            (x, y), r = circle
            x = x / 320 * 640
            y = y / 240 * 480
            r = r / 320 * 640
            org_image = cv2.circle(org_image, (int(x), int(y)), int(r), (255, 0, 0), 2)
            vx = 0
            vy = 0
            vw = 0
            if abs(x - ORG_PIXEL_X) > 20:
                state.color_x_pid.update(x - ORG_PIXEL_X)
                vx = state.color_x_pid.output
            print(circle)
            if abs(r - 50) > 5:
                if r - 50 < 0:
                    state.color_y_pid.setKp(3.0)
                else:
                    state.color_y_pid.setKp(0.8)
                state.color_y_pid.update(r - 50)
                vy = -state.color_y_pid.output
            # 计算合速度
            vw1 = vy - vx + vw * (1 + 2)
            vw2 = vy + vx - vw * (1 + 2)
            vw3 = vy - vx - vw * (1 + 2)
            vw4 = vy + vx + vw * (1 + 2)

            vw1 = 100 if vw1 > 100 else vw1
            vw2 = 100 if vw1 > 100 else vw2
            vw3 = 100 if vw1 > 100 else vw3
            vw4 = 100 if vw1 > 100 else vw4
            vw1 = -100 if vw1 < -100 else vw1
            vw2 = -100 if vw1 < -100 else vw2
            vw3 = -100 if vw1 < -100 else vw3
            vw4 = -100 if vw1 < -100 else vw4

            en_mot.set_speed(int(vw1), 1)
            en_mot.set_speed(int(-vw4), 2)
            en_mot.set_speed(int(-vw2), 3)
            en_mot.set_speed(int(vw3), 4)

        else:
            state.lost_target_count += 1
            if state.lost_target_count > 2:
                state.color_x_pid.update(0)
                state.color_y_pid.update(0)
                en_mot.set_speed(int(0), 1)
                en_mot.set_speed(int(0), 2)
                en_mot.set_speed(int(0), 3)
                en_mot.set_speed(int(0), 4)
                state.lost_target_count = 0
            state.last_color_circle = None
    return org_image


def image_callback(ros_image):
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    frame_result = ball_tracking(image)
    toc = time.time()
    curr_fps = 1.0 / (state.tic - toc)
    state.fps = curr_fps if state.fps == 0.0 else (state.fps * 0.95 + curr_fps * 0.05)
    state.tic = toc
    frame_result = cv2.cvtColor(frame_result, cv2.COLOR_RGB2BGR)
    cv2.imshow(ROS_NODE_NAME, frame_result)
    cv2.waitKey(1)


def set_target(color_name):
    color_ranges = rospy.get_param('/lab_config_manager/color_range_list', {})
    rospy.logdebug(color_ranges)
    with state.lock:
        if color_name in color_ranges:
            state.target_color_name = color_name
            state.target_color_range = color_ranges[color_name]
        else:
            state.target_color_name = None
            state.target_color_range = None


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    state = BallTracking()
    jetmax = hiwonder.JetMax()
    jetmax.set_position((jetmax.ORIGIN[0], -100, 0), 1.5)
    rospy.sleep(1.5)
    image_queue = queue.Queue(maxsize=3)
    set_target('tennis')
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)  # 订阅摄像头画面
    try:
        rospy.spin()
    except:
        sys.exit(0)
