#!/usr/bin/env python3

import logging
import netifaces as ni
import asyncio
import traceback
import math
import threading

import rospy
from std_srvs.srv import Empty, Trigger
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from std_msgs.msg import Bool, UInt16
from opc_ros.msg import SetServo, JetMax, SetJetMax
from opc_ros.srv import SetTarget, SetTargetResponse, SetTargetRequest
from opc_ros.srv import SetTarget_object, SetTarget_objectResponse, SetTarget_objectRequest

from opcua import ua, uamethod, Server

_logger = logging.getLogger(__name__)

# IPAddr = ni.ifaddresses('ap0')[ni.AF_INET][0]['addr']
IPAddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']


MIN_MIDSERVO = 0
MAX_MIDSERVO = 1000

MIN_LEFTSERVO = 0
MAX_LEFTSERVO = 1000

MIN_RIGHTSERVO = 0
MAX_RIGHTSERVO = 1000

MIN_ROTATOR = 0
MAX_ROTATOR = 180

MIN_GRIPPER = 0
MAX_GRIPPER = 180

DURATION = 0.2

midServo = 90
leftServo = 90
rightServo = 90
rotatorServo = 90
gripperServo = 90
suckcup = False
speed = 5
cordinateSpeed = math.floor(speed / 2)
x = 0
y = 0
z = 0

oldData = None

JetMaxControlList = list()
#  0 -> mid
#  1 -> left
#  2 -> right
#  3 -> rotator
#  4 -> gripper
#  5 -> sucker
#  6 -> position command
#  7 -> relative position command

AI_SERVICE_NAME = ["palletizing",
                    "waste_classification",
                    "object_tracking", 
                    "color_sorting"
                    ]
AI_COLOR = ["red", "green", "blue"]

@uamethod
def moveServo(parent, servo_name: str, angle_increase: bool):
    global midServo, leftServo, rightServo, rotatorServo, speed, JetMaxControlList
    # print(f'{servo_name}, {angle_increase}')
    if servo_name == "mid":
        if not angle_increase and midServo > MIN_MIDSERVO:
            midServoTemp = midServo - speed if (midServo - speed >= MIN_MIDSERVO) else MIN_MIDSERVO
            try:
                JetMaxControlList[0].publish(SetServo(data=int(midServoTemp), duration=DURATION))
            except Exception as e:
                traceback.print_exc()
        elif angle_increase and midServo < MAX_MIDSERVO:
            midServoTemp = midServo + speed if (midServo + speed <= MAX_MIDSERVO) else MAX_MIDSERVO
            JetMaxControlList[0].publish(SetServo(data=int(midServoTemp), duration=DURATION))

    elif servo_name == "left":
        if not angle_increase and leftServo > MIN_LEFTSERVO:
            leftServoTemp = leftServo - speed if (leftServo - speed >= MIN_LEFTSERVO) else MIN_LEFTSERVO
            JetMaxControlList[1].publish(SetServo(data=int(leftServoTemp), duration=DURATION))
        elif angle_increase and leftServo < MAX_LEFTSERVO:
            leftServoTemp = leftServo + speed if (leftServo + speed <= MAX_LEFTSERVO) else MAX_LEFTSERVO
            JetMaxControlList[1].publish(SetServo(data=int(leftServoTemp), duration=DURATION))

    elif servo_name == "right":
        if not angle_increase and rightServo > MIN_RIGHTSERVO:
            rightServoTemp = rightServo - speed if (rightServo - speed >= MIN_RIGHTSERVO) else MIN_RIGHTSERVO
            JetMaxControlList[2].publish(SetServo(data=int(rightServoTemp), duration=DURATION))
        elif not angle_increase and rightServo < MAX_RIGHTSERVO:
            rightServoTemp = rightServo + speed if (rightServo + speed <= MAX_RIGHTSERVO) else MAX_RIGHTSERVO
            JetMaxControlList[2].publish(SetServo(data=int(rightServoTemp), duration=DURATION))

    elif servo_name == "rotator":
        if not angle_increase and rotatorServo > MIN_ROTATOR:
            rotatorServoTemp = rotatorServo - speed if (rotatorServo - speed >= MIN_ROTATOR) else MIN_ROTATOR
            JetMaxControlList[3].publish(SetServo(data=int(rotatorServoTemp), duration=DURATION))
        elif angle_increase and rotatorServo < MAX_ROTATOR:
            rotatorServoTemp = rotatorServo + speed if (rotatorServo + speed <= MAX_ROTATOR) else MAX_ROTATOR
            JetMaxControlList[3].publish(SetServo(data=int(rotatorServoTemp), duration=DURATION))

    elif servo_name == "gripper":
        if not angle_increase and gripperServo > MIN_GRIPPER:
            gripperServoTemp = gripperServo - speed if (gripperServo - speed >= MIN_GRIPPER) else MIN_GRIPPER
            JetMaxControlList[4].publish(SetServo(data=int(gripperServoTemp), duration=DURATION))
        elif angle_increase and gripperServo < MAX_GRIPPER:
            gripperServoTemp = gripperServo + speed if (gripperServo + speed <= MAX_GRIPPER) else MAX_GRIPPER
            JetMaxControlList[4].publish(SetServo(data=int(gripperServoTemp), duration=DURATION))
    else:
        print(f"NOTOK")
        return f"NOTOK"
    print(f"{servo_name};{angle_increase};OK")
    return f"{servo_name};{angle_increase};OK"


