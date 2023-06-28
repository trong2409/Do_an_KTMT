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
from std_msgs.msg import Bool,String,UInt16
from jetmax_control.msg import SetServo
from yolov5_tensorrt import Yolov5TensorRT

# sys.path.insert(1, '/home/hiwonder/ros/src/jetmax_buildin_funcs/waste_classification/scripts')
#sys.path.append('/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control_custom/scripts')

from __main__ import Singleton

single = Singleton()
jetmax = single.jetmax
sucker = single.sucker

ROS_NODE_NAME = "waste_classification"

TRT_ENGINE_PATH = os.path.join(sys.path[0], "waste_v5_160.trt")
print(sys.path)
#print(f'{sys.path[0]}/waste_v5_160_trt')
TRT_ENGINE_PATH ="/home/hiwonder/ros/src/jetmax_buildin_funcs/waste_classification/scripts/waste_v5_160.trt"
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
WASTE_CLASSES_COLORS = {
    'recyclable_waste': 'blue',
    'hazardous_waste': 'red',
    'food_waste': 'green',
    'residual_waste': 'black'
}
COLORS = {
    'recyclable_waste': (0, 0, 255),
    'hazardous_waste': (255, 0, 0),
    'food_waste': (0, 255, 0),
    'residual_waste': (80, 80, 80)
}
TARGET_POSITION = {
    'recyclable_waste': (155, -65, 65, 65),
    'hazardous_waste': (155, -20, 65, 85),
    'food_waste': (155, 30, 65, 100),
    'residual_waste': (165, 80, 65, 118)
}

SUCK_WASTE_IDLE = 1
SUCK_WASTE_SUCK  = 2
SUCK_WASTE_HOLD = 3
SUCK_WASTE_RELEASE = 4

unit_block_corners = np.asarray([[0, 0, 0],
                                 [20, -20, 0],  # TAG_SIZE = 33.30mm
                                 [-20, -20, 0],
                                 [-20, 20, 0],
                                 [20, 20, 0]],
                                dtype=np.float64)
unit_block_img_pts = None

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


class WasteClassification:
    def __init__(self):
        self.lock = threading.RLock()
        self.is_running = False
        self.moving_box = None
        self.moving_color=None
        self.image_sub = None
        self.heartbeat_timer = None
        self.runner = None
        self.count = 0
        self.camera_params = None
        self.K = None
        self.R = None
        self.T = None
        self.suck_state= SUCK_WASTE_IDLE 
        self.waste_class = 'food_waste'
        self.target_colors = {}

    def reset(self):
        self.is_running = False
        self.moving_box = None
        self.image_sub = None
        self.heartbeat_timer = None
        self.runner = None
        self.count = 0

    def load_camera_params(self):
        global unit_block_img_pts
        self.camera_params = rospy.get_param('/camera_cal/card_params', self.camera_params)
        if self.camera_params is not None:
            self.K = np.array(self.camera_params['K'], dtype=np.float64).reshape(3, 3)
            self.R = np.array(self.camera_params['R'], dtype=np.float64).reshape(3, 1)
            self.T = np.array(self.camera_params['T'], dtype=np.float64).reshape(3, 1)
            img_pts, jac = cv2.projectPoints(unit_block_corners, self.R, self.T, self.K, None)
            unit_block_img_pts = img_pts.reshape(5, 2)
            l_p1 = unit_block_img_pts[-1]
            l_p2 = unit_block_img_pts[-2]
            self.WIDTH = math.sqrt((l_p1[0] - l_p2[0]) ** 2 + (l_p1[1] - l_p2[1]) ** 2)
            print(unit_block_img_pts)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def suck_waste():
    try:
        # Go to wast position
        c_x, c_y, waste_class_name = state.moving_box
        cur_x, cur_y, cur_z = jetmax.position
        x_, y_, _ = camera_to_world(state.K, state.R, state.T, np.array([c_x, c_y]).reshape((1, 1, 2)))[0][0]
