import socket
import cv2
import numpy as np
import serial
from opcua import Client

hostname = socket.gethostname()
# IPAddr = "192.168.137.1"
IPAddr = socket.gethostbyname(hostname)
url = "opc.tcp://" + IPAddr + ":4841"

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
    def __init__(self, ser):
        self.ser = ser
        self.cmdList = list()

    def datachange_notification(self, node, val, data):
        # print(node, val)
        # nameServo = node.get_browse_name().to_string()[2]
        # value = int(val)
        self.cmdList.append(val)

    def event_notification(self, event):
        print("Python: New event", event)


def sendUartCommand(ser: serial.Serial, SubHandler: SubHandler):
    if len(SubHandler.cmdList) > 0:
        tempItem = SubHandler.cmdList.pop()
        nameServo = tempItem[0]
        val = tempItem[1]
        if ser is not None:
            ser.write((f"{nameServo}:" + str(val) + "#").encode())
        print((f"{nameServo}:" + str(val) + "#"))

def showVideo(handler: SubHandler):
    pass



#################################################################
#                      SETUP OPC-UA SERVER                      #
#################################################################
# url = "opc.tcp://192.168.50.121:4841"
url = "opc.tcp://10.0.136.34:8888"
client = Client(url)
client.connect()

videoNode = client.get_node("ns=2;i=17")


# Create subcribe channel
handler = SubHandler(ser)
subcribe = client.create_subscription(1, handler)
subcribe.subscribe_data_change(videoNode)


while True:
    if len(handler.cmdList) > 0:
        data = handler.cmdList.pop()
        print("hi")
        # print(data)
        # a = cv2.imdecode(data,1)
        image = np.ndarray(shape=(len(data), 1), dtype=np.uint8, buffer=data)
        decimg = cv2.imdecode(image, cv2.IMREAD_COLOR)
        cv2.imshow("test", decimg)
        key = cv2.waitKey(1)
        if key &0x00FF == ord('q'):
            break

# encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
# result, encimg = cv2.imencode('.jpg', img, encode_param)

for i in range(1, 13):
    print(f'2^{i} mod 13 = {2**i % 13}')
