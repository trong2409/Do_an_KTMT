from cryptography.x509 import AccessDescription

print("Xin chào Mosquitto")
import paho.mqtt.client as mqttclient
import socket
import time
import json
import uuid
import datetime

BROKER_ADDRESS = socket.gethostbyname(socket.gethostname())
'''
dia chi host trang web. co the lay source code cua 
thingboard roi tai len server tu tao, luc do 
minh se xai dia chi khac
'''
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "j1LspaO6a6TlFbHV8Tn1"

temp = 30
humi = 50
light_intensity = 100
counter = 0
oldData = ""
led1 = False
pump1 = False


def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


# mqtt giong nhu 1 kenh youtube vay, muon nhan thong bao video moi thi phai
# subcribe vao no, de khi co video moi thi no se ba'o ve` lien
# (qua recv_message)

def recv_message(client, userdata, message):
    # data = message.payload.decode("utf-8")
    ack = "o"*42
    client.publish("v1/devices/me/telemetry1", ack)
    '''Because printing affect the speed of the program, I'll comment them out.'''
    # print("Received: ", message.payload.decode("UTF-8"))
    # print("Topic: ", message.topic)
    # except:
    #     print("problemmm")


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        # client.subscribe("#")
        client.subscribe("v1/devices/me/telemetry0")

        # client.subscribe("$SYS/broker/bytes/received")
    else:
        print("Connection is failed")

client = mqttclient.Client("cat.tran03")
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

try:
    while True:
        pass
finally:
    client.loop_stop()

