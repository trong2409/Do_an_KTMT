from opcua import  Server
from opcua import Client
import random
import time

import socket
hostname=socket.gethostname()
# IPAddr = "192.168.137.1"
IPAddr=socket.gethostbyname(hostname)
url = "opc.tcp://"+IPAddr+":4840"


class SubHandler(object):
    def __init__(self,M,R,L,F):
        self.M = M
        self.R = R
        self.L = L
        self.F = F
        
    def datachange_notification(self, node, val, data):
        nameServo = node.get_browse_name().to_string()[2]
        if nameServo=='M':
            self.M.set_value(val)
        if nameServo=='R':
            self.R.set_value(val)
        if nameServo=='L':
            self.L.set_value(val)
        if nameServo=='F':
            self.F.set_value(val)
    def event_notification(self, event):
        print("Python: New event", event)
#################################################################
#                      SETUP OPC-UA CLIENT                      #
#################################################################
ServerUrl = "opc.tcp://"+IPAddr+":4841"
client = Client(ServerUrl)
client.connect()
print('Sub_client connected to sub_server')
print('==========================================')

M = client.get_node("ns=2;i=2")
R = client.get_node("ns=2;i=3")
L = client.get_node("ns=2;i=4")
F = client.get_node("ns=2;i=5")

#################################################################
#                      SETUP OPC-UA SERVER                      #
#################################################################
server= Server()
server.set_endpoint(url)
name = "OPCUA_SUB_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
station = node.add_object(addspace,"Station")

MidServo = station.add_variable(addspace,"M",90)
RightServo = station.add_variable(addspace,"R",90)
LeftServo = station.add_variable(addspace,"L",90)
FoldServo = station.add_variable(addspace,"F",90)

MidServo.set_writable()
RightServo.set_writable()
LeftServo.set_writable()
FoldServo.set_writable()

server.start()
print("Sub_server started at {}".format(url))

handler  = SubHandler(M,R,L,F)
subcribe = server.create_subscription(1, handler)
subcribe.subscribe_data_change(MidServo)
subcribe.subscribe_data_change(RightServo)
subcribe.subscribe_data_change(LeftServo)
subcribe.subscribe_data_change(FoldServo)