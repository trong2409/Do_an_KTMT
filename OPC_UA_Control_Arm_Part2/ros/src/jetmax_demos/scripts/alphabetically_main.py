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

WORD_WANT = tuple([i for i in "DBRH"])

ROS_NODE_NAME = "hiwonder_jetmax_aph"
IMAGE_SIZE = 640, 480
CHARACTERS_ENGINE_PATH = os.path.join(sys.path[0], 'models/characters_v5_160.trt')
CHARACTER_LABELS = tuple([i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
CHARACTER_NUM = 26
TRT_INPUT_SIZE = 160
COLORS = tuple([tuple([random.randint(10, 255) for j in range(3)]) for i in range(CHARACTER_NUM)])
TARGET_POSITION = (-200, -180, 65)
yolov5_chars = Yolov5TensorRT(CHARACTERS_ENGINE_PATH, TRT_INPUT_SIZE, CHARACTER_NUM)


class Alphabetically:
    def __init__(self):
        self.lock = threading.RLock()
        self.moving_box = None
        self.index = 0
        self.pos_add = 0
        self.last_target = TARGET_POSITION

        self.runner = None
        self.moving_count = 0
        self.count = 0
        self.fps_t0 = time.time()
        self.fps = 0
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


def moving():
    # 计算机械臂当前位置与目标位置的x, y 轴距离
    c_x, c_y, cls_id, cls_conf = state.moving_box
    cur_x, cur_y, cur_z = jetmax.position

    x, y, _ = camera_to_world(state.K, state.R, state.T, np.array([c_x, c_y]).reshape((1, 1, 2)))[0][0]

    # 计算当前位置与目标位置的欧氏距离，以控制运动速度
    t = math.sqrt(x * x + y * y + 120 * 120) / 120

    # 计算气泵旋转舵机要旋转的角度
    # 机械臂吸取物品时的相对相对于初始位置时机械比正前方夹角加物品的旋转角度
    new_x, new_y = cur_x + x, cur_y + y
    arm_angle = math.atan(new_x / new_y) * 180 / math.pi

    hiwonder.pwm_servo1.set_position(90 - arm_angle, 0.1)
    jetmax.set_position((new_x, new_y, 70), t)
    rospy.sleep(t + 0.4)

    sucker.set_state(True)
    jetmax.set_position((new_x, new_y, 60), 1)  # 下移机械臂，吸取物品
    rospy.sleep(1)
    hiwonder.pwm_servo1.set_position(90, 0.1)

    # 获取码垛的位置
    x, y, z = state.last_target
    y += 45
    state.last_target = x, y, z

    cur_x, cur_y, cur_z = jetmax.position  # 当前的机械臂位置
    jetmax.set_position((cur_x, cur_y, 100), 0.8)
    rospy.sleep(0.8)

    angle = math.atan(x / y) * 180 / math.pi
    angle = 90 + (90 - angle) if angle > 0 else -angle
    hiwonder.pwm_servo1.set_position(angle, t)
    cur_x, cur_y, cur_z = jetmax.position
    t = math.sqrt((cur_x - x) ** 2 + (cur_y - y) ** 2) / 150
    rospy.loginfo((x, y, z))
    jetmax.set_position((x, y, z + 30), t)
    rospy.sleep(t)

    # 机械臂下移到目标码垛位置
    jetmax.set_position((x, y, z), 0.8)
    rospy.sleep(0.8)

    sucker.release(3)
    jetmax.set_position((x, y, z + 30), 0.8)  # 上提机械臂
    rospy.sleep(0.1)
    hiwonder.pwm_servo1.set_position(90, 0.5)  # 恢复吸盘角度
    rospy.sleep(0.5)

    # 回到初始位置
    jetmax.go_home(t)
    rospy.sleep(t + 0.5)
    with state.lock:
        state.moving_box = None
        state.moving_count += 1
        state.index += 1
        if state.moving_count >= len(WORD_WANT):
            state.moving_count = 0
        state.runner = None
    print("FINISHED")


def image_proc(img_in):
    result_image = cv2.cvtColor(img_in, cv2.COLOR_RGB2BGR)

    if state.runner is not None:
        return result_image

    outputs = yolov5_chars.detect(np.copy(img_in))
    boxes, confs, classes = yolov5_chars.post_process(img_in, outputs, 0.65)

    cards = []
    width, height = IMAGE_SIZE
    if state.index >= len(WORD_WANT):
        state.index = 0
        state.last_target = TARGET_POSITION

    if WORD_WANT[state.index] == '\n':
        state.index += 1
        x, y, z = state.last_target
        y -= 50
        x = TARGET_POSITION[0] - 5 - 40
        state.last_target = x, y, z

    for box, cls_id, cls_conf in zip(boxes, classes, confs):
        x1 = box[0] / TRT_INPUT_SIZE * width
        y1 = box[1] / TRT_INPUT_SIZE * height
        x2 = box[2] / TRT_INPUT_SIZE * width
        y2 = box[3] / TRT_INPUT_SIZE * height
        char = CHARACTER_LABELS[cls_id]
        if char == WORD_WANT[state.index]:
            cards.append((x1, y1, x2, y2, cls_id, cls_conf))
        cv2.putText(result_image, char + " " + str(float(cls_conf))[:4], (int(x1), int(y1) - 5),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS[cls_id], 2)
        cv2.rectangle(result_image, (int(x1), int(y1)), (int(x2), int(y2)), COLORS[cls_id], 3)

    if len(cards) == 0:
        state.count = 0
        state.moving_box = None
        rospy.logwarn("can not find card '{}'".format(WORD_WANT[state.index]))
    else:
        if state.moving_box is None:
            moving_box = max(cards, key=lambda x: x[-1])  # 识别到的所有卡牌中概率最大的一个
            x1, y1, x2, y2, cls_id, cls_conf = moving_box
            c_x, c_y = (x1 + x2) / 2, (y1 + y2) / 2
            state.moving_box = c_x, c_y, cls_id, cls_conf  # 存起来
            result_image = cv2.circle(result_image, (int(c_x), int(c_y)), 1, (255, 0, 0), 30)
            state.count = 0
        else:
            l_c_x, l_c_y, l_cls_id, _ = state.moving_box
            cards = [((x1 + x2) / 2, (y1 + y2) / 2, cls_id, cls_conf) for x1, y1, x2, y2, cls_id, cls_conf in
                     cards]  # 计算中心坐标
            distances = [math.sqrt((l_c_x - c_x) ** 2 + (l_c_y - c_y) ** 2) for c_x, c_y, _, _ in cards]  # 计算两次的中心坐标距离
            new_moving_box = min(zip(distances, cards), key=lambda x: x[0])  # 找到距离最小的
            _, (c_x, c_y, cls_id, cls_conf) = new_moving_box
            result_image = cv2.circle(result_image, (int(l_c_x), int(l_c_y)), 1, (0, 255, 0), 30)
            result_image = cv2.circle(result_image, (int(c_x), int(c_y)), 1, (255, 0, 0), 30)
            if cls_id == l_cls_id:  # 前后两次识别到的id相同，则进行搬运分类。若不同则重新识别
                state.moving_box = c_x, c_y, cls_id, cls_conf
                state.count += 1
                if state.count > 5:
                    print("MOVE")
                    state.count = 0
                    state.runner = threading.Thread(target=moving, daemon=True)
                    state.runner.start()
            else:
                state.moving_box = None
    return result_image


def show_fps(img, fps):
    """Draw fps number at top-left corner of the image."""
    font = cv2.FONT_HERSHEY_PLAIN
    line = cv2.LINE_AA
    fps_text = 'FPS: {:.2f}'.format(fps)
    cv2.putText(img, fps_text, (11, 20), font, 1.0, (32, 32, 32), 4, line)
    cv2.putText(img, fps_text, (10, 20), font, 1.0, (240, 240, 240), 1, line)
    return img


def image_proc_b():
    ros_image = image_queue.get(block=True)
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    result_img = image_proc(image)
    # fps cal
    fps_t1 = time.time()
    fps_cur = (1.0 / (fps_t1 - state.fps_t0))
    state.fps = fps_cur if state.fps == 0.0 else (state.fps * 0.8 + fps_cur * 0.2)
    state.fps_t0 = fps_t1
    # show_fps(result_img, state.fps)
    cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
    cv2.imshow(ROS_NODE_NAME, result_img)
    cv2.waitKey(1)


def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    state = Alphabetically()
    image_queue = queue.Queue(maxsize=1)
    state.load_camera_params()
    if state.camera_params is None:
        rospy.logerr("Can not load camera parameters!")

    jetmax = hiwonder.JetMax()
    jetmax.go_home()
    sucker = hiwonder.Sucker()
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)  # 订阅摄像头画面
    while True:
        try:
            image_proc_b()
            if rospy.is_shutdown():
                sys.exit(0)
        except KeyboardInterrupt:
            break