# -----------------------------------------------------------------------------------------------------------------------------------------#
        # Suck waste
        OH = math.sqrt(cur_x**2+cur_y**2) + abs(y_)
        if y_ < 0:
            angle_OOA = math.atan(abs(y_/x_))+math.pi/2 
        else:
            angle_OOA = math.pi/2-math.atan(abs(y_/x_))
        OA = math.sqrt(x_**2+y_**2+cur_x**2+cur_y**2-2*math.sqrt((x_**2+y_**2)*(cur_x**2+cur_y**2))*math.cos(angle_OOA))
        OX = math.sqrt(cur_x**2+cur_y**2)
        alpha = OA/OX
        angle_HOA = math.degrees(math.atan(abs(x_)/OH))
        if angle_HOA > 20:
            angle_HOA+=7
        elif angle_HOA > 9.5:
            angle_HOA+=3
        
        
        
        if x_ > 0:
            jetmax.set_joint_relatively(1,angle_HOA,1)
        elif x_ < 0:
            jetmax.set_joint_relatively(1,-angle_HOA,1)
        else:
            pass

        cur_x, cur_y, cur_z = jetmax.position
        new_x,new_y = alpha*cur_x, alpha*cur_y
        print("cur_x1, cur_y1: ",cur_x,cur_y)
        jetmax.set_position((new_x, new_y, 45), 1.5)
        rospy.sleep(1.5)
        sucker.set_state(True)
        rospy.sleep(0.5)
        print("new_x, new_y: ",new_x,new_y)
        
# -----------------------------------------------------------------------------------------------------------------------------------------#
        # Go up
        cur_x, cur_y, cur_z = jetmax.position
        if cur_x > 0 :
            cur_x = 163/math.sqrt((cur_y/cur_x)**2 + 1)
        else: 
            cur_x = -163/math.sqrt((cur_y/cur_x)**2 + 1)
        if cur_y > 0 :
            cur_y = abs(cur_y/cur_x)*(163/math.sqrt((cur_y/cur_x)**2 + 1))
        else:
            cur_y = -abs(cur_y/cur_x)*(163/math.sqrt((cur_y/cur_x)**2 + 1))
        jetmax.set_position((cur_x, cur_y, 212), 1)
        rospy.sleep(1)
    finally:
        # Hold
        rospy.Publisher('/waste_classification/set_suck',UInt16,queue_size=1).publish(UInt16(data=SUCK_WASTE_HOLD))
        rospy.sleep(2.5)
        state.moving_box = None
        state.runner = None
        print("FINISHED")

def release_waste():
    rect, box, color_name = state.moving_color
    cur_x, cur_y, cur_z = jetmax.position
    x_, y_, _ = camera_to_world(state.K, state.R, state.T, np.array(rect[0]).reshape((1, 1, 2)))[0][0]
    try:
# -----------------------------------------------------------------------------------------------------------------------------------------#
        # Release waste
        OH = math.sqrt(cur_x**2+cur_y**2) + abs(y_)
        if y_ < 0:
            angle_OOA = math.atan(abs(y_/x_))+math.pi/2 
        else:
            angle_OOA = math.pi/2-math.atan(abs(y_/x_))
        OA = math.sqrt(x_**2+y_**2+cur_x**2+cur_y**2-2*math.sqrt((x_**2+y_**2)*(cur_x**2+cur_y**2))*math.cos(angle_OOA))
        OX = math.sqrt(cur_x**2+cur_y**2)
        alpha = OA/OX
        angle_HOA = math.degrees(math.atan(abs(x_)/OH))
        # if angle_HOA > 20:
        #     angle_HOA+=7
        # elif angle_HOA > 9.5:
        #     angle_HOA+=3
        
        if x_ > 0:
            jetmax.set_joint_relatively(1,angle_HOA,1)
        elif x_ < 0:
            jetmax.set_joint_relatively(1,-angle_HOA,1)
        else:
            pass

        cur_x, cur_y, cur_z = jetmax.position
        new_x,new_y = alpha*cur_x, alpha*cur_y
        print("cur_x1, cur_y1: ",cur_x,cur_y)
        jetmax.set_position((new_x, new_y, 160), 1.5)
        rospy.sleep(1.5)
        sucker.set_state(False)
        rospy.sleep(0.5)
        print("new_x, new_y: ",new_x,new_y)
        
