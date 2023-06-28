#!/bin/bash
source /opt/ros/melodic/setup.bash
source /home/hiwonder/ros/devel/setup.bash

export ROS_HOME=/home/hiwonder/.ros
rosrun palletizing palletizing_main.py &

PID=$!
wait "$PID"

