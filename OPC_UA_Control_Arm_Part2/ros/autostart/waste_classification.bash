#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
rosrun waste_classification waste_classification_main.py &

PID=$!
wait "$PID"