# -----------------------------------------------------------------------------------------------------------------------------------------#
        # Go up
        cur_x, cur_y, cur_z = jetmax.position
        if cur_x > 0 :
            cur_x = 163/math.sqrt((cur_y/cur_x)**2 + 1)
        else: 
            cur_x = -163/math.sqrt((cur_y/cur_x)**2 + 1)
        if cur_y > 0 :
            cur_y = abs(cur_y/cur_x)*(163/math.sqrt((cur_y/cur_x)**2 + 1))
        else:
            cur_y = -abs(cur_y/cur_x)*(163/math.sqrt((cur_y/cur_x)**2 + 1))

        jetmax.set_position((cur_x, cur_y, 212), 1)
        rospy.sleep(1)
    except Exception as e:
        rospy.logerr("ERROR")
    finally:
        # Go home
        # state.suck_state = SUCK_WASTE_IDLE
        rospy.Publisher('/waste_classification/set_suck',UInt16,queue_size=1).publish(UInt16(data=SUCK_WASTE_IDLE))
        rospy.sleep(2.5)
        state.moving_color = None
        state.runner = None

def image_proc_suck_waste():
    ros_image = image_queue.get(block=True)
    if state.is_running is False or state.runner is not None:
        image_pub.publish(ros_image)
        return
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    outputs = yolov5.detect(image)
    boxes, confs, classes = yolov5.post_process(image, outputs, 0.85)
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
        if cls_conf < 0.85:
            continue
        if waste_class_name == state.waste_class:
            cards.append((cls_conf, x1, y1, x2, y2, waste_class_name))
            image = cv2.putText(image, waste_name + " " + str(float(cls_conf))[:4], (x1, y1 - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLORS[waste_class_name], 2)
            image = cv2.rectangle(image, (x1, y1), (x2, y2), COLORS[waste_class_name], 3)

    if len(cards) == 0:
        state.count = 0
        state.moving_box = None
    else:
        if state.moving_box is None:
            moving_box = max(cards, key=lambda card: card[0])
            conf, x1, y1, x2, y2, waste_class_name = moving_box
            c_x, c_y = (x1 + x2) / 2, (y1 + y2) / 2
            state.moving_box = c_x, c_y, waste_class_name
        else:
            l_c_x, l_c_y, l_waste_class_name = state.moving_box
            moving_box = min(cards, key=lambda card: math.sqrt((l_c_x - card[1]) ** 2 + (l_c_y - card[2]) ** 2))

            conf, x1, y1, x2, y2, waste_class_name = moving_box
            c_x, c_y = (x1 + x2) / 2, (y1 + y2) / 2

            image = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 255), 6)
            
            image = cv2.circle(image, (int(c_x), int(c_y)), 1, (255, 255, 255), 10)

            if math.sqrt((l_c_x - c_x) ** 2 + (l_c_y - c_y) ** 2) > 30:
                state.count = 0
            else:
                c_x = l_c_x * 0.2 + c_x * 0.8
                c_y = l_c_y * 0.2 + c_y * 0.8
                state.count += 1
            state.moving_box = c_x, c_y, waste_class_name
# -----------------------------------------------------------------------------------------------------------------------------------------#
            x_, y_, _ = camera_to_world(state.K, state.R, state.T, np.array([c_x, c_y]).reshape((1, 1, 2)))[0][0]
            x0, y0, cur_z = jetmax.position
            print("=================================================")
            print("x_,y_: ", x_, "",y_)
            print("cur_x,cur_y: ", x0, "",y0)
# -----------------------------------------------------------------------------------------------------------------------------------------#
            if state.count > 10 and state.suck_state== SUCK_WASTE_SUCK :
                state.count = 0
                state.runner = threading.Thread(target=suck_waste, daemon=True)
                state.runner.start()

    image = cv2.rectangle(image, (90, 125), (507, 460), (0,0,0), 3)
    rgb_image = image.tostring()
    ros_image.data = rgb_image
    image_pub.publish(ros_image)

