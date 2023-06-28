#!/usr/bin/env python3
import sys
import cv2
import math
import numpy as np
from sensor_msgs.msg import Image
import hiwonder
import rospy

ROS_NODE_NAME = "color_detect"

def image_proc(img):
    img_h, img_w = img.shape[:2]
    frame_gb = cv2.GaussianBlur(np.copy(img), (5, 5), 5)
    frame_lab = cv2.cvtColor(frame_gb, cv2.COLOR_RGB2LAB)  # 转换rgb到lab

    blocks = []
    for color_name, color in target_colors.items():  # 遍历所有颜色阈值
        frame_mask = cv2.inRange(frame_lab, tuple(color['min']), tuple(color['max']))
        eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
        contour_area = map(lambda c: (c, math.fabs(cv2.contourArea(c))), contours)
        contour_area = list(filter(lambda c: c[1] > 1200, contour_area))  # 去除过小的色块

        if len(contour_area) > 0:
            for contour, area in contour_area:  # Loop through all the contours found
                (center_x, center_y), r = cv2.minEnclosingCircle(contour)
                cv2.circle(img, (int(center_x), int(center_y)), 1, hiwonder.COLORS[color_name.upper()], 5)
                cv2.circle(img, (int(center_x), int(center_y)), int(r), hiwonder.COLORS[color_name.upper()], 2)
                cv2.putText(img, color_name.upper(), (int(center_x), int(center_y)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

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


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    jetmax = hiwonder.JetMax()
    jetmax.go_home()
    rospy.sleep(1)
    target_colors = rospy.get_param('/lab_config_manager/color_range_list', {})
    del[target_colors['white']]
    del[target_colors['black']]
    image_sub = rospy.Subscriber("/usb_cam/image_rect_color", Image, image_callback, queue_size=1)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        sys.exit(0)
