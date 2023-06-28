#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
roslaunch camera_cal camera_cal.launch &

PID=$!
wait "$PID"

