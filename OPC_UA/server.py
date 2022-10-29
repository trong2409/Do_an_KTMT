from opcua import  Server
import datetime
from random import randint
import time

import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

server= Server()
# url = "opc.tcp://"+IPAddr+":4840"
url = "opc.tcp://"+IPAddr+":4840"
server.set_endpoint(url)

name = "OPCUA_SIMUALTION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Data = list()

file_array = [
    './input/input_1_2b.txt',
    "./input/input_2_8b.txt",
    "./input/input_3_32b.txt",
    "./input/input_4_128b.txt",
    "./input/input_5_512b.txt",
    "./input/input_6_2Kb.txt",
    "./input/input_7_8Kb.txt",
    "./input/input_8_32Kb.txt",
    "./input/input_8_128Kb.txt",
]

Param = node.add_object(addspace,"Parameters")

for i in range(0, 9):
    file = open(file_array[i], 'r')
    text = file.read()
    Data.append(Param.add_variable(addspace,f'data_{i}',text))
    Data[i].set_writable()
    file.close()

# Press = Param.add_variable(addspace,"Pressure",0)
# Time = Param.add_variable(addspace,"Time",0)


# Press.set_writable()
# Time.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    pass

