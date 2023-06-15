from opcua import  Server
import datetime
from random import randint
import time

import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

server = Server()
# url = "opc.tcp://"+IPAddr+":4840"
IP = "10.230.219.253"
url = f"opc.tcp://{IP}:4840"
server.set_endpoint(url)

name = "OPCUA_SIMUALTION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace,"Parameters")

Data = list()

for i in range(0,9):
    Data.append(Param.add_variable(addspace, f'data_{i}', "a"*(2 ** (1 * i * 2))))
    Data[i].set_writable()

server.start()
print("Server started at {}".format(url))

try:
    while True:
        pass
finally:
    server.stop()

