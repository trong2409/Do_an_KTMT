from opcua import  Server
import serial

import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
url = "opc.tcp://"+IPAddr+":4841"

# Range of each Servo
MIN_M = 0
MAX_M = 180

MIN_R = 100
MAX_R = 180

MIN_L = 0
MAX_L = 100

MIN_F = 80
MAX_F = 180

# Init serial
ser = serial.Serial(
    port='COM8',
    baudrate=115200,
    parity='N',
    stopbits=1,
    bytesize=8
)

# Handler when value of Nodes is changed
class SubHandler(object):
    def __init__(self,ser, preM, preR, preL, preF):
        self.ser = ser
        self.preM = preM
        self.preR = preR
        self.preL = preL
        self.preF = preF

        
    def datachange_notification(self, node, val, data):
        print(node,val)
        nameServo = node.get_browse_name().to_string()[2]
        value = int(val)
        if nameServo=='M':
            if value > self.preM and value < MAX_M:
                self.ser.write(("M:+:"+str(val) + "#").encode())
                print("M:+:"+str(val) + "#")
            if value < self.preM and value > MIN_M: 
                self.ser.write(("M:-:"+str(val) + "#").encode())
                print("M:-:"+str(val) + "#")
            self.preM = value
        
        if nameServo=='R':
            if value > self.preR and value < MAX_R:
                self.ser.write(("R:+:"+str(val) + "#").encode())
                print("R:+:"+str(val) + "#")
            if value < self.preR and value > MIN_R: 
                self.ser.write(("R:-:"+str(val) + "#").encode())
                print("R:-:"+str(val) + "#")

            self.preR = value
        
        if nameServo=='L':
            if value > self.preL and value < MAX_L:
                self.ser.write(("L:+:"+str(val) + "#").encode())
                print("L:+:"+str(val) + "#")
            if value < self.preL and value > MIN_L: 
                self.ser.write(("L:-:"+str(val) + "#").encode())
                print("L:-:"+str(val) + "#")
            self.preL = value

        if nameServo=='F':
            if value > self.preF and value < MAX_F:
                self.ser.write(("F:+:"+str(val) + "#").encode())
                print("F:+:"+str(val) + "#")
            if value < self.preF and value > MIN_F: 
                self.ser.write(("F:-:"+str(val) + "#").encode())
                print("F:-:"+str(val) + "#")
            self.preF = value

    def event_notification(self, event):
        print("Python: New event", event)  

#################################################################
#                      SETUP OPC-UA SERVER                      #
#################################################################
server= Server()
server.set_endpoint(url)
name = "OPCUA_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
station = node.add_object(addspace,"Station")

MidServo = station.add_variable(addspace,"M",0)
RightServo = station.add_variable(addspace,"R",0)
LeftServo = station.add_variable(addspace,"L",0)
FoldServo = station.add_variable(addspace,"F",0)

MidServo.set_writable()
RightServo.set_writable()
LeftServo.set_writable()
FoldServo.set_writable()

server.start()
print("Center started at {}".format(url))

# Store previous value of Nodes to compare with current Nodes
preM = MidServo.get_value()
preR = RightServo.get_value()
preL = LeftServo.get_value()
preF = FoldServo.get_value()

# Create subcribe channel
handler  = SubHandler(ser,preM, preR, preL, preF)
subcribe = server.create_subscription(1, handler)
subcribe.subscribe_data_change(MidServo)
subcribe.subscribe_data_change(RightServo)
subcribe.subscribe_data_change(LeftServo)
subcribe.subscribe_data_change(FoldServo)