#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
#rosrun remote_control remote_control_joystick.py &
#rosrun jetmax_control jetmax_control_main.py &
rosrun jetmax_control_custom main.py &
rosrun opc_ros server.py

PID=$!
wait "$PID"

