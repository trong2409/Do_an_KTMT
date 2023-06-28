#!/usr/bin/env python3

import hiwonder
import time

"""
控制pwm舵机按速度转动
"""

def main():
    while True:
        #控制1号pwm舵机
        hiwonder.pwm_servo1.set_position(90, 1) #用1秒转动到90度位置
        time.sleep(2)
        #通过角速度计算舵机需要的运动时间
        # 控制舵机用20度每秒的速度从90度转动到180度
        t = (180 - 90) / 20
        hiwonder.pwm_servo1.set_position(180, t)
        time.sleep(t + 1)
        # 控制舵机用40度每秒的速度从180度转动到0度
        t = (180 - 0) / 40
        hiwonder.pwm_servo1.set_position(0, t)
        time.sleep(t + 1)




if __name__ == "__main__":
    main()
