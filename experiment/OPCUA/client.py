
from opcua import Client, ua, uamethod
import time
import datetime

import socket
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)

# url = "opc.tcp://192.168.56.1:4840"
DataCenter_url = "opc.tcp://192.168.197.204:4840"

client = Client(DataCenter_url)

client.connect()
print(f'Client connected to url {DataCenter_url}')
print('==========================================')

Node = client.get_objects_node()

base = client.get_node("ns=2;i=1")

# write_method = client.get_node(f'ns=2;i={2}')

read_method = client.get_node(f"ns=2;i={2}")

# result_w = base.call_method(write_method, "xyz")

# result_r = base.call_method(read_method)

count = 1000
result = list()

'''Because printing affect the speed of the program, I'll comment them out.'''
# print_data = False

for i in range(0,9):

    # send_data = (2 ** (1 + i * 2)) * "a"
    print_data = False
    while (count>0):
        req = time.time()
        # print("Request: "+ datetime.datetime.now().strftime("%H:%M:%S.%f"))
        # result_w = base.call_method(write_method, send_data)
        try:
            result_r = base.call_method(read_method, ua.Variant(i,ua.VariantType.UInt16))
        except:
            print("timeout")
        if not print_data:
            print(result_r)
            print_data = True
        # print(result_r)
        # print(result_w)
        res = time.time()
        # print("Respone: "+ datetime.datetime.now().strftime("%H:%M:%S.%f"))

        # print("RTT is: ", res-req)
        # print('==========================================')
        print(count, end=",")
        result.append(res-req)
        count-=1

    count = 1000
    print("\r\n", result)
    print("="*20)
    result.clear()

client.disconnect()