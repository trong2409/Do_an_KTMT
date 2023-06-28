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

from FER import fer

mtcnn = MTCNN(keep_all=True, min_face_size=50, factor=0.709, post_process=False, device=device)

ROS_NODE_NAME = 'face_expression'
jetmax = hiwonder.JetMax()
image_queue = queue.Queue(maxsize=1)
mtx = hiwonder.TM1640(4, 9)
mtx.gram = [0xFF] * 16
mtx.refresh()

def display_expression(name):
    expressions = {
    'Happy' : """---XX------XX---
                 --X--X----X--X--
                 -X----X--X----X-
                 ----------------
                 ----------------
                 ---X--------X---
                 ----X------X----
                 -----XXXXXX-----""".replace(' ', '').split('\n'),

    'Angry' : """-XX----------XX-
                 --XX--------XX--
                 ---XX------XX---
                 ----XX----XX----
                 ----------------
                 ----XXXXXXXX----
                 ---XX------XX---
                 --XX--------XX--""".replace(' ', '').split('\n'),

    'Sad' :   """---XXX----XXX---
                 --XX--------XX--
                 XXX----------XXX
                 ----------------
                 ----------------
                 ----XXXXXXXX----
                 --XX--------XX--
                 -X------------X-""".replace(' ', '').split('\n')
    }
    if name in expressions:
        e = expressions[name]
        for y in range(8):
            for x in range(16):
                mtx.set_bit(x, y, 1 if e[y][x] == 'X' else 0)
    else:
        mtx.gram = [0] * 16
    mtx.refresh()



class FaceExpression:
    def __init__(self):
        self.lock = threading.RLock()
        self.servo_x = 500
        self.face_tracking = None
        self.no_face_count = 0
        self.lost_target_count = 0
        self.is_running_face = False
        self.fps = 0.0
        self.tic = time.time()
        self.exp = ''
        self.count = 0


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
    box = None
    if state.face_tracking is None:
        if len(boxes) > 0:
            box = min(boxes, key=lambda b: math.sqrt(((b[2] + b[0]) / 2 - 320) ** 2 + ((b[3] + b[1]) / 2 - 240) ** 2))
            x1, y1, x2, y2 = box
            center_x, center_y = int((x1 + x2) / 2), int((y1 + y2) / 2)
            cv2.rectangle(img_ret, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.circle(img_ret, (center_x, center_y), 2, (0, 255, 0), 4)
            state.face_tracking = center_x, center_y
            state.no_face_count = time.time() + 2
    else:
        centers = [(int((box[2] + box[0]) / 2), int((box[3] + box[1]) / 2), box) for box in boxes]
        get_face = False
        if len(centers) > 0:
            center_x, center_y = state.face_tracking
            cv2.circle(img_ret, (center_x, center_y), 2, (255, 0, 0), 4)
            min_dist_center = min(centers, key=lambda c: math.sqrt((c[0] - center_x) ** 2 + (c[1] - center_y) ** 2))
            new_center_x, new_center_y, box = min_dist_center
            x1, y1, x2, y2 = box
            dist = math.sqrt((new_center_x - center_x) ** 2 + (new_center_y - center_y) ** 2)
            if dist < 250:
                cv2.rectangle(img_ret, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cv2.circle(img_ret, (new_center_x, new_center_y), 2, (0, 0, 255), 4)
                get_face = True
                state.face_tracking = int(new_center_x), int(new_center_y)
                state.no_face_count = time.time() + 0.2

        if state.no_face_count < time.time():
            state.face_tracking = None
            get_face = False
        if get_face:
            x1, y1, x2, y2 = box
            x1 = 0 if x1 < 0 else  639 if x1 > 639 else x1
            x2 = 0 if x2 < 0 else  639 if x2 > 639 else x2
            y1 = 0 if y1 < 0 else 479 if y1 > 479 else y1
            y2 = 0 if y2 < 0 else 479 if y2 > 479 else y2

            print(x1, y1, x2, y2)
            face = org_img1[y1: y2, x1: x2]
            cv2.imshow("face", cv2.cvtColor(face, cv2.COLOR_RGB2BGR))
            a = fer.fer(face)
            cv2.putText(img_ret, a, (0, 200), 0, 1.6, (255, 50, 50), 5)
            display_expression(a)
    return img_ret

def image_proc_b():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    image = image_proc_a(image)
    toc = time.time()
    curr_fps = 1.0 / (state.tic - toc)
    state.fps = curr_fps if state.fps == 0.0 else (state.fps * 0.95 + curr_fps * 0.05)
    state.tic = toc
    cv2.imshow(ROS_NODE_NAME, image)
    cv2.waitKey(1)

def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass



if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    state = FaceExpression()
    jetmax.go_home(1)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', RosImage, image_callback)
    try:
        while not rospy.is_shutdown():
            image_proc_b()
    except Exception as e:
        rospy.logerr(e)
        print(e.__traceback__.tb_lineno)
        sys.exit()
