#!/usr/bin/env python3
import os
import sys
import cv2
import rospy
import numpy as np
import threading
import hiwonder
import Jetson.GPIO as GPIO
import time

"""
触摸传感器控制臂
短按执行一个动作
连续短按连次就是复位
长按机械臂向下运动，需要一定值后自动复位
"""

ROS_NODE_NAME = "touch_control"

if __name__ == '__main__':
    rospy.init_node(ROS_NODE_NAME, log_level=rospy.DEBUG)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9, GPIO.IN)
    jetmax = hiwonder.JetMax()
    jetmax.go_home(2)
    rospy.sleep(2)
    last_state = 1
    press_time = time.time()
    longpress_time = time.time()
    short_count = 0
    next_short_time = time.time()
    
    def x_short(n):
        print('短按%d次' % n)
        if n == 1:
            jetmax.set_position((jetmax.ORIGIN[0], jetmax.ORIGIN[1], 70), 1)
            rospy.sleep(1.1)
            jetmax.set_servo(1, int(210 / 240 * 1000), 1)
            rospy.sleep(1.1)
            pos = list(jetmax.position)
            pos[2] += 100
            jetmax.set_position(pos, 1)
            rospy.sleep(1.1)
            jetmax.go_home(1)
            rospy.sleep(1.1)
        elif n == 2:
            jetmax.go_home()
            rospy.sleep(1.1)
        else:
            pass

    while not rospy.is_shutdown():

        if next_short_time < time.time() and short_count > 0: #如果距离上次短按超过设定时间就执行短按动作
            x_short(short_count)
            short_count = 0

        current_state = GPIO.input(9) #获取当前状态
        if current_state != last_state: #新旧状态不同， 就是触摸按钮被操作了
            if current_state == 0: #如果新状态为0, 就是被按下的
                print("按钮被按下")
                pressed_time = time.time() #记下被按下时的时刻
                longpress_time = pressed_time
            else: #如果新状态为1, 就是被松开
                print("按钮被松开", end='')
                if pressed_time == longpress_time:
                    print(", 是短按")
                    short_count += 1
                    next_short_time = time.time() + 0.5 #0.5秒内按下第二次就是连按
                else:
                    print(", 是长按")
                
        else: #如果新旧状态相同， 就是没有操作按钮， 或者一直按着按钮
            if current_state == 0: #如果按钮是被按着的
                dur = time.time() - pressed_time  #计算一下被按了多久
                if dur > 2:
                    print("按钮被长按")
                    longpress_time = time.time()
                    pos = list(jetmax.position)
                    pos[2] -= 2
                    if pos[2] <= 60:
                        jetmax.go_home()
                        rospy.sleep(1.1)
                    else:
                        jetmax.set_position(pos, 0.05)
        last_state = current_state #将新状态存起来
        time.sleep(0.05) #50毫秒刷新一次按钮状态



