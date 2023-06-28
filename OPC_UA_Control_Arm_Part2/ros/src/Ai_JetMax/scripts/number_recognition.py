#!/usr/bin/env python3
import os
import sys
import cv2
import math
import rospy
import numpy as np
from sensor_msgs.msg import Image
import queue
import hiwonder
from yolov5_tensorrt import Yolov5TensorRT
import random
import threading

ROS_NODE_NAME = "virtual_calculator"
TRT_ENGINE_PATH = os.path.join(sys.path[0], "models/numbers_v5_160.trt")
TRT_INPUT_SIZE = 160
TRT_CLASS_NAMES = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=')
TRT_NUM_CLASSES = 15
COLORS = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(TRT_NUM_CLASSES)]


def image_proc_a():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    outputs = yolov5.detect(image)
    boxes, confs, classes = yolov5.post_process(image, outputs, 0.6)
    width = image.shape[1]
    height = image.shape[0]
    for box, cls_conf, cls_id in zip(boxes, confs, classes):
        x1 = int(box[0] / TRT_INPUT_SIZE * width)
        y1 = int(box[1] / TRT_INPUT_SIZE * height)
        x2 = int(box[2] / TRT_INPUT_SIZE * width)
        y2 = int(box[3] / TRT_INPUT_SIZE * height)
        card_name = str(TRT_CLASS_NAMES[cls_id])
        cv2.putText(image, card_name + " " + str(float(cls_conf))[:4], (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, COLORS[cls_id], 2)
        cv2.rectangle(image, (x1, y1), (x2, y2), COLORS[cls_id], 2)
        print(x1, y1, x2, y2, card_name)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow(ROS_NODE_NAME, image)
    cv2.waitKey(1)


def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    yolov5 = Yolov5TensorRT(TRT_ENGINE_PATH, TRT_INPUT_SIZE, TRT_NUM_CLASSES)
    jetmax = hiwonder.JetMax()
    jetmax.go_home(2)
    rospy.sleep(2)
    image_queue = queue.Queue(maxsize=1)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback, queue_size=1)  # Subscribe to the camera
    while not rospy.is_shutdown():
        image_proc_a()
