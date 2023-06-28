#!/bin/bash

sudo kill -9 $(ps -elf|grep -v grep|grep python3|grep alphabetically|awk '{print $4}') >/dev/null 2>&1
sudo systemctl stop alphabetically.service  

sudo kill -9 $(ps -elf|grep -v grep|grep python3|grep waste_classification|awk '{print $4}') >/dev/null 2>&1
sudo systemctl stop waste_classification.service

sudo kill -9 $(ps -elf|grep -v grep|grep python3|grep object_tracking|awk '{print $4}') >/dev/null 2>&1
sudo systemctl stop object_tracking.service

sudo kill -9 $(ps -elf|grep -v grep|grep python3|grep color_sorting|awk '{print $4}') >/dev/null 2>&1
sudo systemctl stop color_sorting.service


