#!/usr/bin/env python3
import sys
import math
import rospy
import time
import queue
import threading
import cv2
import numpy as np
import hiwonder
from sensor_msgs.msg import Image as RosImage

from PIL import Image
import torch
from facenet_pytorch import MTCNN

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)

mtcnn = MTCNN(keep_all=True, min_face_size=50, factor=0.709, post_process=False, device=device)

ROS_NODE_NAME = 'face_expression'
jetmax = hiwonder.JetMax()
image_queue = queue.Queue(maxsize=1)


def show_faces(img, boxes, landmarks, color):
    new_boxes = []
    new_landmarks = []
    for bb, ll in zip(boxes, landmarks):
        x1 = int(hiwonder.misc.val_map(bb[0], 0, 160, 0, 640))
        y1 = int(hiwonder.misc.val_map(bb[1], 0, 160, 0, 480))
        x2 = int(hiwonder.misc.val_map(bb[2], 0, 160, 0, 640))
        y2 = int(hiwonder.misc.val_map(bb[3], 0, 160, 0, 480))
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        new_boxes.append([x1, y1, x2, y2])
        landmarks_curr_face = []
        if len(landmarks):
            for j in range(5):
                lx = int(hiwonder.misc.val_map(ll[j][0], 0, 160, 0, 640))
                ly = int(hiwonder.misc.val_map(ll[j][1], 0, 160, 0, 480))
                cv2.circle(img, (lx, ly), 2, color, 2)
                landmarks_curr_face.append([lx, ly])
        new_landmarks.append(landmarks_curr_face)
    return img, new_boxes, new_landmarks



def image_proc_a(image):
    img_ret = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    org_img1 = np.copy(image)
    image = cv2.resize(image, (160, 160))
    boxes, _, landmarks = mtcnn.detect(Image.fromarray(image), landmarks=True)
    if boxes is None:
        return img_ret
    boxes = list(boxes)
    landmarks = list(landmarks)

    img_ret, boxes, landmarks = show_faces(img_ret, boxes, landmarks, (0, 255, 0))
    return img_ret

def image_proc_b():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    image = image_proc_a(image)
    toc = time.time()
    cv2.imshow(ROS_NODE_NAME, image)
    cv2.waitKey(1)

def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass



if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    jetmax.go_home(1)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', RosImage, image_callback)
    try:
        while not rospy.is_shutdown():
            image_proc_b()
    except Exception as e:
        rospy.logerr(e)
        print(e.__traceback__.tb_lineno)
        sys.exit()
