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


class VisualCalculator:
    def __init__(self):
        self.moving_box = None
        self.is_moving = False
        self.is_running = False
        self.runner = None
        self.count = 0
        self.lock = threading.RLock()
        self.step = 0
        self.eq_box = 0, 0, 0, 0
        self.ans_step = 0
        self.answer = ""
        self.line = 0
        self.string = ""
        self.camera_params = None
        self.K = None
        self.R = None
        self.T = None

    def load_camera_params(self):
        self.camera_params = rospy.get_param('/camera_cal/block_params', self.camera_params)
        if self.camera_params is not None:
            self.K = np.array(self.camera_params['K'], dtype=np.float64).reshape(3, 3)
            self.R = np.array(self.camera_params['R'], dtype=np.float64).reshape(3, 1)
            self.T = np.array(self.camera_params['T'], dtype=np.float64).reshape(3, 1)


def camera_to_world(cam_mtx, r, t, img_points):
    inv_k = np.asmatrix(cam_mtx).I
    r_mat = np.zeros((3, 3), dtype=np.float64)
    cv2.Rodrigues(r, r_mat)
    # invR * T
    inv_r = np.asmatrix(r_mat).I  # 3*3
    transPlaneToCam = np.dot(inv_r, np.asmatrix(t))  # 3*3 dot 3*1 = 3*1
    world_pt = []
    coords = np.zeros((3, 1), dtype=np.float64)
    for img_pt in img_points:
        coords[0][0] = img_pt[0][0]
        coords[1][0] = img_pt[0][1]
        coords[2][0] = 1.0
        worldPtCam = np.dot(inv_k, coords)  # 3*3 dot 3*1 = 3*1
        # [x,y,1] * invR
        worldPtPlane = np.dot(inv_r, worldPtCam)  # 3*3 dot 3*1 = 3*1
        # zc
        scale = transPlaneToCam[2][0] / worldPtPlane[2][0]
        # zc * [x,y,1] * invR
        scale_worldPtPlane = np.multiply(scale, worldPtPlane)
        # [X,Y,Z]=zc*[x,y,1]*invR - invR*T
        worldPtPlaneReproject = np.asmatrix(scale_worldPtPlane) - np.asmatrix(transPlaneToCam)  # 3*1 dot 1*3 = 3*3
        pt = np.zeros((3, 1), dtype=np.float64)
        pt[0][0] = worldPtPlaneReproject[0][0]
        pt[1][0] = worldPtPlaneReproject[1][0]
        pt[2][0] = 0
        world_pt.append(pt.T.tolist())
    return world_pt


def moving(start):
    # Calculate the x, y axis distance between the current position of the robotic arm and the target position
    _, _, c_x, c_y = start
    cur_x, cur_y, cur_z = jetmax.position

    x, y, _ = camera_to_world(state.K, state.R, state.T, np.array([c_x, c_y]).reshape((1, 1, 2)))[0][0]

    # Calculate the Euclidean distance between the current position and the target position to control the movement speed
    t = math.sqrt(x * x + y * y + 70 * 70) / 80

    # The angle of the relative initial position of the robotic arm when picking up the card
    new_x, new_y = cur_x + y, cur_y - x
    arm_angle = math.atan(new_y / new_x) * 180 / math.pi
    print(arm_angle)

    hiwonder.pwm_servo1.set_position(90 + arm_angle, 0.1)
    jetmax.set_position((new_x, new_y, 70), t)
    rospy.sleep(t + 0.4)

    sucker.set_state(True)
    jetmax.set_position((new_x, new_y, 60), 1)  # Move jetmax down to pick up the card
    rospy.sleep(1)

    jetmax.set_position((new_x, new_y, 120), 1)
    rospy.sleep(0.2)
    hiwonder.pwm_servo1.set_position(90, 0.8)
    rospy.sleep(0.8)

    _, _, c_x, c_y = state.eq_box
    print(c_x, c_y)
    cur_x, cur_y, cur_z = jetmax.position

    x, y, _ = camera_to_world(state.K, state.R, state.T, np.array([c_x, c_y]).reshape((1, 1, 2)))[0][0]
    z = 60

    t = math.sqrt((cur_x - x) ** 2 + (cur_y - y) ** 2) / 100
    t1 = math.sqrt((cur_x - x) ** 2 + (cur_y - y) ** 2) / 100

    # Calculate the angle between the robotic arm and the central axis when placing the card
    state.ans_step += 1
    new_x, new_y = jetmax.ORIGIN[0] + x - (state.ans_step * 45), jetmax.ORIGIN[1] + y
    angle = math.atan(new_x / new_y) * 180 / math.pi
    print(angle)

    hiwonder.pwm_servo1.set_position(90 - angle, t)
    jetmax.set_position((new_x, new_y, cur_z), t)
    rospy.sleep(t + 0.3)

    # Move jetmax down to the target position
    jetmax.set_position((new_x, new_y, z), 0.8)
    rospy.sleep(0.8)

    sucker.release(3)
    jetmax.set_position((new_x, new_y, z + 30), 0.8)
    rospy.sleep(0.2)
    hiwonder.pwm_servo1.set_position(90, 0.5)
    rospy.sleep(0.5)

    # Back to the initial position
    if state.ans_step >= len(state.answer):
        jetmax.set_position(tuple(jetmax.ORIGIN),  t1)
    else:
        jetmax.set_position((jetmax.ORIGIN[1], jetmax.ORIGIN[0], jetmax.ORIGIN[2]), t1)
    rospy.sleep(t1 + 0.2)
    state.runner = None


