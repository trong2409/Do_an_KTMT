#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
rosrun color_sorting color_sorting_main.py &

PID=$!
wait "$PID"

