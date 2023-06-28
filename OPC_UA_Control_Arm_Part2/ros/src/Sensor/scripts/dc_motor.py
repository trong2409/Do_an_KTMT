#!/usr/bin/env python3

import hiwonder
import time

"""
控制多个pwm舵机转动
"""

def main():
    while True:
        #jetmax 上一共有3个直流马达接口, 最大输出电压为电源输入电压
        
        #速度范围为-100~+100， 0为停止
        # + - 对应方向， 数值只能为整数

        hiwonder.motor1.set_speed(100) #控制1号电机速度为100
        hiwonder.motor2.set_speed(-100) #控制2号电机速度为-100
        time.sleep(2)

        #你还可以通过getattr()来获取对应的对象进行操作
        def set_motor(id_, speed):
            getattr(hiwonder, "motor%d"%id_).set_speed(speed)

        set_motor(1, 0) #控制1号电机速度为0
        set_motor(2, 0) #控制2号电机速度为0
        set_motor(3, 0) #控制3号电机速度为0

        time.sleep(5)
        


if __name__ == "__main__":
    main()
