#!/usr/bin/env python3
# encoding:utf-8
import sys
import time
import numpy as np
from math import *
import threading
import multiprocessing
import matplotlib.pyplot as plt
import hiwonder

jetmax = hiwonder.JetMax()

turning_radius = 25

ax = []                    # 定义一个 x 轴的空列表用来接收动态的数据
ay = []                    # 定义一个 y 轴的空列表用来接收动态的数据
#传感器最大接收数值，距离大于600mm时超声波传感器易被干扰
maximum_range=50
time.sleep(3)   

hiwonder.sonar.set_rgb_mode(0)
hiwonder.sonar.start_symphony()  # 设置超声波RGB颜色渐变模式

#旋转半径R
# 计算出在旋转半径为R、角度a时机械臂逆运动学算法输入参数
def angle(a,R=turning_radius):
    x=0.0
    y=0.0
    if  a>=0 and a <=180:
        if a==0:
            x=R
            y=0.0
            return x,y
        elif a == 90:
            x=0
            y=R
            return x,y
        elif a==180:
            x=-R
            y=0.0
            return x,y
        else:
            y= sin(pi/180*a)*R
            x= y/tan(pi/180*a)
            return x,y
    else:
        pass

plt.ion()                  # 开启一个画图的窗口
plt.xlim(-maximum_range, maximum_range)
plt.ylim(0, maximum_range)
plt.grid(True)

end = 0
start = 0
noise = 0
count = 0
error = 20
distance = 0

def two_dimensional_scatter_diagram():
    z=[0,0]
    flag =1
    # 扫描角度
    # 步长越大越块相应的数据也越少
    step=2#
    #机械臂运动速度 由于实时画图需要一定时间导致此值过小也不会太快而且会有卡顿感
    speed=50
    sp=speed/1000

    Detection_Angle=180
    data = np.zeros(Detection_Angle+1, dtype = np.int) 
    x_y_data=np.zeros((Detection_Angle+1,2), dtype = np.float) 

    z[0],z[1]=angle(0) 
    time.sleep(2.2)

    begin_time=0
    end_time=0
    jetmax.go_home()
    time.sleep(1)
    cur = list(jetmax.position)
    cur[1] += 120
    jetmax.set_position(cur, 1)
    time.sleep(1)
    jetmax.set_joint(1, 30, 1)
    time.sleep(1)
    while True:
            if flag:                                                            #flag控制机械臂左转后右转
                for j in range(0,Detection_Angle+1,step):                       #Detection_Angle控制探测角度
                    z[0], z[1] = angle(j)
                    end_time = time.time()
                    run_time = end_time-begin_time
                    if sp>run_time:
                        time.sleep(abs(sp-run_time)*0.9)
                    jetmax.set_joint(1, 30 + j, sp)
                    begin_time = time.time()
                    data[j]=hiwonder.sonar.get_distance() / 10
                    if data[j] > maximum_range:  #当
                        data[j]=maximum_range
                    x=z[0]*data[j]/turning_radius
                    y=z[1]*data[j]/turning_radius
                    print(data[j])                
                    ax.append(x)# 添加 i 到 x 轴的数据中
                    ay.append(y)  # 添加 i 的平方到 y 轴的数据中
                    plt.xlim(-maximum_range, maximum_range)
                    plt.ylim(0, maximum_range)
                    plt.grid(True)
                    plt.plot(ax[-2:], ay[-2:])
                    plt.pause(0.0000001)# 暂停一下
                flag = 0  # 切换转动方向
                plt.clf()
                ax.clear()
                ay.clear()
            else:
                for j in range(Detection_Angle,-1,-step):
                    z[0], z[1] = angle(j)
                    end_time = time.time()
                    run_time = end_time-begin_time
                    if sp>run_time:
                        time.sleep(abs(sp-run_time)*0.9)
                    jetmax.set_joint(1,  30 + j, sp)
                    begin_time = time.time()
                    data[j]=hiwonder.sonar.get_distance() / 10
                    if data[j] > maximum_range:
                        data[j]=maximum_range
                    x=z[0]*data[j]/turning_radius
                    y=z[1]*data[j]/turning_radius
                    ax.append(x) # 添加 i 到 x 轴的数据中
                    ay.append(y) # 添加 i 的平方到 y 轴的数据中
                    plt.xlim(-maximum_range, maximum_range)
                    plt.ylim(0, maximum_range)
                    plt.grid(True)
                    plt.plot(ax[-2:], ay[-2:])
                    plt.pause(0.000001)  # 暂停一下
                flag = 1
                plt.clf()
                ax.clear()
                ay.clear()

if __name__ == "__main__":
    two_dimensional_scatter_diagram()



