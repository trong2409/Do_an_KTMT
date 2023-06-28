#!/usr/bin/env python3
import os
import sys
import cv2
import math
import time
import queue
import random
import threading
import numpy as np
import rospy
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest
import hiwonder
from hiwonder import serial_servo as ss
from yolov5_tensorrt import Yolov5TensorRT


ROS_NODE_NAME = "hiwjfkalsdjfkla"
IMAGE_SIZE = 640, 480
CHARACTERS_ENGINE_PATH = os.path.join(sys.path[0], 'models/characters_v5_160.trt')
CHARACTER_LABELS = tuple([i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
CHARACTER_NUM = 26
TRT_INPUT_SIZE = 160
COLORS = tuple([tuple([random.randint(10, 255) for j in range(3)]) for i in range(CHARACTER_NUM)])
TARGET_POSITION = (-200, -180, 65)
yolov5_chars = Yolov5TensorRT(CHARACTERS_ENGINE_PATH, TRT_INPUT_SIZE, CHARACTER_NUM)


def image_proc(img_in):
    result_image = cv2.cvtColor(img_in, cv2.COLOR_RGB2BGR)

    outputs = yolov5_chars.detect(np.copy(img_in))
    boxes, confs, classes = yolov5_chars.post_process(img_in, outputs, 0.60)

    for box, cls_id, cls_conf in zip(boxes, classes, confs):
        x1 = box[0] / TRT_INPUT_SIZE * 640
        y1 = box[1] / TRT_INPUT_SIZE * 480
        x2 = box[2] / TRT_INPUT_SIZE * 640
        y2 = box[3] / TRT_INPUT_SIZE * 480
        char = CHARACTER_LABELS[cls_id]
        cv2.putText(result_image, char + " " + str(float(cls_conf))[:4], (int(x1), int(y1) - 5),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS[cls_id], 2)
        cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), COLORS[cls_id], 3)
        print(x1, y1, x2, y2, char)

    return result_image


def show_fps(img=None):
    global fps, fps_t0
    """Draw fps number at top-left corner of the image."""
    # fps cal
    fps_t1 = time.time()
    fps_cur = (1.0 / (fps_t1 - fps_t0))
    fps = fps_cur if fps == 0.0 else (fps * 0.8 + fps_cur * 0.2)
    fps_t0 = fps_t1

    font = cv2.FONT_HERSHEY_PLAIN
    line = cv2.LINE_AA
    fps_text = 'FPS: {:.2f}'.format(fps)
    if img is not None:
        cv2.putText(img, fps_text, (11, 20), font, 1.0, (32, 32, 32), 4, line)
        cv2.putText(img, fps_text, (10, 20), font, 1.0, (240, 240, 240), 1, line)
    return img


def image_proc_b():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    result_img = image_proc(image)
    show_fps(result_img)
    cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
    cv2.imshow(ROS_NODE_NAME, result_img)
    cv2.waitKey(1)


def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass


if __name__ == '__main__':
    fps_t0 = time.time()
    fps = 0
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    image_queue = queue.Queue(maxsize=1)
    jetmax = hiwonder.JetMax()
    jetmax.go_home()
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)  # 订阅摄像头画面
    while not rospy.is_shutdown():
        image_proc_b()
