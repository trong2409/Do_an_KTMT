#!/usr/bin/env python3
print("----OPC UA Server----")

import uuid
import copy
import logging
import time
import netifaces
import json
import sys
import os.path
import pathlib
from math import sin
from datetime import datetime
from threading import Thread
from opcua.ua import NodeId, NodeIdType
from opcua import ua, uamethod, Server
from serialThread import SerialCommunication

#################################################################
#                      SUB-FUNCTIONS                            #
#################################################################
config_file = str(pathlib.Path().home()) + "/server_opc/.conf"

sys.path.insert(0, "..")
try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        myvars = globals()
        myvars.update(locals())
        shell = code.InteractiveConsole(myvars)
        shell.interact()

@uamethod
def controlMotor(parent, idMotor, direct, distance):
    global serialControl
    global sensor_value_1, sensor_value_2, sensor_value_3, sensor_value_4, sensor_value_5, sensor_value_6, sensor_value_7
    try:
        data = "#MT;" + str(idMotor) + ";" + str(direct) + ";" + str(distance) + ";"
        serialControl.write(data)
    finally:
        if str(idMotor) == "0":
            sensor_value_1.set_value(False)
            sensor_value_2.set_value(False)
            sensor_value_3.set_value(False)
        elif str(idMotor) == "2":
            sensor_value_4.set_value(False)
        elif str(idMotor) == "3":
            sensor_value_5.set_value(False)
        elif str(idMotor) == "4":
            sensor_value_6.set_value(False)
        elif str(idMotor) == "5":
            sensor_value_7.set_value(False)

    return 0

@uamethod
def controlServo(parent, idServo, degree):
    global serialControl, servo_degree_1, servo_degree_2
    if str(idServo) ==  "0":
        servo_degree_1.set_value(degree)
    if str(idServo) ==  "1":
        servo_degree_2.set_value(degree)
    try:
        data = "#SV;" + str(idServo) + ";" + str(degree) + ";"
        serialControl.write(data)
    finally:
        pass
    return 0

@uamethod
def controlHome(parent, idMotor):
    global serialControl
    try:
        data = "#HOME;" + str(idMotor) + ";"
        serialControl.write(data)
    finally:
        pass
    return 0

@uamethod
def controlLED(parent, color):
    global serialControl
    try:
        data = "#LED;0;" + str(color) + ";"
        serialControl.write(data)
    finally:
        pass

    return 0

class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def __init__(self, status=None):
        self._status = status

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

        if self._status is not None:
            if node == self._status:
                set_led(status=self._status, node=node, val=val)

    def event_notification(self, event):
        print("Python: New event", event)       
    
def detect_ethernet_ip():
    ifaces = netifaces.interfaces()
    if 'enp2s0' in ifaces:
        if len(netifaces.ifaddresses('enp2s0')) > 1:
            return netifaces.ifaddresses('enp2s0')[netifaces.AF_INET][0]['addr']
    if 'eth0' in ifaces:
        if len(netifaces.ifaddresses('eth0')) > 1:
            return netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    if 'wlan0' in ifaces:
        if len(netifaces.ifaddresses('wlan0')) > 1:
            return netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']

