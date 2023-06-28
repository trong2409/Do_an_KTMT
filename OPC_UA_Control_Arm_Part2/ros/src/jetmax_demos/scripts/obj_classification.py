#!/usr/bin/env python3
import math
import sys
import rospy
import time
import queue
import threading
from sensor_msgs.msg import Image as RosImage
import cv2
import numpy as np
import hiwonder
import torch
from torchvision.models import GoogLeNet
from torchvision import transforms
from PIL import Image

ROS_NODE_NAME = 'obj_cls'
DEFAULT_X, DEFAULT_Y, DEFAULT_Z = 0 + 10, 138 + 8.14, 84 + 128.4 - 5
image_queue = queue.Queue(maxsize=3)
jetmax = hiwonder.JetMax()

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = GoogLeNet(num_classes=10, aux_logits=False, init_weights=True)  # googLeNet
model.to(device)  # 将模型加载到设备中， 正常情况下在jetson nano就是加载到gpu上面
model_weight_path = "./models/googLeNet.pth"
missing_keys, unexpected_keys = model.load_state_dict(torch.load(model_weight_path), strict=False)  # 加载模型权重数据
# 模型包含的分类
classes = {
    "0": "apple",
    "1": "banana",
    "2": "bell_pepper",
    "3": "nothing",
    "4": "carrot",
    "5": "lemon",
    "6": "lettuce",
    "7": "mango",
    "8": "potato",
    "9": "red_chili"
}
# 将所有分类又再分为水果和蔬菜
vg = ["bell_pepper", "carrot", "lettuce", "potato", "red_chili"]  # 蔬菜
fu = ["apple", "banana", "lemon", "mango"]  # 水果

# 对图像的预处理操作
data_transform = transforms.Compose([
    transforms.Resize((223, 224)),  # 缩放
    transforms.ToTensor(),  # 转换为tensor对象
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])  # 归一化


class Classification:
    def __init__(self):
        self.position = DEFAULT_X, DEFAULT_Y, DEFAULT_X
        self.lock = threading.RLock()
        self.fps = 0.0
        self.last_class = 3
        self.args = [0] * 10
        self.count = 0
        self.tic = time.time()
        self.runner = None


state = Classification()


def move_1(name):
    """
    水果搬运过程
    :param name:  水果的名字
    :return:
    """
    # 不同的水果， 有不同的大小， 根据大小有不同的爪子开合程度
    if name == "banana":
        jetmax.set_position((10, 200, 50), 1)
        rospy.sleep(1)
        hiwonder.pwm_servo2.set_position(70, 0.7)
        rospy.sleep(0.8)
    elif name == " lemon":
        jetmax.set_position((10, 200, 70), 1)
        rospy.sleep(1)
        hiwonder.pwm_servo2.set_position(50, 0.7)
        rospy.sleep(0.8)
    else:
        jetmax.set_position((10, 200, 50), 1)
        rospy.sleep(1)
        hiwonder.pwm_servo2.set_position(50, 0.7)
        rospy.sleep(0.8)

    # 前往目标位置
    jetmax.set_position((10, 200, 180), 1)
    rospy.sleep(1)
    jetmax.set_position((180, -40, 180), 2)
    rospy.sleep(2.1)
    # 松开爪子
    hiwonder.pwm_servo2.set_position(90, 0.8)
    rospy.sleep(0.8)
    # 回初位
    jetmax.go_home(2)
    rospy.sleep(2.2)


def move_2(name):
    """
    蔬菜搬运
    :param name:  蔬菜的名字
    :return:
    """
    # 不同的蔬菜， 有不同的大小， 根据大小有不同的爪子开合程度
    if name == "lettuce":
        jetmax.set_position((10, 200, 50), 1)
        rospy.sleep(1)
        hiwonder.pwm_servo2.set_position(50, 0.7)
        rospy.sleep(0.8)
    elif name == "bell_pepper":
        jetmax.set_position((10, 200, 50), 1)
        rospy.sleep(1)
        hiwonder.pwm_servo2.set_position(60, 0.7)
        rospy.sleep(0.8)
    elif name == "potato":
        jetmax.set_position((10, 200, 50), 1)
        rospy.sleep(1)
        hiwonder.pwm_servo2.set_position(50, 0.7)
        rospy.sleep(0.8)
    else:
        jetmax.set_position((10, 200, 40), 1)
        rospy.sleep(1)
        hiwonder.pwm_servo2.set_position(70, 0.7)
        rospy.sleep(0.8)

    # 前往目标位置
    jetmax.set_position((10, 200, 180), 1)
    rospy.sleep(1)
    jetmax.set_position((-180, -20, 220), 2)
    rospy.sleep(2.1)
    # 松开爪子
    hiwonder.pwm_servo2.set_position(90, 0.8)
    rospy.sleep(0.8)
    # 回初位
    jetmax.go_home(2)
    rospy.sleep(2.2)


