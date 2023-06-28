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
import tm1640

ROS_NODE_NAME = "face_mask"

DEFAULT_X, DEFAULT_Y, DEFAULT_Z = hiwonder.JetMax.ORIGIN
FACEMASK_ENGINE_PATH = os.path.join(sys.path[0], 'models/facemask_v5_160.trt')
CLASSNUM = 2
TRT_INPUT_SIZE = 160
FACEMASK_LABELS = ("nomask", "mask")
COLORS = ((255, 0, 0), (0, 0, 255))
IMAGE_SIZE = 640, 480


def draw_cross():
    tm1640.display_buf = [0] * 16
    for i in range(0, 8):
        tm1640.set_bit(i, i, 1)
        tm1640.set_bit(i, 7 - i, 1)

    for i in range(8, 16):
        tm1640.set_bit(i, i - 8, 1)
        tm1640.set_bit(i, 7 - (i - 8), 1)
    tm1640.update_display()


def draw_smail():
    tm1640.display_buf = [0] * 16
    tm1640.set_bit(5, 1, 1)
    tm1640.set_bit(5, 2, 1)
    tm1640.set_bit(6, 1, 1)
    tm1640.set_bit(6, 2, 1)
    tm1640.set_bit(10, 1, 1)
    tm1640.set_bit(10, 2, 1)
    tm1640.set_bit(9, 1, 1)
    tm1640.set_bit(9, 2, 1)

    for i in range(5, 11):
        tm1640.set_bit(i, 7, 1)

    tm1640.set_bit(11, 6, 1)
    tm1640.set_bit(12, 5, 1)

    tm1640.set_bit(3, 5, 1)
    tm1640.set_bit(4, 6, 1)
    tm1640.update_display()


def clear_disp():
    tm1640.display_buf = [0] * 16
    tm1640.update_display()


def moving():
    hiwonder.motor2.set_speed(0)
    jetmax.set_position((-DEFAULT_Y, DEFAULT_X, DEFAULT_Z), 1.5)
    rospy.sleep(1.5)
    hiwonder.motor1.set_speed(100)
    jetmax.set_position((-DEFAULT_Y, DEFAULT_X, 60), 0.8)
    rospy.sleep(1.2)
    jetmax.set_position((-DEFAULT_Y, DEFAULT_X, DEFAULT_Z), 1)
    rospy.sleep(1)
    jetmax.set_position((DEFAULT_X, DEFAULT_Y, DEFAULT_Z), 1.5)
    rospy.sleep(1.5)
    rospy.sleep(4)

    clear_disp()
    draw_smail()
    jetmax.set_position((DEFAULT_X, DEFAULT_Y, DEFAULT_Z - 50), 300)
    rospy.sleep(0.3)
    jetmax.set_position((DEFAULT_X, DEFAULT_Y, DEFAULT_Z), 300)
    rospy.sleep(0.3)
    jetmax.set_position((DEFAULT_X, DEFAULT_Y, DEFAULT_Z - 50), 300)
    rospy.sleep(0.3)
    jetmax.set_position((DEFAULT_X, DEFAULT_Y, DEFAULT_Z), 300)


def image_proc_a(img_in):
    global runner, count
    outputs = yolov5_chars.detect(img_in)
    boxes, confs, classes = yolov5_chars.post_process(img_in, outputs, 0.6, 0.2)
    facex = []
    width, height = IMAGE_SIZE
    result_image = img_in
    no_mask = False
    mask = False
    for box, cls_id, cls_conf in zip(boxes, classes, confs):
        x1 = box[0] / TRT_INPUT_SIZE * width
        y1 = box[1] / TRT_INPUT_SIZE * height
        x2 = box[2] / TRT_INPUT_SIZE * width
        y2 = box[3] / TRT_INPUT_SIZE * height

        '''
        if x2 - x1 > y2 - y1:
            x1 = int(((x1 + x2) / 2) - ((y2 - y1) / 2))
            x2 = x1 + (y2 - y1)
        '''

        facex.append((x1, y1, x2, y2, cls_id, cls_conf))
        result_image = cv2.putText(img_in, FACEMASK_LABELS[cls_id] + " " + str(float(cls_conf))[:4],
                                   (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS[cls_id], 2)
        result_image = cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), COLORS[cls_id], 3)
        rospy.loginfo((cls_id, float(cls_conf), x1, x2, y1, y2))
        if x2 - x1 > 100 and abs(((x2 + x1) / 2) - 320) < 100:
            if cls_id == 0:
                no_mask = True
            elif cls_id == 1:
                mask = True

    if runner is None or not runner.isAlive():
        if no_mask:
            count += 1
            # if count > 10:
            draw_cross()
            # r#unner = threading.Thread(target=moving, daemon=True)
            # runner.start()
        else:
            count = 0
            if mask:
                draw_smail()
            else:
                clear_disp()

    return result_image


def show_fps(img, fps):
    return img
    """Draw fps number at top-left corner of the image."""
    font = cv2.FONT_HERSHEY_PLAIN
    line = cv2.LINE_AA
    fps_text = 'FPS: {:.2f}'.format(fps)
    cv2.putText(img, fps_text, (11, 20), font, 1.0, (32, 32, 32), 4, line)
    cv2.putText(img, fps_text, (10, 20), font, 1.0, (240, 240, 240), 1, line)
    return img


def image_proc():
    global fps, fps_t0
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)

    result_img = image_proc_a(image)
    # fps cal
    fps_t1 = time.time()
    fps_cur = (1.0 / (fps_t1 - fps_t0))
    fps = fps_cur if fps == 0.0 else (fps * 0.8 + fps_cur * 0.2)
    fps_t0 = fps_t1
    show_fps(result_img, fps)
    #
    # rgb_image = result_img.tostring()
    result_img = cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
    result_img = cv2.resize(result_img, (1024, 768))
    cv2.imshow(ROS_NODE_NAME, result_img)
    cv2.waitKey(1)
    # ros_image.data = rgb_image
    # image_pub.publish(ros_image)


def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    yolov5_chars = Yolov5TensorRT(FACEMASK_ENGINE_PATH, TRT_INPUT_SIZE, CLASSNUM)
    image_queue = queue.Queue(maxsize=2)
    jetmax = hiwonder.JetMax()
    jetmax.set_position((DEFAULT_X, DEFAULT_Y, DEFAULT_Z), 1)
    runner = None
    count = 0
    fps = 0
    fps_t0 = 0
    rospy.sleep(1)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)  # 订阅摄像头画面
    # image_pub = rospy.Publisher('/%s/image_result' % ROS_NODE_NAME, Image, queue_size=1)  # register result image pub

    while True:
        try:
            image_proc()
            if rospy.is_shutdown():
                break
        except KeyboardInterrupt:
            break
