#!/usr/bin/env python3
import sys
import cv2
import math
import time
import numpy as np
from sensor_msgs.msg import Image
import hiwonder
import threading
import rospy

"""
17 超声波+识别抓取 (测距识别)
"""

ROS_NODE_NAME = "color_detect"


def moving(block):
    global runner
    (x, y), r, color_name = block
    if color_name == 'red':
        hiwonder.sonar.set_color(0, 0xFF0000)
        hiwonder.sonar.set_color(1, 0xFF0000)
    if color_name == 'green':
        hiwonder.sonar.set_color(0, 0x00FF00)
        hiwonder.sonar.set_color(1, 0x00FF00)
    if color_name == 'blue':
        hiwonder.sonar.set_color(0, 0x0000FF)
        hiwonder.sonar.set_color(1, 0x0000FF)
    hiwonder.buzzer.on()
    rospy.sleep(0.1)
    hiwonder.buzzer.off()
    rospy.sleep(1)
    hiwonder.pwm_servo1.set_position(100, 0.5)
    rospy.sleep(2)
    if color_name == 'red':
        jetmax.set_position((238, 80, 130), 2)
        rospy.sleep(2)
    elif color_name == 'green':
        jetmax.set_position((238, 30, 130), 1.8)
        rospy.sleep(1.8)
    elif color_name == 'blue':
        jetmax.set_position((238, -20, 130), 1.6)
        rospy.sleep(1.6)
    else:
        pass
    cur = list(jetmax.position)
    cur[2] = 85
    jetmax.set_position(cur, 1)
    hiwonder.pwm_servo1.set_position(130, 0.5)
    rospy.sleep(1)
    cur[2] = 150
    jetmax.set_position(cur, 1.2)
    rospy.sleep(2)
    jetmax.go_home(2)
    rospy.sleep(2)
    hiwonder.sonar.set_color(0, 0)
    hiwonder.sonar.set_color(1, 0)
    runner = None

def image_proc(img):
    global runner
    img_h, img_w = img.shape[:2]
    frame_gb = cv2.GaussianBlur(np.copy(img), (5, 5), 5)
    frame_lab = cv2.cvtColor(frame_gb, cv2.COLOR_RGB2LAB)  # 转换rgb到lab

    blocks = []
    frame_roi = frame_lab[0:280, 140:500]
    cv2.line(img, (140, 0), (140, 280), (255, 0, 0), 2)
    cv2.line(img, (140, 280), (500, 280), (255, 0, 0), 2)
    cv2.line(img, (500, 280), (500, 0), (255, 0, 0), 2)
    cv2.line(img, (500, 0), (140, 0), (255, 0, 0), 2)
    cv2.putText(img, "D:{:0.2f}mm".format(distance), (0, 440), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 2)
    if runner is not None:
        return img

    if distance < 70:
        for color_name, color in target_colors.items():  # 遍历所有颜色阈值
            frame_mask = cv2.inRange(frame_roi, tuple(color['min']), tuple(color['max']))
            eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
            dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
            contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
            contour_area = map(lambda c: (c, math.fabs(cv2.contourArea(c))), contours)
            contour_area = list(filter(lambda c: c[1] > 1200, contour_area))  # 去除过小的色块

            if len(contour_area) > 0:
                for contour, area in contour_area:  # Loop through all the contours found
                    (center_x, center_y), r = cv2.minEnclosingCircle(contour)
                    cv2.circle(img, (int(center_x + 140), int(center_y)), 1, hiwonder.COLORS[color_name.upper()], 5)
                    cv2.circle(img, (int(center_x + 140), int(center_y)), int(r), hiwonder.COLORS[color_name.upper()], 2)
                    cv2.putText(img, color_name.upper(), (int(center_x + 140), int(center_y)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)
                        
                    blocks.append(((center_x, center_y), r, color_name))
        if len(blocks) > 0:
            block = max(blocks, key=lambda x: x[1])
            runner = threading.Thread(target=moving, args=(block,), daemon=True)
            runner.start()

    cv2.line(img, (int(img_w / 2 - 10), int(img_h / 2)), (int(img_w / 2 + 10), int(img_h / 2)), (0, 255, 255), 2)
    cv2.line(img, (int(img_w / 2), int(img_h / 2 - 10)), (int(img_w / 2), int(img_h / 2 + 10)), (0, 255, 255), 2)
    return img


def image_callback(ros_image):
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    frame_result = np.copy(image)
    frame_result = image_proc(frame_result)
    image_bgr = cv2.cvtColor(frame_result, cv2.COLOR_RGB2BGR)
    cv2.imshow("result", image_bgr)
    cv2.waitKey(1)

def distance_update():
    global distance
    t = time.time()
    while True:
        d = hiwonder.sonar.get_distance()
        distance = d if distance is None else d * 0.4 + distance * 0.6
        if t < time.time():
            print("Distance:{:0.2f}mm".format(distance))
            t = time.time() + 1
        rospy.sleep(0.05)



if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    jetmax = hiwonder.JetMax()
    jetmax.go_home()
    hiwonder.pwm_servo1.set_position(130, 0.5)
    rospy.sleep(1)
    distance = None
    runner = None
    colors = rospy.get_param('/lab_config_manager/color_range_list', {})
    target_colors = {}
    target_colors['red'] = colors['red']
    target_colors['green'] = colors['green']
    target_colors['blue'] = colors['blue']
    image_sub = rospy.Subscriber("/usb_cam/image_rect_color", Image, image_callback, queue_size=1)
    sonar_thread = threading.Thread(target=distance_update, daemon=True)
    sonar_thread.start()
    hiwonder.sonar.set_color(0, 0x0)
    hiwonder.sonar.set_color(1, 0x0)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        sys.exit(0)
