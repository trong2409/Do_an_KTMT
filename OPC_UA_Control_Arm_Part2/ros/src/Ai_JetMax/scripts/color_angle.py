#!/usr/bin/env python3
import sys
import cv2
import math
import threading
import numpy as np
import rospy
from sensor_msgs.msg import Image
import hiwonder

ROS_NODE_NAME = "color_angle"
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


class State:
    def __init__(self):
        self.target_colors = {}
        self.runner = None
        self.camera_params = None
        self.K = None
        self.R = None
        self.T = None
        self.WIDTH = None


    def load_camera_params(self):
        global unit_block_img_pts
        self.camera_params = rospy.get_param('/camera_cal/block_params', self.camera_params)
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


def image_proc(img):
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

                cv2.drawContours(img, [box], -1, hiwonder.COLORS[color_name.upper()], 2)
                cv2.circle(img, (int(center_x), int(center_y)), 1, hiwonder.COLORS[color_name.upper()], 5)
                angle = rect[2]
                angle = angle - 90 if angle > 45 else angle
                s = "Angle:{:0.2f}deg".format(angle)
                cv2.putText(img, s, (int(center_x), int(center_y)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                print(s)

    cv2.line(img, (int(img_w / 2 - 10), int(img_h / 2)), (int(img_w / 2 + 10), int(img_h / 2)), (0, 255, 255), 2)
    cv2.line(img, (int(img_w / 2), int(img_h / 2 - 10)), (int(img_w / 2), int(img_h / 2 + 10)), (0, 255, 255), 2)
    print("\n")

    return img


def image_callback(ros_image):
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    frame_result = np.copy(image)
    frame_result = image_proc(frame_result)
    image_bgr = cv2.cvtColor(frame_result, cv2.COLOR_RGB2BGR)
    cv2.imshow("result", image_bgr)
    cv2.waitKey(1)


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    state = State()
    state.load_camera_params()
    if state.camera_params is None:
        rospy.logerr("Can not load camera params")
        sys.exit(-1)
    jetmax = hiwonder.JetMax()
    jetmax.go_home()
    rospy.sleep(1)
    state.target_colors = rospy.get_param('/lab_config_manager/color_range_list', {})
    del[state.target_colors['white']]
    del[state.target_colors['black']]
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        sys.exit(0)
