from opcua import  Server
import datetime
from random import randint
import time

import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

server= Server()
# url = "opc.tcp://"+IPAddr+":4840"
url = "opc.tcp://192.168.0.101:4840"
server.set_endpoint(url)

name = "OPCUA_SIMUALTION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace,"Parameters")

Data = Param.add_variable(addspace, f'data', "init_data")

Data.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    pass