@uamethod
def autoServo(parent, servo_name: str, direction: int):
    global SERVO_LOCK_AUTORUN
    if direction < -1 or direction > 1:
        return "NOTOK"
    if servo_name in SERVO_LOCK_AUTORUN:
        SERVO_LOCK_AUTORUN[servo_name] = direction
        return "OK"
    else:
        return "NOTOK"


@uamethod
def changeSpeed(parent, spd: int):
    global speed, cordinateSpeed
    if spd < 1 or spd > 30:
        return "NOTOK"
    speed = spd
    cordinateSpeed = math.floor(speed / 2)
    if (cordinateSpeed < 1):
        cordinateSpeed = 1
    return "OK"


@uamethod
def sucker(parent, suck: bool):
    JetMaxControlList[5].publish(Bool(data=suck))
    return "OK"


@uamethod
def moveCordinate(parent, cordinate: str, increase: bool):
    global cordinateSpeed
    if cordinate == "x":
        if increase:
            JetMaxControlList[7].publish(SetJetMax(x=cordinateSpeed, y=0, z=0, duration=0.2))
        else:
            JetMaxControlList[7].publish(SetJetMax(x=-cordinateSpeed, y=0, z=0, duration=0.2))
    elif cordinate == "y":
        if increase:
            JetMaxControlList[7].publish(SetJetMax(x=0, y=cordinateSpeed, z=0, duration=0.2))
        else:
            JetMaxControlList[7].publish(SetJetMax(x=0, y=-cordinateSpeed, z=0, duration=0.2))
    elif cordinate == "z":
        if increase:
            JetMaxControlList[7].publish(SetJetMax(x=0, y=0, z=cordinateSpeed, duration=0.2))
        else:
            JetMaxControlList[7].publish(SetJetMax(x=0, y=0, z=-cordinateSpeed, duration=0.2))
    else:
        return f'NOTOK; cordinate can only be x,y,z'
    return f'{cordinate};{increase};OK'


@uamethod
def autoCordinate(parent, cordinate: str, direction: int):
    global CORDINATE_LOCK_AUTORUN
    if direction < -1 or direction > 1:
        return "NOTOK"
    if cordinate in CORDINATE_LOCK_AUTORUN:
        CORDINATE_LOCK_AUTORUN[cordinate] = direction
        return "OK"
    else:
        return "NOTOK"


# -1: decrease angle, 0: stop, 1: increase angle
SERVO_LOCK_AUTORUN = {
    "mid": 0,
    "left": 0,
    "right": 0,
    "rotator": 0,
    "gripper": 0
}

