from http import client
from itertools import count
from random import randint
from opcua import Client
import time
import datetime
import xlsxwriter

import socket


hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)
url = "opc.tcp://"+IPAddr+":4840"

flag_isSent = 0
requestTime=0
result = {"2b":[]}
sizeTest = 2**2

class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        global flag_isSent
        if flag_isSent==1:
            result['2b'].append(time.time()-requestTime)
        flag_isSent=0
        print("Python: New data change event", node, val)
        

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

    strNum=''
    if i%2==0:
        strNum=str(randint(1,9))+'0'*(sizeTest-1)
    else:
        strNum='0'*(sizeTest-1)+str(randint(1,9))

    if flag_isSent==0 :
        DataServer.set_value(strNum)
        flag_isSent=1
        requestTime=time.time()
    while flag_isSent==1:
        pass

workbook = xlsxwriter.Workbook('result1.xlsx')
worksheet = workbook.add_worksheet()
array = [result['2b']]
row = 0
for col, data in enumerate(array):
    worksheet.write_column(row, col, data)
workbook.close()
print('done')

client.disconnect()