#!/bin/bash
sudo systemctl stop server_opc;

sleep 1;

sudo systemctl disable server_opc;

sleep 1;

sudo avrdude -C avrdude.conf -v -p atmega2560 -c wiring -P /dev/ttyACM0 -b 115200 -D -U flash:w:DRIVER_PAUL_ROBOT.ino.hex:i;

sudo systemctl enable server_opc;

sleep 1;

sudo systemctl start server_opc;
