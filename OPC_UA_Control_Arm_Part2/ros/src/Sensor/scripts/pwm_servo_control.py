#!/usr/bin/env python3

import hiwonder
import time

"""
控制pwm舵机转动
"""

def main():
    while True:
        #控制1号pwm舵机
        hiwonder.pwm_servo1.set_position(90, 1) #用1秒转动到90度位置
        time.sleep(2)
        hiwonder.pwm_servo1.set_position(180, 1) #用1秒转动到180度位置
        time.sleep(2)
        hiwonder.pwm_servo1.set_position(0, 2) #用2秒转动到0度位置
        time.sleep(3)


if __name__ == "__main__":
    main()
