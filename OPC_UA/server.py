from opcua import  Server
import datetime
from random import randint
import time


import socket
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)


server= Server()
# url = "opc.tcp://"+IPAddr+":4840"
url = "opc.tcp://192.168.123.212:4840"
server.set_endpoint(url)

name = "OPCUA_SIMUALTION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace,"Parameters")

Data = Param.add_variable(addspace,"Data",'')
# Press = Param.add_variable(addspace,"Pressure",0)
# Time = Param.add_variable(addspace,"Time",0)

Data.set_writable()
# Press.set_writable()
# Time.set_writable()

server.start()
print("Server started at {}".format(url))

file = open('input.txt','r')
text = file.read()

while True:
    # Pressure = randint(200,999)
    # TIME = datetime.datetime.now()
    # print(Temperature)
    Data.set_value(text)
    # Press.set_value(Pressure)
    # Time.set_value(TIME)

    time.sleep(2)

