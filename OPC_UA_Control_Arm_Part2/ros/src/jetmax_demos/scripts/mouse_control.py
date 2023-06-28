#!/usr/bin/env python3

import sys
import math
import re
import sys
import math
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPainter, QPen)
from PyQt5.QtCore import Qt
import time
import hiwonder

jetmax = hiwonder.JetMax()
sucker = hiwonder.Sucker()

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        #resize设置宽高，move设置位置
        self.resize(1200, 900)
        self.move(100, 100)
        self.setWindowTitle("简单的画板4.0")

        #setMouseTracking设置为False，否则不按下鼠标时也会跟踪鼠标事件
        self.setMouseTracking(False)
        self.enable = False

    def mouseMoveEvent(self, event):
        '''
            按住鼠标移动事件：将当前点添加到pos_xy列表中
            调用update()函数在这里相当于调用paintEvent()函数
            每次update()时，之前调用的paintEvent()留下的痕迹都会清空
        '''
        #中间变量pos_tmp提取当前点
        x, y = (event.pos().x(), event.pos().y())
        if self.enable:
            new_x = hiwonder.misc.val_map(x, 0, 1200, -120, 120)
            new_y = hiwonder.misc.val_map(y, 0, 900, -200, -40)
            old_x, old_y, old_z = list(jetmax.position)
            t = math.sqrt((new_x - old_x) ** 2 + (new_y - old_y) ** 2) / 150
            print(t)
            jetmax.set_position((new_x, new_y, old_z), t)
            time.sleep(t)

    def mousePressEvent(self, event):
        if(event.button() == Qt.RightButton):
            sucker.set_state(True)
        if(event.button() == Qt.LeftButton):
            self.enable = True


    def mouseReleaseEvent(self, event):
        if(event.button() == Qt.RightButton):
            sucker.release(2)
        if(event.button() == Qt.LeftButton):
            self.enable = False

    def wheelEvent(self, event):
        pos = list(jetmax.position)
        delta = event.angleDelta().y()
        if delta < 0:
            pos[2] = pos[2] - 1
        else:
            pos[2] = pos[2] + 1
        jetmax.set_position(pos, 0.05)


if __name__ == "__main__":
    jetmax.go_home(1)
    time.sleep(1)
    app = QApplication(sys.argv)
    pyqt_learn = Example()
    pyqt_learn.show()
    app.exec_()
