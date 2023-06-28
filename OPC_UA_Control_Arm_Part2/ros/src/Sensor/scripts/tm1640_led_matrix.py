#!/usr/bin/env python3

import hiwonder
import time

"""
将led点阵模块连接到jetmax 的GPIO2口
"""


def main():
    mtx = hiwonder.TM1640(4, 9) #4, 9 对应 clk， dio 引脚号
    mtx.gram = [0xFF] * 16 #gram用作点阵的显存， 共16个字节， 一个字节对应一列led点, 这里就是将所有点都点亮
    print(mtx.gram)
    mtx.refresh() #设置了显存之后调用 refresh 将显存内容显示出来
    time.sleep(2)

    #可以使用set_bit来设置显存内某个点的亮灭
    # set_bit(x, y, 新状态) 0代表灭， 1代表亮
    for y in range(8):
        for x in range(0, 16, 4):
            mtx.set_bit(x, y, 0)
            mtx.set_bit(x+1, y, 0)
            mtx.set_bit(x+2, y, 0)
            mtx.set_bit(x+3, y, 0)
            mtx.refresh()

    #可以用字符来组成图画然后画出来
    smile = """__XXXX____XXXX__
               _X____X__X____X_
               ________________
               ________________
               ________________
               __X__________X__
               ___X________X___
               ____XXXXXXXX____""".replace(' ', '').split('\n')
    print(smile)
    for y in range(8):
        for x in range(16):
            mtx.set_bit(x, y, 1 if smile[y][x] == 'X' else 0)
    mtx.refresh()
    time.sleep(3)

    #清空屏幕
    mtx.gram = [0] * 16 
    mtx.refresh()

        
            


if __name__ == '__main__':
    main()