def image_proc_release_waste():
    ros_image = image_queue.get(block=True)
    if state.is_running is False or state.runner is not None:
        image_pub.publish(ros_image)
        return
    img = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    img_h, img_w = img.shape[:2]
    frame_gb = cv2.GaussianBlur(np.copy(img), (5, 5), 5)
    frame_lab = cv2.cvtColor(frame_gb, cv2.COLOR_RGB2LAB)  # Convert rgb to lab

    blocks = []
    for color_name, color in state.target_colors.items():  # Loop through all selected colors
        frame_mask = cv2.inRange(frame_lab, tuple(color['min']), tuple(color['max']))
        eroded = cv2.erode(frame_mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        dilated = cv2.dilate(eroded, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        contours = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
        contour_area = map(lambda c: (c, math.fabs(cv2.contourArea(c))), contours)
        contour_area = list(filter(lambda c: c[1] > 1000, contour_area))  # Eliminate contours that are too small

        if len(contour_area) > 0:
            for contour, area in contour_area:  # Loop through all the contours found
                rect = cv2.minAreaRect(contour)
                center_x, center_y = rect[0]
                box = cv2.boxPoints(rect)  # The four vertices of the minimum-area-rectangle
                box_list = box.tolist()
                box = np.int0(box)
                ap = max(box_list, key=lambda p: math.sqrt((p[0] - state.K[0][2]) ** 2 + (p[1] - state.K[1][2]) ** 2))
                index_ap = box_list.index(ap)
                p1 = box_list[index_ap - 1 if index_ap - 1 >= 0 else 3]
                p2 = box_list[index_ap + 1 if index_ap + 1 <= 3 else 0]
                n_p1 = point_xy(ap, p1, state.WIDTH)
                n_p2 = point_xy(ap, p2, state.WIDTH)

                c_x, c_y = None, None
                if n_p1 and n_p2:
                    x_1, y_1 = n_p1
                    x_2, y_2 = n_p2
                    c_x = (x_1 + x_2) / 2
                    c_y = (y_1 + y_2) / 2
                    # yellow
                    cv2.circle(img, (int(n_p1[0]), int(n_p1[1])), 2, (255, 255, 0), 10)
                    # yellow
                    cv2.circle(img, (int(n_p2[0]), int(n_p2[1])), 2, (255, 255, 0), 10)
                    # black
                    cv2.circle(img, (int(c_x), int(c_y)), 2, (0, 0, 0), 10)

                # blue
                cv2.circle(img, (int(ap[0]), int(ap[1])), 2, (0, 255, 255), 10)
                cv2.drawContours(img, [box], -1, hiwonder.COLORS[color_name.upper()], 2)
                cv2.circle(img, (int(center_x), int(center_y)), 1, hiwonder.COLORS[color_name.upper()], 5)
                rect = list(rect)
                # if c_x:
                #     rect[0] = c_x, c_y
                # else:
                #     rect[0] = (center_x, center_y)
                rect[0] = (center_x, center_y)
                blocks.append((rect, box, color_name))

    if len(blocks) > 0:
        if state.moving_color is None:
            # Choose the contour with the largest area as the next target
            state.moving_color = max(blocks, key=lambda tmp: tmp[0][1][0] * tmp[0][1][1])
        else:
            # Find the rectangle with the smallest distance from the last rectangle and update the data
            rect, _, _ = state.moving_color
            moving_x, moving_y = rect[0]
            blocks = list(map(lambda tmp: (tmp, math.sqrt((moving_x - tmp[0][0][0]) ** 2 +
                                                          (moving_y - tmp[0][0][1]) ** 2)), blocks))
            blocks.sort(key=lambda tmp: tmp[1])
            moving_color, _ = blocks[0]
            x, y = moving_color[0][0]
            cv2.drawContours(img, [moving_color[1]], -1, (255, 255, 255), 2)
            # white
            cv2.circle(img, (int(x), int(y)), 1, (255, 255, 255), 5)

            state.count += 1
            if state.count > 5:
                rect, box, color_name = moving_color
                (x, y), (w, h), angle = rect
                (o_x, o_y), _, o_angle = state.moving_color[0]
                # o_x = x * 0.2 + o_x * 0.8
                # o_y = y * 0.2 + o_y * 0.8
                o_x = x
                o_y = y
                o_angle = angle * 0.2 + o_angle * 0.8
                rect = (o_x, o_y), (w, h), o_angle
                moving_color = rect, box, color_name
# -----------------------------------------------------------------------------------------------------------------------------------------#
                x_, y_, _ = camera_to_world(state.K, state.R, state.T, np.array(rect[0]).reshape((1, 1, 2)))[0][0]
                x0, y0, cur_z = jetmax.position
                print("=================================================")
                print("x_,y_: ", x_, "",y_)
                print("cur_x,cur_y: ", x0, "",y0)
# -----------------------------------------------------------------------------------------------------------------------------------------#
                if state.count > 30 and state.suck_state == SUCK_WASTE_RELEASE:
                    state.count = 0
                    state.moving_color = moving_color
                    state.runner = threading.Thread(target=release_waste, daemon=True)  # Move block
                    state.runner.start()
                state.moving_color = moving_color
    else:
        state.moving_color = None
        state.count = 0

    cv2.line(img, (int(img_w / 2 - 10), int(img_h / 2)), (int(img_w / 2 + 10), int(img_h / 2)), (0, 255, 255), 2)
    cv2.line(img, (int(img_w / 2), int(img_h / 2 - 10)), (int(img_w / 2), int(img_h / 2 + 10)), (0, 255, 255), 2)
    
    img = cv2.rectangle(img, (60, 85), (540, 460), (0,0,0), 3)
    rgb_image = img.tostring()
    ros_image.data = rgb_image
    image_pub.publish(ros_image)

def point_xy(pt_a, pt_b, r):
    x_a, y_a = pt_a
    x_b, y_b = pt_b
    if x_a == x_b:
        return x_a, y_a + (r / abs((y_b - y_a))) * (y_b - y_a)
    k = (y_a - y_b) / (x_a - x_b)
    b = y_a - k * x_a
    A = k ** 2 + 1
    B = 2 * ((b - y_a) * k - x_a)
    C = (b - y_a) ** 2 + x_a ** 2 - r ** 2
    x1 = (-B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
    x2 = (-B - math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
    y1 = k * x1 + b
    y2 = k * x2 + b
    dist_1 = math.sqrt((x1 - x_b) ** 2 + (y1 - y_b) ** 2)
    dist_2 = math.sqrt((x2 - x_b) ** 2 + (y2 - y_b) ** 2)
    if dist_1 <= dist_2:
        return x1, y1
    else:
        return x2, y2
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#
def image_callback(ros_image):
    try:
        image_queue.put_nowait(ros_image)
    except queue.Full:
        pass

def enter_func(msg):
    rospy.loginfo("enter")
    pre_exit_func()
    jetmax.go_home()
    state.reset()
    state.load_camera_params()
    state.image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)
    AIEnter_pub.publish(String(data=f'{ROS_NODE_NAME}'))
    return TriggerResponse(success=True)

def pre_exit_func():
    state.is_running = False
    if isinstance(state.heartbeat_timer, threading.Timer):
        state.heartbeat_timer.cancel()
    if isinstance(state.runner, threading.Thread):
        state.runner.join()
    if isinstance(state.image_sub, rospy.Subscriber):
        rospy.loginfo('unregister image')
        state.image_sub.unregister()
    rospy.ServiceProxy('/jetmax/go_home', Empty)()
    rospy.Publisher('/jetmax/end_effector/sucker/command', Bool, queue_size=1).publish(data=False)
    rospy.Publisher('/jetmax/end_effector/servo1/command', SetServo, queue_size=1).publish(data=90, duration=0.5)
    rospy.Publisher('/waste_classification/set_waste_class',String,queue_size=1).publish(String(data=""))
    rospy.Publisher('/waste_classification/set_suck',UInt16,queue_size=1).publish(UInt16(data=SUCK_WASTE_IDLE))

def exit_func(msg):
    rospy.loginfo("exit")
    pre_exit_func()
    AIEnter_pub.publish(String(data=""))
    AIRun_pub.publish(String(data = ""))
    return TriggerResponse(success=True)

def set_running(msg: SetBoolRequest):
    if msg.data:
        rospy.loginfo("start running")
        state.is_running = True
        rospy.Publisher('/waste_classification/set_waste_class',String,queue_size=1).publish(String(data="food_waste"))
        AIRun_pub.publish(String(data = f'{ROS_NODE_NAME}'))
    else:
        rospy.loginfo("stop running")
        state.is_running = False
        AIRun_pub.publish(String(data = ""))
    return SetBoolResponse(success=True)

def set_suck(data):
    state.suck_state = data.data

def set_waste_class(data):
    if data.data == "": return
    state.waste_class = data.data
    color_ranges = rospy.get_param('/lab_config_manager/color_range_list', {})
    state.target_colors.clear()
    state.target_colors[WASTE_CLASSES_COLORS[state.waste_class]] = color_ranges[state.waste_class]

def heartbeat_timeout_cb():
    rospy.loginfo('heartbeat timeout. exiting...')
    rospy.ServiceProxy('/%s/exit' % ROS_NODE_NAME, Trigger)

def heartbeat_srv_cb(msg: SetBoolRequest):
    if isinstance(state.heartbeat_timer, threading.Timer):
        state.heartbeat_timer.cancel()
    rospy.logdebug("Heartbeat")

    if msg.data:
        state.heartbeat_timer = threading.Timer(5, heartbeat_timeout_cb)
        state.heartbeat_timer.start()
    else:
        if isinstance(state.heartbeat_timer, threading.Timer):
            state.heartbeat_timer.cancel()
    return SetBoolResponse(success=msg.data)

    # rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)


image_queue = queue.Queue(maxsize=2)
state = WasteClassification()
state.load_camera_params()
if state.camera_params is None:
    rospy.logerr("Can not load camera parameters")
    sys.exit(-1)
yolov5 = Yolov5TensorRT(TRT_ENGINE_PATH, TRT_INPUT_SIZE, TRT_NUM_CLASSES)
image_pub = rospy.Publisher('/%s/image_result' % ROS_NODE_NAME, Image, queue_size=1)  # register result image pub
enter_srv = rospy.Service('/%s/enter' % ROS_NODE_NAME, Trigger, enter_func)
exit_srv = rospy.Service('/%s/exit' % ROS_NODE_NAME, Trigger, exit_func)
running_srv = rospy.Service('/%s/set_running' % ROS_NODE_NAME, SetBool, set_running)
heartbeat_srv = rospy.Service('/%s/heartbeat' % ROS_NODE_NAME, SetBool, heartbeat_srv_cb)
rospy.Subscriber('/%s/set_suck' % ROS_NODE_NAME,UInt16,set_suck)
rospy.Subscriber('/%s/set_waste_class' % ROS_NODE_NAME,String,set_waste_class)
AIEnter_pub = rospy.Publisher('/jetmax/AIEnterCurrent', String, queue_size=1)
AIRun_pub = rospy.Publisher('/jetmax/AIRunCurrent', String, queue_size=1)
# if __name__ == '__main__':
#     rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
#     image_queue = queue.Queue(maxsize=2)
#     state = WasteClassification()
#     state.load_camera_params()
#     if state.camera_params is None:
#         rospy.logerr("Can not load camera parameters")
#         sys.exit(-1)
#     jetmax = hiwonder.JetMax()
#     sucker = hiwonder.Sucker()
#     yolov5 = Yolov5TensorRT(TRT_ENGINE_PATH, TRT_INPUT_SIZE, TRT_NUM_CLASSES)
#     image_pub = rospy.Publisher('/%s/image_result' % ROS_NODE_NAME, Image, queue_size=1)  # register result image pub
#     enter_srv = rospy.Service('/%s/enter' % ROS_NODE_NAME, Trigger, enter_func)
#     exit_srv = rospy.Service('/%s/exit' % ROS_NODE_NAME, Trigger, exit_func)
#     running_srv = rospy.Service('/%s/set_running' % ROS_NODE_NAME, SetBool, set_running)
#     heartbeat_srv = rospy.Service('/%s/heartbeat' % ROS_NODE_NAME, SetBool, heartbeat_srv_cb)
# while True:
#     try:
        # if state.suck_state==SUCK_WASTE_IDLE or state.suck_state == SUCK_WASTE_SUCK:
        #     image_proc_suck_waste()
        # if state.suck_state==SUCK_WASTE_HOLD or state.suck_state == SUCK_WASTE_RELEASE:
        #     image_proc_release_waste()
        
#         if rospy.is_shutdown():
#            break
#     except Exception as e:
#         rospy.logerr(e)
#         break
