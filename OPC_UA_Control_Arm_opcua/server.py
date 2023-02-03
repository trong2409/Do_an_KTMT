#!/usr/bin/env python3

import logging
import netifaces as ni
import asyncio
import traceback

import rospy
#from std_srvs.srv import Empty
from std_msgs.msg import Bool
from opc_ros.msg import SetServo, JetMax

from opcua import ua, uamethod, Server

_logger = logging.getLogger(__name__)

IPAddr = ni.ifaddresses('ap0')[ni.AF_INET][0]['addr']

MIN_MIDSERVO = 0
MAX_MIDSERVO = 240

MIN_LEFTSERVO = -30
MAX_LEFTSERVO = 210

MIN_RIGHTSERVO = -120
MAX_RIGHTSERVO = 120

MIN_ROTATOR = 0
MAX_ROTATOR = 180

MIN_GRIPPER = 0
MAX_GRIPPER = 180

midServo = 90
leftServo = 90
rightServo = 90
rotatorServo = 90
gripperServo = 90
suckcup = False
speed = 5

JetMaxControlList = list()
#  0 -> mid
#  1 -> left
#  2 -> right
#  3 -> rotator
#  4 -> fold
#  5 -> sucker

@uamethod
def moveServo(parent, servo_name: str, angle_decrease: bool):
    global midServo, leftServo, rightServo, rotatorServo, speed
    # print(f'{servo_name}, {angle_decrease}')
    if servo_name == "mid":
        if angle_decrease and midServo > MIN_MIDSERVO:
            midServotemp = midServo - speed if (midServo - speed >= MIN_MIDSERVO) else MIN_MIDSERVO
        elif not angle_decrease and midServo < MAX_MIDSERVO:
            midServo = midServo + speed if (midServo + speed <= MAX_MIDSERVO) else MAX_MIDSERVO
            try:
                jetmax_pub.publish(SetJetMax(x=-10,y=0,z=0,duration=0.1))
            except Exception as e:
                traceback.print_exc()
    if servo_name == "left":
        if angle_decrease and leftServo > MIN_LEFTSERVO:
            leftServo = leftServo - speed if (leftServo - speed >= MIN_LEFTSERVO) else MIN_LEFTSERVO
        elif not angle_decrease and leftServo < MAX_LEFTSERVO:
            leftServo = leftServo + speed if (leftServo + speed <= MAX_LEFTSERVO) else MAX_LEFTSERVO
    if servo_name == "right":
        if angle_decrease and rightServo > MIN_RIGHTSERVO:
            rightServo = rightServo - speed if (rightServo - speed >= MIN_RIGHTSERVO) else MIN_RIGHTSERVO
        elif not angle_decrease and rightServo < MAX_RIGHTSERVO:
            rightServo = rightServo + speed if (rightServo + speed <= MAX_RIGHTSERVO) else MAX_RIGHTSERVO
    if servo_name == "rotator":
        if angle_decrease and rotatorServo > MIN_ROTATOR:
            rotatorServo = rotatorServo - speed if (rotatorServo - speed >= MIN_ROTATOR) else MIN_ROTATOR
        elif not angle_decrease and rotatorServo < MAX_ROTATOR:
            rotatorServo = rotatorServo + speed if (rotatorServo + speed <= MAX_ROTATOR) else MAX_ROTATOR
    if servo_name == "gripper":
        if angle_decrease and gripperServo > MIN_GRIPPER:
            gripperServo = gripperServo - speed if (gripperServo - speed >= MIN_GRIPPER) else MIN_GRIPPER
        elif not angle_decrease and gripperServo < MAX_GRIPPER:
            gripperServo = gripperServo + speed if (gripperServo + speed <= MAX_GRIPPER) else MAX_GRIPPER
    return f"{servo_name};{angle_decrease};OK"

