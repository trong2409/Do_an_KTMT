import logging
import asyncio
import socket

from asyncua import ua, uamethod, Server

_logger = logging.getLogger(__name__)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

MIN_MIDSERVO = 0
MAX_MIDSERVO = 270

MIN_LEFTSERVO = 0
MAX_LEFTSERVO = 180

MIN_RIGHTSERVO = 0
MAX_RIGHTSERVO = 90

MIN_GRIPPER = 0
MAX_GRIPPER = 180

midServo = 90
leftServo = 90
rightServo = 90
gripperServo = 90
speed = 5


@uamethod
def moveServo(parent, servo_name: str, angle_decrease: bool):
    global midServo, leftServo, rightServo, gripperServo, speed
    # print(f'{servo_name}, {angle_decrease}')
    if servo_name == "M":
        if angle_decrease and midServo > MIN_MIDSERVO:
            midServo = midServo - speed if (midServo - speed >= MIN_MIDSERVO) else MIN_MIDSERVO
        elif not angle_decrease and midServo < MAX_MIDSERVO:
            midServo = midServo + speed if (midServo + speed <= MAX_MIDSERVO) else MAX_MIDSERVO
    if servo_name == "L":
        if angle_decrease and leftServo > MIN_LEFTSERVO:
            leftServo = leftServo - speed if (leftServo - speed >= MIN_LEFTSERVO) else MIN_LEFTSERVO
        elif not angle_decrease and leftServo < MAX_LEFTSERVO:
            leftServo = leftServo + speed if (leftServo + speed <= MAX_LEFTSERVO) else MAX_LEFTSERVO
    if servo_name == "R":
        if angle_decrease and rightServo > MIN_RIGHTSERVO:
            rightServo = rightServo - speed if (rightServo - speed >= MIN_RIGHTSERVO) else MIN_RIGHTSERVO
        elif not angle_decrease and rightServo < MAX_RIGHTSERVO:
            rightServo = rightServo + speed if (rightServo + speed <= MAX_RIGHTSERVO) else MAX_RIGHTSERVO
    if servo_name == "G":
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
    if servo_name == "M":
        SERVO_LOCK_AUTORUN["MID_SERVO"] = direction
    if servo_name == "L":
        SERVO_LOCK_AUTORUN["LEFT_SERVO"] = direction
    if servo_name == "R":
        SERVO_LOCK_AUTORUN["RIGHT_SERVO"] = direction
    if servo_name == "G":
        SERVO_LOCK_AUTORUN["GRIPPER_SERVO"] = direction
    return "OK"




# -1: decrease angle, 0: stop, 1: increase angle
SERVO_LOCK_AUTORUN = {
    "MID_SERVO": 0,
    "LEFT_SERVO": 0,
    "RIGHT_SERVO": 0,
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
    async def updateRobot():
        global midServo, leftServo, rightServo, gripperServo, speed
        while True:
            if midServo != await midServoNode.get_value():
                await midServoNode.write_value(midServo)
            if leftServo != await leftServoNode.get_value():
                await leftServoNode.write_value(leftServo)
            if rightServo != await rightServoNode.get_value():
                await rightServoNode.write_value(rightServo)
            if gripperServo != await gripperServoNode.get_value():
                await gripperServoNode.write_value(gripperServo)
            if speed != await speedNode.get_value():
                speed = await speedNode.get_value()
            await asyncio.sleep(0.005)

    async def autoRun():
        global SERVO_LOCK_AUTORUN
        while True:
            if SERVO_LOCK_AUTORUN["LEFT_SERVO"] == -1:
                moveServo(idx, "L", ua.Variant(True, ua.VariantType.Boolean))
            if SERVO_LOCK_AUTORUN["LEFT_SERVO"] == 1:
                moveServo(idx, "L", ua.Variant(False, ua.VariantType.Boolean))
            if SERVO_LOCK_AUTORUN["RIGHT_SERVO"] == -1:
                moveServo(idx, "R", ua.Variant(True, ua.VariantType.Boolean))
            if SERVO_LOCK_AUTORUN["RIGHT_SERVO"] == 1:
                moveServo(idx, "R", ua.Variant(False, ua.VariantType.Boolean))
            if SERVO_LOCK_AUTORUN["MID_SERVO"] == -1:
                moveServo(idx, "M", ua.Variant(True, ua.VariantType.Boolean))
            if SERVO_LOCK_AUTORUN["MID_SERVO"] == 1:
                moveServo(idx, "M", ua.Variant(False, ua.VariantType.Boolean))
            if SERVO_LOCK_AUTORUN["GRIPPER_SERVO"] == -1:
                moveServo(idx, "G", ua.Variant(True, ua.VariantType.Boolean))
            if SERVO_LOCK_AUTORUN["GRIPPER_SERVO"] == 1:
                moveServo(idx, "G", ua.Variant(False, ua.VariantType.Boolean))
            await asyncio.sleep(0.1)
            # print("sleep 5 seconds")




    server = Server()

    await server.init()

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
    idx = await server.register_namespace(uri)

    # add some nodes
    myfolder = await server.nodes.objects.add_folder(idx, "Robot Arm")
    midServoNode = await myfolder.add_variable(idx, "M", 90)
    leftServoNode = await myfolder.add_variable(idx, "L", 90)
    rightServoNode = await myfolder.add_variable(idx, "R", 90)
    gripperServoNode = await myfolder.add_variable(idx, "G", 90)
    speedNode = await myfolder.add_variable(idx, "S", 5)

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

    method = await myfolder.add_method(idx,
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

    method1 = await myfolder.add_method(idx,
                                        "autoServo",
                                        autoServo,
                                        [inargx1, inargy1],
                                        [outarg1])

    await midServoNode.set_writable()
    await leftServoNode.set_writable()
    await rightServoNode.set_writable()
    await gripperServoNode.set_writable()
    await speedNode.set_writable()

    async with server:
        print(f'OPC server running at {await server.get_endpoints()}')
        # asyncio.gather giup chay 2 ham async 1 cach "song song"
        await asyncio.gather(updateRobot(), autoRun())




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
