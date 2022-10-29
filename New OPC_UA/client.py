from http import client
from itertools import count
import random
from opcua import Client
import time
import datetime
import xlsxwriter
import string

import socket


hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)
# url = "opc.tcp://"+IPAddr+":4840"

url = "opc.tcp://192.168.193.212:4840"

flag_isSent = 0
requestTime=0
result = list()
sizeTest = 2**1

class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """
    def __init__(self):
        self.index = 0
    def datachange_notification(self, node, val, data):
        global flag_isSent, requestTime
        result.append(time.time()-requestTime)
        flag_isSent=0
        print("Python: New data change event", node, val, self.index)
        self.index += 1

    def event_notification(self, event):
        print("Python: New event", event)  


#################################################################
#                      SETUP OPC-UA CLIENT                      #
#################################################################
client = Client(url)
client.connect()
print('Client connected to Center')
print('==========================================')

# create subcribe channel
DataClient = client.get_node("ns=2;i=2")
DataServer = client.get_node("ns=2;i=3")

handler  = SubHandler()
subcribe = client.create_subscription(1, handler)
subcribe.subscribe_data_change(DataClient)

for  i in range(0,1000):

    # strNum=''.join(random.choices(string.ascii_lowercase + string.digits, k=sizeTest))

    DataServer.set_value(random.random())
    requestTime=time.time()
    flag_isSent = 1

    while flag_isSent == 1:
        pass


print(result)

# workbook = xlsxwriter.Workbook('result1.xlsx')
# worksheet = workbook.add_worksheet()
# array = [result['2b']]
#
# row = 0
# for col, data in enumerate(array):
#     worksheet.write_column(row, col, data)
# workbook.close()
# print('done')

client.disconnect()