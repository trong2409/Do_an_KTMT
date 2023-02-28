from cryptography.x509 import AccessDescription

print("Xin chào Mosquitto")
import paho.mqtt.client as mqttclient
import socket

BROKER_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 1883

def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")

def recv_message(client, userdata, message):
    ack = "o"*64
    client.publish("v1/devices/me/telemetry1", ack)
    '''Because printing affect the speed of the program, I'll comment them out.'''
    # print("Received: ", message.payload.decode("UTF-8"))


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("v1/devices/me/telemetry0")
    else:
        print("Connection is failed")

client = mqttclient.Client("cat.tran03")

client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883, keepalive=60) 
client.loop_start()

client.on_subscribe = subscribed
client.on_message = recv_message

try:
    while True:
        pass
finally:
    client.loop_stop()

