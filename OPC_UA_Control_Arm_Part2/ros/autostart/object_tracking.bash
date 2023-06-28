#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
rosrun object_tracking object_tracking_main.py &

PID=$!
wait "$PID"

