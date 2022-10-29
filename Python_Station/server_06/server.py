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
def controlRobotXYZ(parent, idRobot, posX, posY, posZ):
    data = "#X" + str(posX) + "Y" + str(posY) + "Z" + str(posZ)
    serialControl.write(data)
    return 0

@uamethod
def controlRobotServo(parent, idRobot, servo):
    global serialControl
    data = "#S" + str(servo)
    serialControl.write(data)
    return 0

@uamethod
def controlRobotPumpValve(parent, idRobot, pump, valve):
    global serialControl
    data = "#B" + str(pump) + "V" + str(valve)
    serialControl.write(data)
    return 0

@uamethod
def controlRobotAction(parent, idRobot, action):
    global serialControl
    if int(action) == 0:
        serialControl.write("#HOME")
    elif int(action) == 1:
        serialControl.write("#SCEN1")
    elif int(action) == 2:
        serialControl.write("#SCEN2")
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

    robot_folder = station_object.add_folder(addspace, "Robot")
    robot_object = robot_folder.add_object(addspace, "Robot_01")

    position_object_1  = robot_object.add_object(addspace, "Position")
    position_X_robot_1 = position_object_1.add_variable(addspace, "X", 0)
    position_Y_robot_1 = position_object_1.add_variable(addspace, "Y", 0)
    position_Z_robot_1 = position_object_1.add_variable(addspace, "Z", 0)
    position_S_robot_1 = position_object_1.add_variable(addspace, "S", 0)

    pump_robot_1  = robot_object.add_variable(addspace, "B", 0)
    valve_robot_1 = robot_object.add_variable(addspace, "V", 0)
    state_robot_1 = robot_object.add_variable(addspace, "stateRobot", "STOP")

    position_X_robot_1.set_read_only()
    position_Y_robot_1.set_read_only()
    position_Z_robot_1.set_read_only()
    position_S_robot_1.set_read_only()
    pump_robot_1.set_read_only()
    valve_robot_1.set_read_only()
    state_robot_1.set_read_only()

    robot_1_method_1 = robot_object.add_method(addspace, "robotXYZ", controlRobotXYZ,
                                                [ua.VariantType.Int64], 
                                                [ua.VariantType.Int64],
                                                [ua.VariantType.Int64],
                                                [ua.VariantType.Int64],
                                                [ua.VariantType.Int64])

    robot_1_method_2 = robot_object.add_method(addspace, "robotServo", controlRobotServo,
                                                [ua.VariantType.Int64], 
                                                [ua.VariantType.Int64],
                                                [ua.VariantType.Int64])
                                    
    robot_1_method_3 = robot_object.add_method(addspace, "robotControl", controlRobotPumpValve,
                                                [ua.VariantType.Int64], 
                                                [ua.VariantType.Int64],
                                                [ua.VariantType.Int64],
                                                [ua.VariantType.Int64])

    robot_1_method_4 = robot_object.add_method(addspace, "robotAction", controlRobotAction,
                                                [ua.VariantType.Int64], 
                                                [ua.VariantType.Int64],
                                                [ua.VariantType.Int64])

    # starting!
    server.start()
    logging.Logger.manager.loggerDict.keys()
    serialControl.start()
    serialControl.setNodesStationRobot(positionX = position_X_robot_1, 
                                    positionY = position_Y_robot_1, 
                                    positionZ = position_Z_robot_1, 
                                    angleServoS = position_S_robot_1, 
                                    pumpB = pump_robot_1, 
                                    valveV = valve_robot_1,
                                    stateRB = state_robot_1)
    
    try:
        print(server_station + " Running...")
        while True:
            pass
        # embed()
    finally:
        server.stop()
        serialControl.stop()

