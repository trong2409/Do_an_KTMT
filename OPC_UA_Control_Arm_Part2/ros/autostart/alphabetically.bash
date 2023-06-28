#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
rosrun alphabetically alphabetically_main.py &

PID=$!
wait "$PID"