@uamethod
def autoServo(parent, servo_name: str, direction: int):
    global SERVO_LOCK_AUTORUN
    if direction < -1 or direction > 1:
        return "NOTOK"
    if servo_name == "mid":
        SERVO_LOCK_AUTORUN["MID_SERVO"] = direction
    if servo_name == "left":
        SERVO_LOCK_AUTORUN["LEFT_SERVO"] = direction
    if servo_name == "right":
        SERVO_LOCK_AUTORUN["RIGHT_SERVO"] = direction
    if servo_name == "rotator":
        SERVO_LOCK_AUTORUN["ROTATOR_SERVO"] = direction
    if servo_name == "gripper":
        SERVO_LOCK_AUTORUN["GRIPPER_SERVO"] = direction
    return "OK"

# -1: decrease angle, 0: stop, 1: increase angle
SERVO_LOCK_AUTORUN = {
    "MID_SERVO": 0,
    "LEFT_SERVO": 0,
    "RIGHT_SERVO": 0,
    "ROTATOR_SERVO": 0,
    "GRIPPER_SERVO": 0
}

class SubHandler(object):
    """
   Subscription Handler. To receive events from server for a subscription
   """

    def datachange_notification(self, node, val, data):
        _logger.warning("Python: New data change event %s %s", node, val)

    def event_notification(self, event):
        _logger.warning("Python: New event %s", event)

