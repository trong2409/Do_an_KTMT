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
def controlMotor(parent, direct):
    global currentMotor, currentStateMotor, serialControl, sensor_value_1, sensor_value_2
    try:
        currentMotor = int(direct)
        data = "#MT;0;" + str(direct) + ";-1;"
        serialControl.write(data)
    finally:
        sensor_value_1.set_value(False)
        sensor_value_2.set_value(False)

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
            set_led(status=self._status, node=node, val=val)

    def event_notification(self, event):
        print("Python: New event", event)       
    
class FakePosition(Thread):
    def __init__(self, position):
        Thread.__init__(self)
        self._stopev = False
        self._position = position
        self._max = 2000
        self._min = 0
    
    def stop(self):
        self._stopev = True

    def run(self):
        global currentPosition, currentMotor
        while not self._stopev:
            if currentMotor == 0:
                pass
            if currentMotor == 1:
                currentPosition += 0.1
            if currentMotor == 2:
                currentPosition -= 0.1
            if currentPosition > self._max:
                currentPosition = self._max
            if currentPosition < self._min:
                currentPosition = self._min
            self._position.set_value(currentPosition)
            time.sleep(0.5)

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
    
    currentMotor = 0
    currentStateMotor = "STOP"
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
    
    sensor_value_1.set_read_only()
    sensor_value_2.set_read_only()

    motor_folder = station_object.add_folder(addspace, "Motor")
    motor_object = motor_folder.add_object(addspace, "Motor_01")
    control_method = motor_object.add_method(addspace, "control", controlMotor, [ua.VariantType.Int64], [ua.VariantType.Int64])
    motor_position = motor_object.add_variable(addspace, "position", 0.0)
    motor_state = motor_object.add_variable(addspace, "state", "STOP")
    motor_speed = motor_object.add_variable(addspace, "speed", 100)
    
    motor_position.set_read_only()
    motor_state.set_read_only()
    motor_speed.set_writable()

    # starting!
    server.start()
    logging.Logger.manager.loggerDict.keys()
    serialControl.start()
    fake = FakePosition(motor_position)
    serialControl.setNodes(sensor_value_1, sensor_value_2, motor_state, status_station)
    fake.start()

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
        fake.stop()
        server.stop()
        serialControl.stop()