def generate_default_config():
    f = open(config_file,"x")
    data = {}
    data = {
        'ip': None, 
        'port':'53535',
        'station': None,
        'id': None,
        'version':'0.0.1'
        }
    f.write(json.dumps(data, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()
    print("Create file configuration.")

def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial

def set_led(status, node, val):
    global serialControl
    if node == status:
        data = ""
        if val == "RUN":
           data = "#LED;0;1;" 
        elif val == "IDLE":
            data = "#LED;0;3;"
        elif val == "STOP":
            data = "#LED;0;3;"
        elif val == "MAN":
            data = "#LED;0;2;"
        if not data == "":
            try:
                serialControl.write(data)  
            finally:
                pass

if __name__ == "__main__":

    #################################################################
    #                      DEFINITION                               #
    #################################################################

    uri = "https://becamex.com.vn/paul/opcua"
    
    serialControl = SerialCommunication("/dev/ttyACM0", baudrate=115200)
    currentPosition = 0
    #################################################################
    #                           FIRST INIT                          #
    #################################################################

    if not os.path.isfile(config_file):
        generate_default_config()

    with open(config_file) as file_json:
        data = json.load(file_json)

    if data['ip'] is None:
        data['ip'] = detect_ethernet_ip()
    if data['id'] is None:
        data['id'] = getserial()
    if data['station'] is None:
        data['station'] = '00'
    station = data['station']

    with open(config_file, 'w') as outfile:
        json.dump(data, outfile)

    url = "opc.tcp://" + str(data['ip']) + ":" + str(data['port'])
    server_station = "[PAUL_SERVER]:STATION_" + station

    logging.basicConfig(level=logging.WARN)

    #################################################################
    #                      SETUP OPC-UA SERVER                      #
    #################################################################

    server = Server()
    server.set_endpoint(url)
    server.set_server_name(server_station)
    # set all possible endpoint policies for clients to connect through
    server.set_security_policy([
                ua.SecurityPolicyType.NoSecurity,
                ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
                ua.SecurityPolicyType.Basic256Sha256_Sign])

    # setup our own namespace
    addspace = server.register_namespace(uri)
    node = server.get_objects_node()

    # create a new node type we can instantiate in our address space
    station_object = node.add_object(addspace, "Station_" + str(station))

    version_station = station_object.add_variable(addspace, "version", data['version'])
    id_station = station_object.add_property(addspace, "device_id", data['id'])
    status_station = station_object.add_variable(addspace, "state", "IDLE")
    mode_station = station_object.add_variable(addspace, "mode", "MANNUAL")
    home_motor = station_object.add_method(addspace, "home", controlHome, [ua.VariantType.Int64], [ua.VariantType.Int64])
    led_method = station_object.add_method(addspace, "led", controlLED, [ua.VariantType.Int64], [ua.VariantType.Int64])

    version_station.set_read_only()
    id_station.set_read_only()
    status_station.set_writable()
    mode_station.set_writable()

    sensor_folder = station_object.add_folder(addspace, "Sensor")
    sensor_object_1 = sensor_folder.add_object(addspace, "Sensor_01")
    sensor_value_1 = sensor_object_1.add_variable(addspace, "value", False)
    sensor_object_2 = sensor_folder.add_object(addspace, "Sensor_02")
    sensor_value_2 = sensor_object_2.add_variable(addspace, "value", False)
    sensor_object_3 = sensor_folder.add_object(addspace, "Sensor_03")
    sensor_value_3 = sensor_object_3.add_variable(addspace, "value", False)
    sensor_object_4 = sensor_folder.add_object(addspace, "Sensor_04")
    sensor_value_4 = sensor_object_4.add_variable(addspace, "value", False)
    sensor_object_5 = sensor_folder.add_object(addspace, "Sensor_05")
    sensor_value_5 = sensor_object_5.add_variable(addspace, "value", False)
    sensor_object_6 = sensor_folder.add_object(addspace, "Sensor_06")
    sensor_value_6 = sensor_object_6.add_variable(addspace, "value", False)
    sensor_object_7 = sensor_folder.add_object(addspace, "Sensor_07")
    sensor_value_7 = sensor_object_7.add_variable(addspace, "value", False)
    
    sensor_value_1.set_read_only()
    sensor_value_2.set_read_only()
    sensor_value_3.set_read_only()
    sensor_value_4.set_read_only()
    sensor_value_5.set_read_only()
    sensor_value_6.set_read_only()
    sensor_value_7.set_read_only()

    motor_folder = station_object.add_folder(addspace, "Motor")

    motor_object_1 = motor_folder.add_object(addspace, "Motor_01")
    control_method_1 = motor_object_1.add_method(addspace, "control", controlMotor, [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64])
    motor_position_1 = motor_object_1.add_variable(addspace, "position", 0.0)
    motor_state_1 = motor_object_1.add_variable(addspace, "state", "STOP")
    motor_speed_1 = motor_object_1.add_variable(addspace, "speed", 100)

    motor_object_2 = motor_folder.add_object(addspace, "Motor_02")
    control_method_2 = motor_object_2.add_method(addspace, "control", controlMotor, [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64])
    motor_position_2 = motor_object_2.add_variable(addspace, "position", 0.0)
    motor_state_2 = motor_object_2.add_variable(addspace, "state", "STOP")
    motor_speed_2 = motor_object_2.add_variable(addspace, "speed", 100)
    
    motor_object_3 = motor_folder.add_object(addspace, "Motor_03")
    control_method_3 = motor_object_3.add_method(addspace, "control", controlMotor, [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64])
    motor_position_3 = motor_object_3.add_variable(addspace, "position", 0.0)
    motor_state_3 = motor_object_3.add_variable(addspace, "state", "STOP")
    motor_speed_3 = motor_object_3.add_variable(addspace, "speed", 100)
    
    motor_object_4 = motor_folder.add_object(addspace, "Motor_04")
    control_method_4 = motor_object_4.add_method(addspace, "control", controlMotor, [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64])
    motor_position_4 = motor_object_4.add_variable(addspace, "position", 0.0)
    motor_state_4 = motor_object_4.add_variable(addspace, "state", "STOP")
    motor_speed_4 = motor_object_4.add_variable(addspace, "speed", 100)
    
    motor_object_5 = motor_folder.add_object(addspace, "Motor_05")
    control_method_5 = motor_object_5.add_method(addspace, "control", controlMotor, [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64])
    motor_position_5 = motor_object_5.add_variable(addspace, "position", 0.0)
    motor_state_5 = motor_object_5.add_variable(addspace, "state", "STOP")
    motor_speed_5 = motor_object_5.add_variable(addspace, "speed", 100)
    
    motor_position_1.set_read_only()
    motor_state_1.set_read_only()
    motor_speed_1.set_writable()

    motor_position_2.set_read_only()
    motor_state_2.set_read_only()
    motor_speed_2.set_writable()

    motor_position_3.set_read_only()
    motor_state_3.set_read_only()
    motor_speed_3.set_writable()

    motor_position_4.set_read_only()
    motor_state_4.set_read_only()
    motor_speed_4.set_writable()

    motor_position_5.set_read_only()
    motor_state_5.set_read_only()
    motor_speed_5.set_writable()

    servo_folder = station_object.add_folder(addspace, "Servo")

    servo_object_1 = servo_folder.add_object(addspace, "Servo_01")
    servo_control_1 = servo_object_1.add_method(addspace, "roll", controlServo, [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64])
    servo_degree_1 = servo_object_1.add_variable(addspace, "degree", 80)

    servo_object_2 = servo_folder.add_object(addspace, "Servo_02")
    servo_control_2 = servo_object_2.add_method(addspace, "roll", controlServo, [ua.VariantType.Int64], [ua.VariantType.Int64], [ua.VariantType.Int64])
    servo_degree_2 = servo_object_2.add_variable(addspace, "degree", 90)

    servo_degree_1.set_read_only()
    servo_degree_2.set_read_only()

    # starting!
    server.start()
    logging.Logger.manager.loggerDict.keys()
    serialControl.start()
    serialControl.setNodesStation05(switchJourney1=sensor_value_1,
                                    switchJourney2=sensor_value_2, 
                                    switchJourney3=sensor_value_3, 
                                    switchJourney4=sensor_value_4, 
                                    switchJourney5=sensor_value_5, 
                                    switchJourney6=sensor_value_6,
                                    switchJourney7=sensor_value_7,
                                    motor1State=motor_state_1,
                                    motor2State=motor_state_2,
                                    motor3State=motor_state_3,
                                    motor4State=motor_state_4,
                                    motor5State=motor_state_5,
                                    servo1degree=servo_degree_1,
                                    servo2degree=servo_degree_2,
                                    stationState=status_station)

    # create subcribe channel
    handler  = SubHandler(status=status_station)
    subcribe = server.create_subscription(1, handler)
    subcribe.subscribe_data_change(status_station)

    try:
        print(server_station + " Running...")
        while True:
            pass
        # embed()
    finally:
        server.stop()
        serialControl.stop()

