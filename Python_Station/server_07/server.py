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
def controlMotor(parent, action):
    global serialControl, currentStation, current_station
    if int(action) == 0:
        currentStation = 0
        serialControl.write("#HOME")
    elif int(action) == 1:
        currentStation += 1
        serialControl.write("#NEXT")
    elif int(action) == 2:
        currentStation -= 1
        serialControl.write("#BACK")
    elif int(action) == 3:
        currentStation = 6
        serialControl.write("#LAST")
    current_station.set_value(currentStation)
    return 0

class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

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

if __name__ == "__main__":

    #################################################################
    #                      DEFINITION                               #
    #################################################################

    uri = "https://becamex.com.vn/paul/opcua"
    
    currentMotor = 0
    currentStateMotor = "STOP"
    serialControl = SerialCommunication("/dev/ttyACM0", baudrate=115200)
    currentPosition = 0
    currentStation = 0
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
    current_station = station_object.add_variable(addspace, "station", 0)

    version_station.set_read_only()
    id_station.set_read_only()
    status_station.set_writable()
    mode_station.set_writable()

    sensor_folder = station_object.add_folder(addspace, "Sensor")
    sensor_object_1 = sensor_folder.add_object(addspace, "Sensor_01")
    sensor_value_1 = sensor_object_1.add_variable(addspace, "value", False)
    
    sensor_value_1.set_read_only()

    motor_folder = station_object.add_folder(addspace, "Motor")

    motor_object_1 = motor_folder.add_object(addspace, "Motor_01")
    control_method_1 = motor_object_1.add_method(addspace, "control", controlMotor, [ua.VariantType.Int64], [ua.VariantType.Int64])
    motor_position_1 = motor_object_1.add_variable(addspace, "position", 0.0)
    motor_state_1 = motor_object_1.add_variable(addspace, "state", "STOP")
    motor_speed_1 = motor_object_1.add_variable(addspace, "speed", 100)
    
    motor_position_1.set_read_only()
    motor_state_1.set_read_only()
    motor_speed_1.set_writable()

    # starting!
    server.start()
    logging.Logger.manager.loggerDict.keys()
    serialControl.start()
    serialControl.setNodesStation07(sensor = sensor_value_1, motorState = motor_state_1)
    
    try:
        print(server_station + " Running...")
        while True:
            pass
        # embed()
    finally:
        server.stop()
        serialControl.stop()

