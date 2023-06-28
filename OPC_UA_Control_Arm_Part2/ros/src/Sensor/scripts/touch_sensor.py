#!/usr/bin/env python3

import Jetson.GPIO as GPIO
import time

"""
触摸传感器读取实验
触摸传感器是简单的数字io传感器， 只要读取对应IO口的电平变化即可

这里我们把传感器连接到jetmax的GPIO2接口上， 读取gpio9 引脚的电平即可获取到触摸传感器的状态
根据状态可以判断长按断按等

需要注意当触摸传感器没被按下时输出高电平， 被按下输出低电平
"""


def main():
    #初始化io口
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9, GPIO.IN)
    last_state = 1
    press_time = time.time()
    longpress_time = time.time()
    while True:
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
                else:
                    print(", 是长按")
                
        else: #如果新旧状态相同， 就是没有操作按钮， 或者一直按着按钮
            if current_state == 0: #如果按钮是被按着的
                dur = time.time() - pressed_time  #计算一下被按了多久
                if dur > 2 and longpress_time < time.time(): #按住超过2秒就是长按, longpress_time 控制每秒打印一次长按时间
                    print("按钮被长按， 按了%d秒" % dur )
                    longpress_time = time.time() + 1
        last_state = current_state #将新状态存起来
        time.sleep(0.05) #50毫秒刷新一次按钮状态

if __name__ == '__main__':
    main()
