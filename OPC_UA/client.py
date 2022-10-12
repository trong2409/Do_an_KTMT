from http import client
from itertools import count
from opcua import Client
import time
import datetime
import xlsxwriter

import socket
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)

# url = "opc.tcp://192.168.56.1:4840"
url = "opc.tcp://"+IPAddr+":5000" 

client = Client(url)

client.connect()
print('Client connected')
print('==========================================')

count = 200
result = {"2b":[]}

while (count>0):
    req = time.time()
    print("Request: "+ datetime.datetime.now().strftime("%H:%M:%S.%f"))
    
    DataNode = client.get_node("ns=2;i=2")
    Data = DataNode.get_value()
    # print("Temperature: ",Temperature)

    res = time.time()
    print("Respone: "+ datetime.datetime.now().strftime("%H:%M:%S.%f"))

    print("RTT is: ", res-req)
    print('==========================================')

    result['2b'].append(res-req)
    count-=1
    

workbook = xlsxwriter.Workbook('result2.xlsx')
worksheet = workbook.add_worksheet()
array = [result['2b']]
row = 0
for col, data in enumerate(array):
    worksheet.write_column(row, col, data)
workbook.close()
print('done')
