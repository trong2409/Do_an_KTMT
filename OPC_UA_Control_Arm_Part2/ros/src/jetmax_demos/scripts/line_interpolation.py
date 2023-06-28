import sys
import math


def linear_interpolation(x_start, y_start,  x_end, y_end):
    points = []
    distance = 0
    x_err, y_err = 0, 0
    inc_x, inc_y = 0, 0
    delta_x, delta_y = 0, 0
    u_row, u_col = x_start, y_start
    delta_x = x_end - x_start  #计算坐标增量
    delta_y = y_end - y_start

    if delta_x > 0 :
        inc_x = 1    #设置单步方向
    elif delta_x == 0:
        inc_x = 0    #垂直线
    else:
        inc_x = -1
        delta_x = -delta_x


    if delta_y > 0:
        inc_y = 1
    elif delta_y == 0:
        inc_y = 0    #水平线
    else:
        inc_y = -1
        delta_y = -delta_y
    
    if delta_x > delta_y:
        distance = delta_x    #选取基本增量坐标轴
    else:
        distance = delta_y

    for i in range(int(distance) + 1 + 1): #画线输出
        points.append([u_row, u_col])
        x_err += delta_x
        y_err += delta_y
        #print(x_err, y_err)
        if x_err > distance:
            x_err -= distance
            u_row += inc_x

        if y_err > distance:
            y_err -= distance
            u_col += inc_y

    return points[1:]

sys.modules[__name__] = linear_interpolation
