print("Xin chào Đồ Án Kỹ Thuật Máy Tính")
import paho.mqtt.client as mqttclient
import time
import json

BROKER_ADDRESS = "192.168.123.102"

# result of RRT
res = []
# flag check subscribing
sub_flag = 0
# dicts store send and receive time
receive_dict = []
send_dict = []

def subscribed(client, userdata, mid, granted_qos):
    global sub_flag
    print("Subscribed...")
    # update sub_flag
    sub_flag = 1

# mqtt giong nhu 1 kenh youtube vay, muon nhan thong bao video moi thi phai
# subcribe vao no, de khi co video moi thi no se ba'o ve` lien
# (qua recv_message)

def recv_message(client, userdata, message):
    global after
    global block_flag
    # data cung la index cua 2 cai dict
    data = message.payload.decode("UTF-8")
    # print("Received: ", data)
    # get time after receive the response message
    after = time.time()
    # print("after:", after)
    receive_dict.append(after)
    # update block_flag
    block_flag = 0
    # print("------------------------")

def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        # client.subscribe("#")
        client.subscribe("v1/devices/me/telemetry1")
        # client.subscribe("$SYS/broker/bytes/received")
    else:
        print("Connection is failed")

client = mqttclient.Client("nam.diep.239")
# client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)
# access token = username de dang nhap vao device.

client.on_connect = connected
# on_connect la 1 ham callback, khi ket
# noi thanh cong thi no se chui vao ham
# connect (on_connect)
client.connect(BROKER_ADDRESS, 1883, keepalive=60)  # thuc hien ket noi.
client.loop_start()

client.on_subscribe = subscribed
client.on_message = recv_message


# num of sample
loop_num = 1000

for x in range(0, 9):
    # size of message
    pack_len = 2 ** (1 + x * 2)

    for i in range(0,loop_num):
        # ensure that subscribing before send the first message
        while sub_flag == 0:
            pass
        # get time before send message
        before = time.time()
        print(i)
        # print('before:', before)
        send_dict.append(before)
        # prepare data before send
        data = "0" * pack_len
        client.publish('v1/devices/me/telemetry0', data)
        # ensure that receiving the response message before send the next message
        block_flag = 1
        while block_flag == 1:
            pass
        # dung index va block_flag thi ko can sleep nua
        # time.sleep(1)

    # calculate the RRT
    for id in range(loop_num):
        res.append(receive_dict[id] - send_dict[id])

    print("res: ", res)
    print("=" * 20)
    res.clear()
    receive_dict.clear()
    send_dict.clear()


