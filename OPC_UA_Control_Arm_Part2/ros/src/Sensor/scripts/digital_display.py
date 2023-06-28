#!/usr/bin/env python3

import hiwonder
import time

"""
将led点阵模块连接到jetmax 的GPIO2口
"""

# 字模数据
font = {'0':0x3f,'1':0x06,'2':0x5b,'3':0x4f,'4':0x66,'5':0x6d,'6':0x7d,'7':0x07,'8':0x7f,'9':0x6f, '-': 0x40}

def main():
    mtx = hiwonder.TM1640(4, 9) #4, 9 对应 clk， dio 引脚号
    mtx.gram = [0xFF] * 4 #gram用作点阵的显存， 共4个字节， 一个字节对应一位数字
    time.sleep(1)
    

    #显示整数
    def display_int(num):
        s = str(num) #将数转为字符串
        buf = [font[c] for c in s[:4]] #只显示数值的前4位数字
        mtx.gram = buf
        if len(buf) < 4: #如果不够4位，前面填充0, 这样数字就会靠右显示
            buf_zero = [0] * (4 - len(buf))
            buf_zero.extend(buf)
            mtx.gram = buf_zero
        mtx.refresh()
    for i in range(-1000,1222, 13):
        display_int(i)

    #显示小数
    def display_float(num):
        s = "{:0.1f}".format(num) #将数字转为字符串保留1位小数
        buf = []
        for c in s:
            if c in font:
                buf.append(font[c])
            else:
                if c == '.': #如果是小数点， 将前面一位数字的显示增加小点
                    buf[-1] = buf[-1] | 0x80
        mtx.gram = buf
        if len(buf) < 4: #如果不够4位，前面填充0, 这样数字就会靠右显示
            buf_zero = [0] * (4 - len(buf))
            buf_zero.extend(buf)
            mtx.gram = buf_zero
        mtx.refresh()

    i = -10.0
    while i < 10.0:
        display_float(i)
        i += 0.1

    while True:
        display_int(int(hiwonder.sonar.get_distance()))
        time.sleep(0.2)

if __name__ == '__main__':
    main()
