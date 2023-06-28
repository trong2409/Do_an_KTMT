#!/usr/bin/env python3

import hiwonder
import time

"""
如果需要用角速度来控制舵机的转动我们需要自己计算舵机从当前位置转动到目标位置的时间
"""

def main():
    #让id为1的舵机用500毫秒时间从当前位置运动到200位置, 并记下当前位置
    #记下当前位置是为了通过目标角速度计算到达目标位置需要的时间
    #当前位置也能通过与舵机通信来读取，读取较慢且麻烦,可以用变量记下来
    hiwonder.serial_servo.set_position(1, 200, 500) 
    time.sleep(2)

    #假如现在要用每秒50度的速度转到800位置可以这么计算
    angle = 200 / 1000 * 240 # 将当前位置数值转换为角度数值
    t_angle = 800 / 1000 * 240 # 将目标位置数值转换为角度数值
    th = angle - t_angle #计算当前角度与目标角度的差
    t = abs(th / 50) #通过角速度50 计算转到目标位置需要的时间, 我们要计算时间， 时间不能为负值
    hiwonder.serial_servo.set_position(1, 800, int(t * 1000)) #因为角速度为度每秒， 这里将秒转换为毫秒
    time.sleep(t)   


if __name__ == "__main__":
    while True:
        main()
        