CORDINATE_LOCK_AUTORUN = {
    "x": 0,
    "y": 0,
    "z": 0
}


class SubHandler(object):
    """
   Subscription Handler. To receive events from server for a subscription
   """

    def datachange_notification(self, node, val, data):
        _logger.warning("Python: New data change event %s %s", node, val)

    def event_notification(self, event):
        _logger.warning("Python: New event %s", event)


# replace server.start()
async def main():
    def updateRobot(data):
        """
        function to read Robot Arm angle data and update to opcua object model (opcua server)
        """
        global midServo, leftServo, rightServo, rotatorServo, speed, suckcup, oldData, x, y, z
        if oldData == data:
            # print("The same data")
            if speed != speedNode.get_value():
                speedNode.set_value(speed)
            return
        else:
            # print(oldData == data)
            pass
        midServo = data.servo1
        leftServo = data.servo2
        rightServo = data.servo3
        rotatorServo = data.pwm1
        gripperServo = data.pwm2
        suckcup = data.sucker
        x = data.x
        y = data.y
        z = data.z
        try:
            midServoNode.set_value(midServo)
            leftServoNode.set_value(leftServo)
            rightServoNode.set_value(rightServo)
            rotatorServoNode.set_value(rotatorServo)
            suckNode.set_value(suckcup)
            gripperServoNode.set_value(gripperServo)
            xNode.set_value(x)
            yNode.set_value(y)
            zNode.set_value(z)
        except Exception as e:
            traceback.print_exc()
        finally:
            oldData = data

    async def autoRun():
        """
        This function will run in a loop which control the arm to
        move automatically. To do that, use call method [autoServo]
        to enable the lock.
        :return: None
        """
        global SERVO_LOCK_AUTORUN
        while not rospy.is_shutdown():
            # rospy is shutdown when ctrl - C is pressed!
            try:
                if SERVO_LOCK_AUTORUN["left"] != 0:
                    moveServo(idx, "left",
                              ua.Variant(True if SERVO_LOCK_AUTORUN["left"] == 1 else False,
                                         ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["right"] != 0:
                    moveServo(idx, "right",
                              ua.Variant(True if SERVO_LOCK_AUTORUN["right"] == 1 else False,
                                         ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["mid"] != 0:
                    moveServo(idx, "mid",
                              ua.Variant(True if SERVO_LOCK_AUTORUN["mid"] == 1 else False,
                                         ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["rotator"] != 0:
                    moveServo(idx, "rotator",
                              ua.Variant(True if SERVO_LOCK_AUTORUN["rotator"] == 1 else False,
                                         ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["gripper"] != 0:
                    moveServo(idx, "gripper",
                              ua.Variant(True if SERVO_LOCK_AUTORUN["gripper"] == 1 else False,
                                         ua.VariantType.Boolean))
                if CORDINATE_LOCK_AUTORUN["x"] != 0:
                    moveCordinate(idx, "x",
                                  ua.Variant(True if CORDINATE_LOCK_AUTORUN["x"] == 1 else False,
                                             ua.VariantType.Boolean))
                if CORDINATE_LOCK_AUTORUN["y"] != 0:
                    moveCordinate(idx, "y",
                                  ua.Variant(True if CORDINATE_LOCK_AUTORUN["y"] == 1 else False,
                                             ua.VariantType.Boolean))
                if CORDINATE_LOCK_AUTORUN["z"] != 0:
                    moveCordinate(idx, "z",
                                  ua.Variant(True if CORDINATE_LOCK_AUTORUN["z"] == 1 else False,
                                             ua.VariantType.Boolean))
                await asyncio.sleep(0.2)
                # print("sleep 5 seconds")
            except Exception:
                traceback.print_exc()

    # server.init()
    server = Server()

    # endpoint: address to connect to
    server.set_endpoint(f"opc.tcp://{IPAddr}:4841")
    server.set_server_name("Robot Arm Server")

    # set all possible endpoint policies for client to connect through
    server.set_security_policy(
        [
            ua.SecurityPolicyType.NoSecurity,
            ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
            ua.SecurityPolicyType.Basic256Sha256_Sign,
        ]
    )

    # setup our namespace. An endpoint can have multiple namespace!
    uri = "https://robotarm.opcua.io"
    idx = server.register_namespace(uri)

    # add some nodes
    myfolder = server.nodes.objects.add_folder(idx, "Robot Arm")

    servo_folder = myfolder.add_folder(idx, "Servo")
    midServoNode = servo_folder.add_variable(idx, "mid", 90, varianttype=ua.VariantType.Int16)
    leftServoNode = servo_folder.add_variable(idx, "left", 90, varianttype=ua.VariantType.Int16)
    rightServoNode = servo_folder.add_variable(idx, "right", 90, varianttype=ua.VariantType.Int16)

    add_on_folder = myfolder.add_folder(idx, "Add-on")
    rotatorServoNode = add_on_folder.add_variable(idx, "rotator", 90, varianttype=ua.VariantType.Int16)
    gripperServoNode = add_on_folder.add_variable(idx, "gripper", 90, varianttype=ua.VariantType.Int16)
    suckNode = add_on_folder.add_variable(idx, "suckcup", False, varianttype=ua.VariantType.Boolean)

    speedNode = myfolder.add_variable(idx, "speed", 5)

    cordinateFolder = myfolder.add_folder(idx, "Cordinate")
    xNode = cordinateFolder.add_variable(idx, "x", 0, varianttype=ua.VariantType.Double)
    yNode = cordinateFolder.add_variable(idx, "y", 0, varianttype=ua.VariantType.Double)
    zNode = cordinateFolder.add_variable(idx, "z", 0, varianttype=ua.VariantType.Double)

    async def serverStart():
        print("serveropc", threading.current_thread().getName())
        with server:
            print(f'OPC server running at {server.endpoint[0]}://{server.endpoint[1]}')
            # asyncio.gather giup chay 2 ham async 1 cach "song song"
            await asyncio.gather(autoRun())
        print("Exit server")
            
    async def ros_run():
        print("rosrun", threading.current_thread().getName())
        global JetMaxControlList
        rospy.init_node("opcua", anonymous=False, log_level=rospy.DEBUG)
        rospy.Subscriber('/jetmax/status', JetMax, callback=updateRobot)

        # Append servos to list JetMaxControlList
        for i in range(1, 4):
            jetmax_pub_control = rospy.Publisher('/jetmax/servo{}/command'.format(i), SetServo, queue_size=1)
            JetMaxControlList.append(jetmax_pub_control)

        for i in range(1, 3):
            jetmax_pub_end_effector = rospy.Publisher('/jetmax/end_effector/servo{}/command'.format(i), SetServo,
                                                      queue_size=1)
            JetMaxControlList.append(jetmax_pub_end_effector)

        jetmax_pub_sucker = rospy.Publisher('/jetmax/end_effector/sucker/command', Bool, queue_size=1)

        jetmax_pos_cmd = rospy.Publisher('/jetmax/command', SetJetMax, queue_size=1)
        jetmax_relative_pos_cmd = rospy.Publisher('/jetmax/relative_command', SetJetMax, queue_size=1)

        JetMaxControlList.extend([jetmax_pub_sucker, jetmax_pos_cmd, jetmax_relative_pos_cmd])
        while not rospy.is_shutdown():
            # rospy is shutdown when ctrl - C is pressed!
            await asyncio.sleep(1)
        print("Exit rospy")
        
            
    await asyncio.gather(serverStart(), ros_run())



if __name__ == "__main__":
    ourFurture = None
    try:
        logging.basicConfig(level=logging.INFO)
        loop = asyncio.get_event_loop()
        print("main", threading.current_thread().getName())
        loop.run_until_complete(main())
    except Exception as e:
        traceback.print_exc()
    finally:
        loop.stop()
        loop.close()
        exit()


