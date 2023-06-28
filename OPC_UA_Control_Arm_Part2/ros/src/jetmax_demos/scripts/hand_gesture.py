#!/usr/bin/env python3
import sys
import cv2
import math
import threading
import numpy as np
import rospy
import queue
from sensor_msgs.msg import Image
import hiwonder
import mediapipe as mp

ROS_NODE_NAME = "hand_gesture"


class HandGesture:
    def __init__(self):
        self.moving_color = None
        self.target_colors = {}
        self.lock = threading.RLock
        self.position = 0, 0, 0
        self.runner = None
        self.count = 0
        self.gesture_str = ''


ps = (-205, 0 + 10, 150), (-205, 0 + 10, 120), (-205, 0 + 10, 190)


def vector_2d_angle(v1, v2):
    """
       Solve the angle between two vector
    """
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(math.acos(
            (v1_x * v2_x + v1_y * v2_y) / (((v1_x ** 2 + v1_y ** 2) ** 0.5) * ((v2_x ** 2 + v2_y ** 2) ** 0.5))))
    except:
        angle_ = 65535.
    if angle_ > 180.:
        angle_ = 65535.
    return angle_


def hand_angle(hand_):
    """
        Obtain the angle of the corresponding hand-related vector, and determine the gesture according to the angle
    """
    angle_list = []
    # ---------------------------- thumb
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[2][0])), (int(hand_[0][1]) - int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])), (int(hand_[3][1]) - int(hand_[4][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- index
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[6][0])), (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])), (int(hand_[7][1]) - int(hand_[8][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- middle
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[10][0])), (int(hand_[0][1]) - int(hand_[10][1]))),
        ((int(hand_[11][0]) - int(hand_[12][0])), (int(hand_[11][1]) - int(hand_[12][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- ring
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[14][0])), (int(hand_[0][1]) - int(hand_[14][1]))),
        ((int(hand_[15][0]) - int(hand_[16][0])), (int(hand_[15][1]) - int(hand_[16][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- pink
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[18][0])), (int(hand_[0][1]) - int(hand_[18][1]))),
        ((int(hand_[19][0]) - int(hand_[20][0])), (int(hand_[19][1]) - int(hand_[20][1])))
    )
    angle_list.append(angle_)
    return angle_list


def h_gesture(angle_list):
    """
        Use the angle of the corresponding hand-related to define the gesture

    """
    thr_angle = 65.
    thr_angle_thumb = 53.
    thr_angle_s = 49.
    gesture_str = None
    if 65535. not in angle_list:
        if (angle_list[0] > thr_angle_thumb) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "fist"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "hand_heart"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] < thr_angle_s):
            gesture_str = "nico-nico-ni"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "hand_heart"
        elif (angle_list[0] > 5) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "one"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "two"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] > thr_angle):
            gesture_str = "three"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] > thr_angle) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] < thr_angle_s):
            gesture_str = "OK"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] < thr_angle_s):
            gesture_str = "four"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] < thr_angle_s):
            gesture_str = "five"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] < thr_angle_s):
            gesture_str = "six"
        else:
            "none"
    return gesture_str


ngcs = {
    'one': 'gcode/1.ngc',
    'two': 'gcode/2.ngc',
    'three': 'gcode/3.ngc',
    'four': 'gcode/4.ngc',
    'five': 'gcode/5.ngc',
    'six': 'gcode/6.ngc',
    'hand_heart': 'ngcs/hand_heart.ngc',
}


def draw_num(num):
    all_num = ['one', 'two', 'three', 'four', 'five', 'six', 'fist', 'hand_heart', 'nico-nico-ni', "OK"]
    try:
        i = all_num.index(num)
    except:
        state.runner = None
    if i < 5:
        for i in range(i + 1):
            hiwonder.buzzer.on()
            rospy.sleep(0.1)
            hiwonder.buzzer.off()
            rospy.sleep(0.3)
    else:
        hiwonder.buzzer.on()
        rospy.sleep(1)
        hiwonder.buzzer.off()
    state.runner = None


def image_proc_a(img):
    img_ret = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if state.runner is not None:
        cv2.putText(img, state.gesture_str, (0, 200), 0, 1.5, (100, 100, 255), 5)
        return img_ret

    results = hands.process(img)
    if results.multi_handedness:
        for label in results.multi_handedness:
            print(label)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # rospy.logdebug('hand_landmarks:', hand_landmarks)
            mp_drawing.draw_landmarks(img_ret, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            hand_local = []
            for i in range(21):
                x = hand_landmarks.landmark[i].x * img.shape[1]
                y = hand_landmarks.landmark[i].y * img.shape[0]
                hand_local.append((x, y))
            if hand_local:
                angle_list = hand_angle(hand_local)
                gesture_str = h_gesture(angle_list)
                cv2.putText(img_ret, gesture_str, (0, 200), 0, 1.5, (100, 100, 255), 5)
                if gesture_str != state.gesture_str:
                    state.count = 0
                state.gesture_str = gesture_str
                state.count += 1
    else:
        state.count = 0

    if state.count > 10:
        state.count = 0
        state.runner = threading.Thread(target=draw_num, args=(state.gesture_str,), daemon=True)
        state.runner.start()
    return img_ret


def image_proc_b():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    image = cv2.flip(image, 1)
    image = image_proc_a(image)
    image = cv2.resize(image, (1024, 768))
    cv2.imshow(ROS_NODE_NAME, image)
    cv2.waitKey(1)


def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass

if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    rospy.sleep(0.2)
    state = HandGesture()
    image_queue = queue.Queue(maxsize=1)
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.5)

    jetmax = hiwonder.JetMax()
    jetmax.go_home()
    rospy.sleep(1)
    hiwonder.motor2.set_speed(0)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback, queue_size=1)
    while not rospy.is_shutdown():
        image_proc_b()
