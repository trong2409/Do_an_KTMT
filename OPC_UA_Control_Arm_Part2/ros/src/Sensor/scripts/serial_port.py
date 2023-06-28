#!/usr/bin/env python3
import serial
import time

def main():
    serialHandle = serial.Serial('/dev/ttyTHS1', 115200) #初始化串口为波特率115200

    #演示控制串口收发数据，
    #短接jetmax 的 rx, tx引脚(即扩增板上的UART口中间两根引脚) 即可在屏幕上看到打印 ‘abcdefg'
    while True:
        serialHandle.write(bytes("abcdefg", encoding='utf-8')) #向串口写入数据, 数据需要时bytes， bytearray
        time.sleep(1)

        count = serialHandle.inWaiting() #获取串口接收缓存中接收到的数据的字节数
        recv_data = serialHandle.read(count) #将接收到的字节读取出来
        print(recv_data)
        time.sleep(1)


if __name__=='__main__':
    main()
