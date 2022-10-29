from http import client
from itertools import count
from opcua import Client
from random import random
import time
import datetime
import xlsxwriter

import socket
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)
url = "opc.tcp://"+IPAddr+":4840"
flag_isRecieved = 0

class SubHandler(object):
    
    def datachange_notification(self, node, val, data):  
        global flag_isRecieved
        flag_isRecieved=1
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)  
#################################################################
#                      SETUP OPC-UA CLIENT                      #
#################################################################
client = Client(url)
client.connect()
print('Server connected to Center')
print('==========================================')

# create subcribe channel
DataClient = client.get_node("ns=2;i=2")
DataServer = client.get_node("ns=2;i=3")
handler  = SubHandler()
subcribe = client.create_subscription(1, handler)
subcribe.subscribe_data_change(DataServer)


while (True):
    if flag_isRecieved==1:
        DataClient.set_value(DataServer.get_value())
        flag_isRecieved=0
