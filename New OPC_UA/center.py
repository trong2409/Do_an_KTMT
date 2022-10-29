from opcua import  Server
import datetime
from random import randint, random
import time


import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
url = "opc.tcp://"+IPAddr+":4840"

class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)  

#################################################################
#                      SETUP OPC-UA SERVER                      #
#################################################################


server= Server()
server.set_endpoint(url)
name = "OPCUA_SIMUALTION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
station = node.add_object(addspace,"Station")
DataClient = station.add_variable(addspace,"DataClient",'')
DataServer = station.add_variable(addspace,"DataServer",'')
DataClient.set_writable()
DataServer.set_writable()

server.start()
print("Center started at {}".format(url))
# create subcribe channel
handler  = SubHandler()
subcribe = server.create_subscription(1, handler)
subcribe.subscribe_data_change(DataClient)
subcribe.subscribe_data_change(DataServer)

# while True:
#     value1 = random()
#     value2 = random()
#     DataClient.set_value(value1)
#     DataServer.set_value(value2)
#     print('=======================')
#     time.sleep(10)

