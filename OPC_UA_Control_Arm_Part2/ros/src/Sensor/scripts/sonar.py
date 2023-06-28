#!/usr/bin/env python3

import hiwonder

import time

"""
超声波灯光控制及距离读取

超声波模块需要连接到jetmax的I2C接口
任意时刻只能连接一个超声波模块
"""

def main():
    # 超声波的灯光有有两种模式， 模式0 用户直接控制灯光发出某种颜色, 模式1控制灯光周期变化
    hiwonder.sonar.set_rgb_mode(0) #设置为模式0
    # 超声波的两个"眼睛" 对应两个灯用0, 1 表示
    hiwonder.sonar.set_color(0, 0xFF0000)  #0 号灯设为 红色 0xFF0000 是要发出的灯光的RGB值
    hiwonder.sonar.set_color(1, 0x00FF00) #1号灯设为 绿色 
    time.sleep(2)


    hiwonder.sonar.set_rgb_mode(1) #设置为 模式1
    hiwonder.sonar.set_breath_cycle(0, 0, 0) #将0号灯的红色设置的呼吸亮灭周期设为0, 就是完全熄灭
    hiwonder.sonar.set_breath_cycle(0, 1, 0) #将0号灯的绿色设置的呼吸亮灭周期设为0, 就是完全熄灭
    hiwonder.sonar.set_breath_cycle(0, 2, 1000) #将0号灯的色蓝色设置的呼吸亮灭周期设为1000毫秒
    #这时候可以看到0号灯回以蓝色1000毫秒周期呼吸亮灭
    time.sleep(2)
    hiwonder.sonar.set_breath_cycle(1, 0, 500) #将1号灯的红色设置的呼吸亮灭周期设为500毫秒
    hiwonder.sonar.set_breath_cycle(1, 1, 0) #将1号灯的绿色设置的呼吸亮灭周期设为0,  就是完全熄灭
    hiwonder.sonar.set_breath_cycle(1, 2, 1000) #将1号灯的色蓝色设置的呼吸亮灭周期设为1000毫秒
    #这时候可以看到1号灯回以蓝色1000毫秒周期呼吸亮灭,红色以500毫秒亮灭
    time.sleep(2)


    #此外可以使用start_symphony来让rgb灯自行幻彩变化
    hiwonder.sonar.start_symphony()


    distance = None
    last_print_time = time.time()
    while True:
        d = hiwonder.sonar.get_distance() #读取超声波的距离， 单位为毫秒

        #我们可以做点简单的滤波应对可能出现的跳变和错误数据
        if distance is None:
            distance = d
        else:
            distance = distance * 0.6 + d * 0.4 #这次测量的距离权重0.4, 之前数值权重0.6

        #1秒打印一次数据
        if last_print_time < time.time():
            last_print_time = time.time() + 1
            print(distance)

        #0.1秒读取一次超声波数据
        time.sleep(0.1)


if __name__ == "__main__":
    main()
