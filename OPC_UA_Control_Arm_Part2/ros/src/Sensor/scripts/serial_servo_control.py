#!/usr/bin/env python3

import hiwonder
import time

"""
jetmax上的舵机的位置数值范围为0～1000, 对应0～240度
需要注意， 舵机的位置数值和时间数值都需要用整数
"""

def main():
    hiwonder.serial_servo.set_position(1, 1000, 3000) #让id为1的舵机用5000毫秒时间从当前位置运动到1000位置
    time.sleep(3)
    hiwonder.serial_servo.set_position(1, 0, 8000) #让id为1的舵机用8000毫秒时间从当前位置运动到0位置
    time.sleep(8)
    #如果我们需要用角度来控制的话可以将及角度转化为数值例如现在要转转动到180度位置
    p = 180 / 240 * 1000
    hiwonder.serial_servo.set_position(1, int(p), 4000) #这就是用4000毫秒从当前位置运动到 180度位置
    hiwonder.serial_servo.set_position(1, int(120 / 240 * 1000), 2000) #这就是用2000毫秒从当前位置运动到 120度位置


if __name__ == "__main__":
    main()