#replace server.start()
async def main():
    def updateRobot(data):
        """
        function to read Robot Arm angle data and update to opcua object model (opcua server)
        """
        global midServo, leftServo, rightServo, rotatorServo, speed, suckcup
        midServo = data.joint1
        leftServo = data.joint2
        rightServo = data.joint3
        rotatorServo = data.pwm1
        gripperServo = data.pwm2
        suckcup = data.sucker
        try:
            if midServo != midServoNode.get_value():
                midServoNode.set_value(midServo)
            if leftServo != leftServoNode.get_value():
                leftServoNode.set_value(leftServo)
            if rightServo != rightServoNode.get_value():
                rightServoNode.set_value(rightServo)
            if rotatorServo != rotatorServoNode.get_value():
                rotatorServoNode.set_value(rotatorServo)
            if suckcup != suckNode.get_value():
                suckNode.set_value(suckcup)
            if gripperServo != gripperServoNode.get_value():
                gripperServoNode.set_value(gripperServo)
            if speed != speedNode.get_value():
                speed = speedNode.get_value()
        except Exception as e:
            traceback.print_exc()

    async def autoRun():
        """
        This function will run in a loop which control the arm to
        move automatically. To do that, use call method [autoServo]
        to enable the lock.
        :return: None
        """
        global SERVO_LOCK_AUTORUN
        while True:
            try:
                if SERVO_LOCK_AUTORUN["LEFT_SERVO"] == -1:
                    moveServo(idx, "left", ua.Variant(True, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["LEFT_SERVO"] == 1:
                    moveServo(idx, "left", ua.Variant(False, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["RIGHT_SERVO"] == -1:
                    moveServo(idx, "right", ua.Variant(True, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["RIGHT_SERVO"] == 1:
                    moveServo(idx, "right", ua.Variant(False, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["MID_SERVO"] == -1:
                    moveServo(idx, "mid", ua.Variant(True, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["MID_SERVO"] == 1:
                    moveServo(idx, "mid", ua.Variant(False, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["ROTATOR_SERVO"] == -1:
                    moveServo(idx, "rotator", ua.Variant(True, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["ROTATOR_SERVO"] == 1:
                    moveServo(idx, "rotator", ua.Variant(False, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["GRIPPER_SERVO"] == -1:
                    moveServo(idx, "gripper", ua.Variant(True, ua.VariantType.Boolean))
                if SERVO_LOCK_AUTORUN["GRIPPER_SERVO"] == 1:
                    moveServo(idx, "gripper", ua.Variant(False, ua.VariantType.Boolean))
                await asyncio.sleep(0.2)
                # print("sleep 5 seconds")
            except KeyboardInterrupt:
                break
 

    async def ros_run():
        global JetMaxControlList
        rospy.init_node("opcua", anonymous=True)
        rospy.Subscriber('/jetmax/status',JetMax,callback=updateRobot)

        # Append servos to list JetMaxControlList
        for i in range(1,4):
            jetmax_pub_control = rospy.Publisher('/jetmax/servo{}/command'.format(i),SetServo,queue_size=1)
            JetMaxControlList.append(jetmax_pub_control)
            
        for i in range(1,3):
            jetmax_pub_end_effector = rospy.Publisher('/jetmax/end_effector/servo{}/command'.format(i),SetServo,queue_size=1)
            JetMaxControlList.append(jetmax_pub_end_effector)
        
        jetmax_pub_sucker = rospy.Publisher('/jetmax/end_effector/sucker/command',Bool,queue_size=1)
        JetMaxControlList.append(jetmax_pub_sucker)
            
    

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
    midServoNode = myfolder.add_variable(idx, "mid", 90, varianttype=ua.VariantType.Double)
    leftServoNode = myfolder.add_variable(idx, "left", 90, varianttype=ua.VariantType.Double)
    rightServoNode = myfolder.add_variable(idx, "right", 90, varianttype=ua.VariantType.Double)
    rotatorServoNode = myfolder.add_variable(idx, "rotator", 90, varianttype=ua.VariantType.Int16)
    gripperServoNode = myfolder.add_variable(idx, "gripper", 90, varianttype=ua.VariantType.Int16)
    suckNode = myfolder.add_variable(idx, "suckcup", False, varianttype=ua.VariantType.Boolean)
    speedNode = myfolder.add_variable(idx, "S", 5)

    inargx = ua.Argument()
    inargx.Name = "Servo"
    inargx.DataType = ua.NodeId(ua.ObjectIds.String)
    inargx.ValueRank = -1
    inargx.ArrayDimensions = []
    inargx.Description = ua.LocalizedText("Servo name")
    inargy = ua.Argument()
    inargy.Name = "Decrease angle"
    inargy.DataType = ua.NodeId(ua.ObjectIds.Boolean)
    inargy.ValueRank = -1
    inargy.ArrayDimensions = []
    inargy.Description = ua.LocalizedText("Decrease the angle of servo")
    outarg = ua.Argument()
    outarg.Name = "Ack"
    outarg.DataType = ua.NodeId(ua.ObjectIds.String)
    outarg.ValueRank = -1
    outarg.ArrayDimensions = []
    outarg.Description = ua.LocalizedText("Acknowledgement")

    method = myfolder.add_method(idx,
                               "moveServo",
                               moveServo,
                               [inargx, inargy],
                               [outarg])

    inargx1 = ua.Argument()
    inargx1.Name = "Servo"
    inargx1.DataType = ua.NodeId(ua.ObjectIds.String)
    inargx1.ValueRank = -1
    inargx1.ArrayDimensions = []
    inargx1.Description = ua.LocalizedText("Servo name")
    inargy1 = ua.Argument()
    inargy1.Name = "Direction"
    inargy1.DataType = ua.NodeId(ua.ObjectIds.Int16)
    inargy1.ValueRank = -1
    inargy1.ArrayDimensions = []
    inargy1.Description = ua.LocalizedText("Direction of servo, -1 to decrease, 0 to stop and 1 to increase")
    outarg1 = ua.Argument()
    outarg1.Name = "Ack"
    outarg1.DataType = ua.NodeId(ua.ObjectIds.String)
    outarg1.ValueRank = -1
    outarg1.ArrayDimensions = []
    outarg1.Description = ua.LocalizedText("Acknowledgement")

    method1 = myfolder.add_method(idx,
                                "autoServo",
                                autoServo,
                                [inargx1, inargy1],
                                [outarg1])

    midServoNode.set_writable()
    leftServoNode.set_writable()
    rightServoNode.set_writable()
    rotatorServoNode.set_writable()
    speedNode.set_writable()
    
    

    with server:
        print(f'OPC server running at {server.endpoint[0]}://{server.endpoint[1]}')
        # asyncio.gather giup chay 2 ham async 1 cach "song song"
        
        await asyncio.gather(autoRun(), ros_run())
        #await asyncio.gather(autoRun(), return_exceptions=True)
        #await asyncio.gather(ros_run())




if __name__ == "__main__":
    
    try:
        logging.basicConfig(level=logging.INFO)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except rospy.ROSInterruptException:
        loop.close()
    except KeyboardInterrupt:
        print("Interrupt")
        
    finally:
        loop.close()
        exit()


