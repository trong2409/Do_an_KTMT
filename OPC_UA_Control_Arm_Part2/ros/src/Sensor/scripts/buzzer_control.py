#!/usr/bin/env python3

import hiwonder
import time

"""
控制蜂鸣器
"""

def main():
    while True:
        #jetmax上的蜂鸣器为有源蜂鸣器只能控制开关，不可控制音调
        for i in range(5):
            hiwonder.buzzer.on() #打开蜂鸣器
            time.sleep(0.1) #
            hiwonder.buzzer.off() #关闭蜂鸣器
            time.sleep(0.1)

        time.sleep(1)


if __name__ == "__main__":
    main()