def image_proc():
    image = image_queue.get(block=True)
    image = image_proc_a(image)
    toc = time.time()
    curr_fps = 1.0 / (state.tic - toc)
    state.fps = curr_fps if state.fps == 0.0 else (state.fps * 0.95 + curr_fps * 0.05)
    state.tic = toc


def image_proc_a(image):
    ta = time.time()
    img = Image.fromarray(image.astype('uint8'), 'RGB')  # 转换为PIL格式的图片数据
    img = data_transform(img)  # 对数据进行预处理
    img = torch.unsqueeze(img, dim=0)  # 升维， 单张图片的小批量数据
    img = img.to(device)  # 将数据加载到gpu上
    model.eval()
    with torch.no_grad():
        output = torch.squeeze(model(img))  # 数据输入处理并对输出降维
        predict = torch.softmax(output, dim=0)  # 归一化输出
        predict_cla = torch.argmax(predict).cpu().numpy()  # 获取所有分类中概率最大的分类，并转换回cpu数据
        predict = tuple(predict.cpu().numpy())  # 获取所有分类的概率
        state.args = predict  # 暂存结果

        # 打印所有分类的概率
        for i in range(10):
            print(classes[str(i)] + ': {:.2f}'.format(predict[i]))
        print("==>>" + classes[str(predict_cla)])

        # 这次识别的结果与上次结果相同则增加计数
        if state.last_class == predict_cla:
            state.count += 1
        else:
            state.last_class = predict_cla
            state.count = 0
        # 计数到一定值认为识别结果可靠
        if state.count > 10 and (state.runner is None or not state.runner.isAlive()):
            # 根据识别的结果判断是否在水果的分类内， 如果在就启动搬运动作，搬运到水果篮中
            if classes[str(predict_cla)] in fu:
                state.count = 0
                state.runner = threading.Thread(target=move_1, args=(classes[str(state.last_class)],), daemon=True)
                state.runner.start()
            # 如果结果在蔬菜分类内就搬运到蔬菜篮中
            elif classes[str(predict_cla)] in vg:
                state.count = 0
                state.runner = threading.Thread(target=move_2, args=(classes[str(state.last_class)],), daemon=True)
                state.runner.start()
            else:
                pass
    return image


def image_callback(ros_image):
    image = np.ndarray(shape=(ros_image.height, ros_image.width, 3), dtype=np.uint8, buffer=ros_image.data)
    t_img = np.copy(image)
    try:
        image_queue.put_nowait(t_img)  # 将画面压入队列， 进行识别处理
    except queue.Full:
        pass

    # 在画面中画出结果， 这里画出来的结果不是这一帧的， 而是之前缓存的。 因为才刚压入队列，没来得及处理呢。 但是影响并不大
    pos = [10, 20]
    for i in range(10):  # 逐个画出分类的概率
        color = (255, 0, 255)
        if state.last_class == i:
            color = (255, 255, 0)
        s = classes[str(i)] + ': {:.2f}'.format(state.args[i])
        image = cv2.putText(image, s, tuple(pos), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        pos[1] += 30

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # 转换为BGR空间
    cv2.imshow(ROS_NODE_NAME, image)  # 显示结果图片
    cv2.waitKey(1)


if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    hiwonder.pwm_servo1.set_position(90, 1)
    jetmax.go_home(1)
    rospy.sleep(1.1)
    image_sub = rospy.Subscriber('/usb_cam/image_rect_color', RosImage, image_callback)  # 订阅摄像头画面
    while True:
        try:
            image_proc()
            if rospy.is_shutdown():
                break
        except KeyboardInterrupt:
            break
