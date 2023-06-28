#!/usr/bin/env python3

import sys
import re
import math
import time
import hiwonder
import line_interpolation

DEFAULT_X, DEFAULT_Y, DEFAULT_Z = 0, 0, 100
OFFSET_X, OFFSET_Y, OFFSET_Z = 0, -120, 7
jetmax = hiwonder.JetMax()
jetmax.L4 = 28

speed = 80
current_pos = [DEFAULT_X, DEFAULT_Y, DEFAULT_Z]

def move_to_pos(x, y, z, t):
    end_x = -x + OFFSET_X
    end_x = end_x
    end_y = -y + OFFSET_Y
    end_z = z + OFFSET_Z
    jetmax.set_position((end_x, end_y, end_z), t)


fake_points = []


def draw(points):
    global speed, current_pos
    for i, (x, y, z) in enumerate(points):
        c_x, c_y, c_z = current_pos
        t = math.sqrt((c_x - x) ** 2 + (c_y - y) ** 2 + (c_z - z) ** 2) / speed 
        t = t * 2
        move_to_pos(x, y, z, t)
        fake_points.append((x, y))
        time.sleep(t + 0.001)
        current_pos = [x, y, z]


def get_param(cmd, param_name):
    try:
        i = cmd.index(param_name)
        return float(cmd[i + 1])
    except Exception as e:
        # print(e)
        return None


def draw_ngc(path, speed_l=80):
    global speed, current_pos
    speed = speed_l
    move_to_pos(DEFAULT_X, DEFAULT_Y, DEFAULT_Z, 1)
    time.sleep(1)
    gcodes = []
    with open(path, 'r') as f:
        gcodes = f.readlines()
    space = re.compile(' +')
    for gcode in gcodes:
        if gcode == '':
            continue
        gcode = space.sub(' ', gcode)
        gcode = gcode.strip().split(' ')
        instruct = gcode[0]
        if len(instruct) < 2:
            continue
        if instruct[0] == 'G':
            code = int(instruct[1:])
            if code == 0:
                c_x, c_y, c_z = current_pos
                x = get_param(gcode, 'X')
                y = get_param(gcode, 'Y')
                z = get_param(gcode, 'Z')
                x = c_x if x is None else x
                y = c_y if y is None else y
                z = c_z if z is None else z
                t = math.sqrt((c_x - x) ** 2 + (c_y - y) ** 2 + (c_z - z) ** 2) / speed
                move_to_pos(x, y, z, t)
                current_pos = [x, y, z]
                time.sleep(t)
            elif code == 1:
                c_x, c_y, c_z = current_pos
                x = get_param(gcode, 'X')
                y = get_param(gcode, 'Y')
                z = get_param(gcode, 'Z')
                x = c_x if x is None else x
                y = c_y if y is None else y
                z = c_z if z is None else z
                if z != c_z:
                    t = math.sqrt((c_x - x) ** 2 + (c_y - y) ** 2 + (c_z - z) ** 2) / speed
                    move_to_pos(x, y, z, t)
                    current_pos = [x, y, z]
                    time.sleep(t)
                else:
                    points = line_interpolation(c_x, c_y, x, y)
                    tmp = []
                    for p in points:
                        p.append(c_z)
                        tmp.append(p)
                    draw(tmp)

            else:
                pass
                # print("INVALID G CODE")
        elif instruct[0] == 'M':
            code = int(instruct[1:])
            if code == 0:
                pass
            elif code == 1:
                pass
            elif code == 2:
                pass
            else:
                pass
        elif instruct[0] == 'F':
            speed = int(instruct[1:])