def pos_a():
    jetmax.set_position((jetmax.ORIGIN[1], jetmax.ORIGIN[0], jetmax.ORIGIN[2]), 2)
    rospy.sleep(2.2)
    state.runner = None


def pos_b():
    jetmax.set_position((jetmax.ORIGIN[0], jetmax.ORIGIN[1], jetmax.ORIGIN[2]), 2)
    rospy.sleep(2.2)
    state.runner = None


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
        card_name = str(TRT_CLASS_NAMES[cls_id])
        image = cv2.putText(image, card_name + " " + str(float(cls_conf))[:4], (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, COLORS[cls_id], 2)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), COLORS[cls_id], 2)
        if state.step == 1:
            if state.ans_step < len(state.answer) and state.answer[state.ans_step] == TRT_CLASS_NAMES[cls_id]:
                cards.append((cls_id, cls_conf, (x1 + x2) / 2, (y1 + y2) / 2))
        else:
            cards.append((cls_id, cls_conf, (x1 + x2) / 2, (y1 + y2) / 2))

    if state.runner is None:
        if state.step == 0:
            if len(cards) > 0:
                cards.sort(key=lambda x: x[2])
                ext = ""
                for c in cards:
                    ext += str(TRT_CLASS_NAMES[c[0]])
                    # print(ext)
                if ext[-1] == '=':
                    try:
                        a = eval(ext[:-1])
                        state.count += 1
                        if state.count > 30:
                            rospy.loginfo("answer:" + str(a))
                            state.answer = str(int(a))
                            state.string = ext + state.answer
                            state.step = 1
                            state.ans_step = 0
                            state.count = 0
                            i, c, x, y = cards[-1]
                            state.eq_box = i, c, x, y
                            state.runner = threading.Thread(target=pos_a, daemon=True)
                            state.runner.start()
                    except Exception as e:
                        rospy.logerr((e, ext[:-1]))
                        state.count = 0
                else:
                    state.count = 0
        elif state.step == 1:
            if state.ans_step >= len(state.answer):
                rospy.loginfo("finished answer")
                state.step = 0
                state.runner = threading.Thread(target=pos_b)
                state.runner.start()
                state.string = ""
            else:
                if len(cards) > 0:
                    cls_id, cls_conf, x, y = cards[0]
                    state.count += 1
                    if state.count > 10:
                        state.runner = threading.Thread(target=moving, args=(cards[0],), daemon=True)
                        state.runner.start()
                else:
                    state.count = 0
                    rospy.logwarn("can not find \'" + state.answer[state.ans_step] + "\'")
        else:
            pass

    else:
        pass
    image = cv2.putText(image, state.string, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (205, 120, 120), 3)
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
    state = VisualCalculator()
    state.load_camera_params()
    if state.camera_params is None:
        rospy.logerr("Can not load camera parameters!")
    yolov5 = Yolov5TensorRT(TRT_ENGINE_PATH, TRT_INPUT_SIZE, TRT_NUM_CLASSES)
    jetmax = hiwonder.JetMax()
    sucker = hiwonder.Sucker()
    jetmax.go_home(2)
    sucker.release()
    rospy.sleep(2)
    image_queue = queue.Queue(maxsize=1)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)  # Subscribe to the camera
    while True:
        try:
            image_proc()
            if rospy.is_shutdown():
                sys.exit(0)
        except KeyboardInterrupt:
            break
