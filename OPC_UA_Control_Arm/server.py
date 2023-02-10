from opcua import Server
import serial
import time
import socket
hostname=socket.gethostname()
# IPAddr = "192.168.137.1"
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
# Yolo bit link: https://app.ohstem.vn/#!/share/yolobit/2IFgJjpmNrN8mFni18MfmenU2vG
try:
    ser = serial.Serial(
        port='COM5',
        baudrate=115200,
        parity='N',
        stopbits=1,
        bytesize=8
    )
except:
    print("Something went wrong")
    ser = None


# Handler when value of Nodes is changed
class SubHandler(object):
    def __init__(self,ser, preM, preR, preL, preF):
        self.ser = ser
        self.cmdList = list()

        
    def datachange_notification(self, node, val, data):
        print(node,val)
        nameServo = node.get_browse_name().to_string()[2]
        value = int(val)
        self.cmdList.append([nameServo,value])
        

    def event_notification(self, event):
        print("Python: New event", event)  
        
        
def sendUartCommand(ser: serial.Serial, SubHandler: SubHandler):
    if len(SubHandler.cmdList) > 0:
        tempItem = SubHandler.cmdList.pop()
        nameServo = tempItem[0]
        val = tempItem[1]
        if ser is not None:
            ser.write((f"{nameServo}:"+str(val) + "#").encode())
        print((f"{nameServo}:"+str(val) + "#"))
        


#################################################################
#                      SETUP OPC-UA SERVER                      #
#################################################################
server= Server()
server.set_endpoint(url)
name = "OPCUA_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
station = node.add_folder(addspace,"Station")

MidServo = station.add_variable(addspace,"M",90)
RightServo = station.add_variable(addspace,"R",90)
LeftServo = station.add_variable(addspace,"L",90)
FoldServo = station.add_variable(addspace,"F",90)

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

while True:
    sendUartCommand(ser, handler)
    time.sleep(0.01)