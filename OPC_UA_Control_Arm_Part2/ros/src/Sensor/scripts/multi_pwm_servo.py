#!/usr/bin/env python3

import hiwonder
import time

"""
控制多个pwm舵机转动
"""

def main():
    while True:
        #控制多个pwm舵机， 只需要将舵机对象的名在最后的数改为对应舵机号即可

        hiwonder.pwm_servo1.set_position(90, 1) #控制1号舵机用1秒转动到90度位置
        hiwonder.pwm_servo2.set_position(90, 1) #控制2号舵机用1秒转动到90度位置
        time.sleep(2)

        #你还可以通过getattr()来获取对应的对象进行操作
        def set_pwm_servo(id_, pos, duration):
            getattr(hiwonder, "pwm_servo%d"%id_).set_position(pos, duration)

        set_pwm_servo(1, 180, 1) #控制1号舵机用1秒转动到180度位置
        set_pwm_servo(2, 0, 2) #控制2号舵机用2秒转动到0度位置

        time.sleep(3)
        


if __name__ == "__main__":
    main()
