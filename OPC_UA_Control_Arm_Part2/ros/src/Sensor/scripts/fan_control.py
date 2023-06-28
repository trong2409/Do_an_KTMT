#!/usr/bin/env python3

import time
import Jetson.GPIO as GPIO

"""
控制风扇模块
风扇模块上有独立的马达驱动电路， 需要使用两个io口来控制其正反转， 或者两个io口通过pwm控制其速度
可以将风扇模块使用4pin 线连接到 jetmax 扩展板上的 GPIO2 上
其对应的引脚是 gpio9, 和gpio4
"""

#初始化io口
def init_fan():
    GPIO.setmode(GPIO.BCM) #设置gpio控制库为bcm模式
    GPIO.setup(9, GPIO.OUT) #将gpio 9 设置 输出
    GPIO.output(9, 0)
    GPIO.setup(4, GPIO.OUT) #将gpio 9 设置 输出
    GPIO.output(4, 0)


def main():
    init_fan()

    # 通过两个io口的高低电平控制正反转
    # 两个io口均为低电平时 停止转动
    # 一高一低对应两个方向
    # 要控制速度， 就保持一个io口为低电平， 另一个输出pwm

    #正转100%速度
    GPIO.output(4, 1)
    GPIO.output(9, 0)
    time.sleep(1)

    #停止转动
    GPIO.output(9, 0)
    GPIO.output(4, 0)
    time.sleep(1)

    #反转
    GPIO.output(4, 0)
    GPIO.output(9, 1)
    time.sleep(1)


    #停止转动
    GPIO.output(9, 0)
    GPIO.output(4, 0)
    time.sleep(1)


    #要控制数度就要其中一个口输出pwm
    # 例如50%占空比
    t = time.time() + 2
    while time.time() < t:
        GPIO.output(4, 1)
        GPIO.output(9, 0)
        time.sleep(0.01)
        GPIO.output(9, 0)
        GPIO.output(4, 0)
        time.sleep(0.01)



if __name__ == "__main__":
    main()
