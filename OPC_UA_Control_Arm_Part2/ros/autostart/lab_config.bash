#!/bin/bash
source /opt/ros/melodic/setup.bash
source ~/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
roslaunch lab_config lab_config_manager.launch &

PID=$!
wait "$PID"

