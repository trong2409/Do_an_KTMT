#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
roslaunch /home/hiwonder/ros/autostart/rosbridge_websocket.launch &

PID=$!
wait "$PID"

