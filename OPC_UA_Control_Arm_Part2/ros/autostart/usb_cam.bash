#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
roslaunch /home/hiwonder/ros/autostart/usb_cam.launch &

PID=$!
wait "$PID"

