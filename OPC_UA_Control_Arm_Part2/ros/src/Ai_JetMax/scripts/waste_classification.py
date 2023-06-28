#!/usr/bin/env python3
import os
import sys
import cv2
import math
import rospy
import numpy as np
import threading
import queue
import hiwonder
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest
from std_srvs.srv import Empty
from std_msgs.msg import Bool
from jetmax_control.msg import SetServo
from yolov5_tensorrt import Yolov5TensorRT

ROS_NODE_NAME = "waste_classification_1"

TRT_ENGINE_PATH = os.path.join(sys.path[0], "models/waste_v5_160.trt")
TRT_INPUT_SIZE = 160
TRT_CLASS_NAMES = ('Banana Peel', 'Broken Bones', 'Cigarette End', 'Disposable Chopsticks',
                   'Ketchup', 'Marker', 'Oral Liquid Bottle', 'Plate',
                   'Plastic Bottle', 'Storage Battery', 'Toothbrush', 'Umbrella')
TRT_NUM_CLASSES = 12
WASTE_CLASSES = {
    'food_waste': ('Banana Peel', 'Broken Bones', 'Ketchup'),
    'hazardous_waste': ('Marker', 'Oral Liquid Bottle', 'Storage Battery'),
    'recyclable_waste': ('Plastic Bottle', 'Toothbrush', 'Umbrella'),
    'residual_waste': ('Plate', 'Cigarette End', 'Disposable Chopsticks'),
}
COLORS = {
    'recyclable_waste': (0, 0, 255),
    'hazardous_waste': (255, 0, 0),
    'food_waste': (0, 255, 0),
    'residual_waste': (80, 80, 80)
}

TARGET_POSITION = {
    'recyclable_waste': (170, -65, 65, 65),
    'hazardous_waste': (170, -15, 65, 85),
    'food_waste': (170, 35, 65, 100),
    'residual_waste': (170, 85, 65, 118)
}


def image_proc():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    outputs = yolov5.detect(image)
    boxes, confs, classes = yolov5.post_process(image, outputs, 0.65)
    width = image.shape[1]
    height = image.shape[0]
    cards = []
    for box, cls_conf, cls_id in zip(boxes, confs, classes):
        x1 = int(box[0] / TRT_INPUT_SIZE * width)
        y1 = int(box[1] / TRT_INPUT_SIZE * height)
        x2 = int(box[2] / TRT_INPUT_SIZE * width)
        y2 = int(box[3] / TRT_INPUT_SIZE * height)
        waste_name = TRT_CLASS_NAMES[cls_id]
        waste_class_name = ''
        for k, v in WASTE_CLASSES.items():
            if waste_name in v:
                waste_class_name = k
                break
        cards.append((cls_conf, x1, y1, x2, y2, waste_class_name))
        cv2.putText(image, waste_class_name, (x1, y1 - 25),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS[waste_class_name], 2)
        cv2.putText(image, waste_name + "{:0.2f}".format(float(cls_conf)), (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS[waste_class_name], 2)
        cv2.rectangle(image, (x1, y1), (x2, y2), COLORS[waste_class_name], 3)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('result', image)
    cv2.waitKey(1)



def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    image_queue = queue.Queue(maxsize=2)
    jetmax = hiwonder.JetMax()
    jetmax.go_home(2)
    rospy.sleep(2)
    yolov5 = Yolov5TensorRT(TRT_ENGINE_PATH, TRT_INPUT_SIZE, TRT_NUM_CLASSES)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)
    while not rospy.is_shutdown():
        image_proc()
