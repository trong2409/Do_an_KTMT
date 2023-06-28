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
from yolov5_tensorrt import Yolov5TensorRT

ROS_NODE_NAME = "screw_nut_classification"

TRT_ENGINE_PATH = os.path.join(sys.path[0], "models/screw_nut_v5_160.trt")
TRT_INPUT_SIZE = 160
TRT_NUM_CLASSES = 2
TRT_CLASS_NAMES = ("Screw", "Nut")
COLORS = {'Screw': (0, 0, 255), "Nut": (0, 255, 0)}
TARGET_POSITION = {"Screw": (120, -0, 140), "Nut": (-120, -0, 140)}


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


class ScrewNutClassification:
    def __init__(self):
        self.lock = threading.RLock()
        self.moving_obj = None
        self.runner = None
        self.count = 0
        self.camera_params = None
        self.K = None
        self.R = None
        self.T = None

    def reset(self):
        self.moving_obj = None
        self.runner = None
        self.count = 0

    def load_camera_params(self):
        self.camera_params = rospy.get_param('/camera_cal/card_params', self.camera_params)
        if self.camera_params is not None:
            self.K = np.array(self.camera_params['K'], dtype=np.float64).reshape(3, 3)
            self.R = np.array(self.camera_params['R'], dtype=np.float64).reshape(3, 1)
            self.T = np.array(self.camera_params['T'], dtype=np.float64).reshape(3, 1)


def moving():
    try:
        c_x, c_y, cls_name = state.moving_obj
        cur_x, cur_y, cur_z = jetmax.position

        x, y, _ = camera_to_world(state.K, state.R, state.T, np.array([c_x, c_y]).reshape((1, 1, 2)))[0][0]
        print("dist", x, y)

        t = math.sqrt(x * x + y * y + 140 * 140) / 140

        new_x, new_y = cur_x + x - 15, cur_y + y
        jetmax.set_position((new_x, new_y, 100), t)
        rospy.sleep(t + 0.2)

        sucker.set_state(True)
        jetmax.set_position((new_x, new_y, 65), 0.8)
        rospy.sleep(0.85)

        x, y, z = TARGET_POSITION[cls_name]
        cur_x, cur_y, cur_z = jetmax.position
        jetmax.set_position((cur_x, cur_y, 140), 0.8)
        rospy.sleep(0.8)

        cur_x, cur_y, cur_z = jetmax.position
        t = math.sqrt((cur_x - x) ** 2 + (cur_y - y) ** 2) / 160
        jetmax.set_position((x, y, 160), t)
        rospy.sleep(t)

        jetmax.set_position((x, y, z), 0.8)
        rospy.sleep(0.8)

        #sucker.release(3)
        hiwonder.motor1.set_speed(-40)
        rospy.sleep(0.2)
        hiwonder.motor1.set_speed(0)

        jetmax.set_position((x, y, z + 50), 0.8)
        rospy.sleep(0.9)

    finally:
        cur_x, cur_y, cur_z = jetmax.position
        t = math.sqrt((cur_x - jetmax.ORIGIN[0]) ** 2 + (cur_y - jetmax.ORIGIN[1]) ** 2) / 140
        jetmax.go_home(t)
        rospy.sleep(t + 0.2)
        state.moving_obj = None
        state.runner = None
        print("FINISHED")


def image_proc_a():
    ros_image = image_queue.get(block=True)
    img = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    img_ret = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if state.runner is not None:
        return img_ret
    outputs = yolov5.detect(img)
    boxes, confs, classes = yolov5.post_process(img, outputs, 0.85)
    height, width = img.shape[:2]
    objs = []
    for box, cls_conf, cls_id in zip(boxes, confs, classes):
        x1 = int(box[0] / TRT_INPUT_SIZE * width)
        y1 = int(box[1] / TRT_INPUT_SIZE * height)
        x2 = int(box[2] / TRT_INPUT_SIZE * width)
        y2 = int(box[3] / TRT_INPUT_SIZE * height)
        cls_name = TRT_CLASS_NAMES[cls_id]
        if cls_conf < 0.85:
            continue
        objs.append((cls_conf, x1, y1, x2, y2, cls_name))
        cv2.putText(img_ret, cls_name + " " + str(float(cls_conf))[:4], (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    COLORS[cls_name], 2)
        cv2.rectangle(img_ret, (x1, y1), (x2, y2), COLORS[cls_name], 3)

    if len(objs) == 0:
        state.count = 0
        state.moving_obj = None
    else:
        if state.moving_obj is None:
            moving_box = max(objs, key=lambda obj: obj[0])
            conf, x1, y1, x2, y2, cls_name = moving_box
            c_x, c_y = (x1 + x2) / 2, (y1 + y2) / 2
            state.moving_obj = c_x, c_y, cls_name
        else:
            l_c_x, l_c_y, l_waste_class_name = state.moving_obj
            moving_obj = min(objs, key=lambda card: math.sqrt((l_c_x - card[1]) ** 2 + (l_c_y - card[2]) ** 2))

            conf, x1, y1, x2, y2, cls_name = moving_obj
            c_x, c_y = (x1 + x2) / 2, (y1 + y2) / 2

            cv2.rectangle(img_ret, (x1, y1), (x2, y2), (255, 255, 255), 6)
            cv2.circle(img_ret, (int(c_x), int(c_y)), 1, (255, 255, 255), 10)

            if math.sqrt((l_c_x - c_x) ** 2 + (l_c_y - c_y) ** 2) > 30:
                state.count = 0
            else:
                c_x = l_c_x * 0.2 + c_x * 0.8
                c_y = l_c_y * 0.2 + c_y * 0.8
                state.count += 1
            state.moving_obj = c_x, c_y, cls_name
            if state.count > 10:
                state.count = 0
                state.runner = threading.Thread(target=moving, daemon=True)
                state.runner.start()
    return img_ret

def image_proc():
    a = image_proc_a()
    cv2.imshow('img', a)
    cv2.waitKey(1)

def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass

if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    image_queue = queue.Queue(maxsize=2)
    state = ScrewNutClassification()
    state.load_camera_params()
    if state.camera_params is None:
        rospy.logerr("Can not load camera parameters")
        sys.exit(-1)
    jetmax = hiwonder.JetMax()
    sucker = hiwonder.Sucker()
    jetmax.go_home()
    sucker.release()
    yolov5 = Yolov5TensorRT(TRT_ENGINE_PATH, TRT_INPUT_SIZE, TRT_NUM_CLASSES)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)
    while True:
        try:
            image_proc()
            if rospy.is_shutdown():
                sys.exit(0)
        except Exception as e:
            print(e)
            break
