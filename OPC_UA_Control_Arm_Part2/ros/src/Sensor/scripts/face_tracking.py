#!/usr/bin/env python3
import math
import rospy
import time
import queue
import threading
from sensor_msgs.msg import Image as RosImage
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from std_srvs.srv import Trigger, TriggerResponse, TriggerRequest
from std_srvs.srv import Empty
from object_tracking.srv import SetTarget, SetTargetResponse, SetTargetRequest
import cv2
import numpy as np
import hiwonder
import sys
import Jetson.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.output(9, 0)
GPIO.output(4, 0)

from PIL import Image
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))
mtcnn = MTCNN(keep_all=True, min_face_size=50, factor=0.709, post_process=False, device=device)
ROS_NODE_NAME = 'face_tracking'
TARGET_PIXEL_X, TARGET_PIXEL_Y = 320, 240

class FaceTracking:
    def __init__(self):
        self.servo_x = 500
        self.servo_y = 500

        self.face_x_pid = hiwonder.PID(0.09, 0.005, 0.005)
        self.face_z_pid = hiwonder.PID(0.1, 0.0, 0.0)
        self.tracking_face = None
        self.no_face_count = 0
        self.lost_target_count = 0
        self.fan_on = False


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
        if len(landmarks[0]):
            for j in range(5):
                lx = int(hiwonder.misc.val_map(ll[j][0], 0, 160, 0, 640))
                ly = int(hiwonder.misc.val_map(ll[j][1], 0, 160, 0, 480))
                cv2.circle(img, (lx, ly), 2, color, 4)
                landmarks_curr_face.append([lx, ly])
        new_landmarks.append(landmarks_curr_face)
    return img, new_boxes, new_landmarks


def fan_control():
    while True:
        if state.fan_on:
            GPIO.output(9, 0)
            GPIO.output(4, 1)
            time.sleep(0.01)
            GPIO.output(9, 0)
            GPIO.output(4, 0)
            time.sleep(0.01)
        else:
            GPIO.output(9, 0)
            GPIO.output(4, 0)
            time.sleep(0.01)


def face_tracking(image):
    ta = time.time()
    org_img = np.copy(image)
    image = cv2.resize(image, (160, 160))
    boxes, _, landmarks = mtcnn.detect(Image.fromarray(image), landmarks=True)
    if boxes is not None:
        boxes = boxes.tolist()
        landmarks = landmarks.tolist()
        org_img, boxes, landmarks = show_faces(org_img, boxes, landmarks, (0, 255, 0))
    else:
        boxes = []

    if state.tracking_face is None:
        if len(boxes) > 0:
            box = min(boxes, key=lambda b: math.sqrt(((b[2] + b[0]) / 2 - 320) ** 2 + ((b[3] + b[1]) / 2 - 240) ** 2))
            x1, y1, x2, y2 = box
            org_img = cv2.rectangle(org_img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            center_x, center_y = int((x1 + x2) / 2), int((y1 + y2) / 2)
            org_img = cv2.circle(org_img, (center_x, center_y), 2, (0, 255, 0), 4)
            state.tracking_face = center_x, center_y
            state.no_face_count = time.time() + 2
            state.face_x_pid.clear()
            state.face_z_pid.clear()
    else:
        centers = [(int((box[2] + box[0]) / 2), int((box[3] + box[1]) / 2), box) for box in boxes]
        get_face = False
        if len(centers) > 0:
            center_x, center_y = state.tracking_face
            org_img = cv2.circle(org_img, (center_x, center_y), 2, (0, 0, 255), 4)
            min_dist_center = min(centers, key=lambda c: math.sqrt((c[0] - center_x) ** 2 + (c[1] - center_y) ** 2))
            new_center_x, new_center_y, box = min_dist_center
            x1, y1, x2, y2 = box
            dist = math.sqrt((new_center_x - center_x) ** 2 + (new_center_y - center_y) ** 2)
            if dist < 150:
                org_img = cv2.rectangle(org_img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                org_img = cv2.circle(org_img, (new_center_x, new_center_y), 2, (255, 0, 0), 4)
                get_face = True
                state.tracking_face = int(new_center_x), int(new_center_y)
                state.no_face_count = time.time() + 2
        if state.no_face_count < time.time():
            state.tracking_face = None
            get_face = False
            state.fan_on = False
            print("FAN OFF")

        if get_face:
            state.fan_on = True
            center_x, center_y = state.tracking_face
            x = center_x - 320
            if abs(x) > 30:
                state.face_x_pid.SetPoint = 0
                state.face_x_pid.update(x)
                state.servo_x += state.face_x_pid.output
                jetmax.set_servo(1, int(state.servo_x), 0.02)
            else:
                state.face_x_pid.update(0)

            z = center_y - 240
            if abs(z) > 30:
                state.face_z_pid.SetPoint = 0
                state.face_z_pid.update(z)
                z = jetmax.position[2] + state.face_z_pid.output
                jetmax.set_position((jetmax.position[0], jetmax.position[1], z), 0.02)
            else:
                state.face_z_pid.update(0)
            print(center_x, center_y)
    return org_img

def image_proc():
    global mtcnn
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    image = face_tracking(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow("result", image)
    cv2.waitKey(1)


def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass



if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    state = FaceTracking()
    jetmax = hiwonder.JetMax()
    jetmax.go_home()
    rospy.sleep(1)
    image_queue = queue.Queue(maxsize=1)
    threading.Thread(target=fan_control, daemon=True).start()
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', RosImage, image_callback)  # 订阅摄像头画面
    while not rospy.is_shutdown():
        image_proc()

