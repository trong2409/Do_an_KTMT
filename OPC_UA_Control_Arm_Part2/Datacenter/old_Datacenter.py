import threading
import time

import asyncua
import opcua
from asyncua import Server, Client, ua, uamethod
import asyncio
import socket
import logging
import netifaces as ni

_logger = logging.getLogger(__name__)

ServerIPAddr = "192.168.149.1"

# hostname = socket.gethostname()
# DataCenterIPAddr = socket.gethostbyname(hostname)

DataCenterIPAddr = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
# DataCenterIPAddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

# a list that contain multiple wrapper function of this datacenter
functionWrapperList = list()


class ClientSubHandler(object):
    """
   Subscription Handler. To receive events from server for a subscription
   DO NOT PUT LENGTHY FUNCTION CALL RUN HERE, IT WON'T WORK.
   FOR EXAMPLE, YOU SUB TO A NODE FROM ANOTHER SERVER, AND THEN ASK FOR
   serverNode.get_browse_node() HERE
   WILL RAISE TIME_OUT EXCEPTION. I DON'T FUCKING KNOW WHY.
   """

    def __init__(self):
        """
        Mot dictionary gom cac phan tu co dang dict["ns=2;i=x"] = DataCenter Node
        key la node ID cua server ma Datacenter subscribe toi
        value la Node trong Datacenter, tuong ung voi node cua Server
        vi Datacenter co muc dich la "copy va 'anh xa." lai cac node trong Server, nen de
        thay doi cac Node trong Datacenter theo su thay doi cua node trong Server,
        ta se su dung dictionary nay,
        """
        self.subscriptionDict = dict()
        # a list contain all server nodes that need to subscribe to
        self.subscriptionList = list()
        # a queue of command to update Datacenter value node
        self.cmdQueue = list()

    def datachange_notification(self, node: opcua.Node, val, data):
        """
        Ham nay se duoc callback khi co su thay doi cua node dang duoc subscribe toi,
        mang 1 so thong tin nhu.
        Trong ham nay, khi node "ns=2;i=x" cua server co su thay doi, ta se truy cap vao
        dict[ns=2;i=x] de lay ra Node tuong ung trong Datacenter. Neu co node tuong ung
        ta gui nodeID "ns=2;i=x" va gia tri can cap nhat (val) vao cmdQueue
        :param node: Node co gia tri bi thay doi. Day la mot object opcua.Node
        :param val: Gia tri cua node vua thay doi
        :param data: ?
        :return: None
        """
        self.cmdQueue.append((node, val))
        # self.subscriptionDict[node.nodeid.to_string()].set_value(val)
        # print(node.nodeid.to_string())
        # print(self.subscriptionDict)
        # _logger.warning("Python: New data change event %s %s", node, val)

    def event_notification(self, event):
        # _logger.warning("Python: New event %s", event)
        pass

    async def executeQueueCmd(self):
        while len(self.cmdQueue) > 0:
            node, val = self.cmdQueue.pop()
            # name = node.get_browse_name().Name
            # print(f'Execute cmd: node {name} -> {val}')
            nodeID = node.nodeid.to_string()
            if self.subscriptionDict[nodeID] is not None:
                datacenterNode = self.subscriptionDict[nodeID]
                # if nodeID != "ns=2;i=16" and nodeID != "ns=2;i=17":
                #     print(f'{node.nodeid.to_string()} -> {type(val)} -> {val}')
                await datacenterNode.set_value(val)


serverURL = f'opc.tcp://{ServerIPAddr}:4841'
Snamespace = "https://robotarm.opcua.io"

dataCenterURL = f'opc.tcp://{DataCenterIPAddr}:4840'
DCnamespace = "https://datacenter.opcua.io"


async def main():
    """
    ref: https://stackoverflow.com/questions/3480184/pass-a-list-to-a-function-to-act-as-multiple-arguments
    ref: https://stackoverflow.com/questions/3687682/how-to-dynamically-define-functions
    :return:
    """

    def functionWrapper(*input_args):
        """
        Dynamically create a wrapper method that can call server method.
        :param input_args: client, server_Method_ID
        :return: a wrapper function that call server method.
        """
        client = input_args[0]
        methodID = input_args[1]
        methodNode = client.get_node(methodID)

        @uamethod
        async def caller(parent, *inputArg):
            """
            caller is a wrapper function that call server method
            :param parent: parent from opcua
            :param inputArg: list of argument to pass into the method.
            number of argument is specified when adding method to opcua server,
            not from function definition
            :return: result of method called from server
            """
            inputArg = list(inputArg)
            print(client, methodID, methodNode)
            # *inputArg duoc goi la "unpacking list"
            return await client.nodes.objects.call_method(methodNode, *inputArg)

        return caller

    async def browseNode( client: asyncua.Client,
                        datacenterParentNode: asyncua.Node,
                         nodes: list[asyncua.Node], migrate: bool,
                         subhandler: ClientSubHandler) -> list:
        """
        Ham brosweNode se:
            broswe cac Node trong Server, trich xuat cac thong tin nhu
                name: ten node
                nodeID: ns=x;i=y
                nodeClass: Variable, Object,...
                value: gia tri cua Node. mot so Node khong co value nhu Object Node
            Khi migrate = True, can truyen them tham so subhandler
            Khi nay, ham se co "copy", tao ra cac node va method giong nhu node ben server \n
            dong thoi tu dong subscribe vao cac node ben server de cap nhat khi co su thay doi
        browseNode(
            DatacenterParentNode: specify the node of datacenter which we need to "append" the browsing result to \n
            Nodes: list of node from the server that Datacenter is connected to, and start browsing them \n
            Migrate: "copy" the node from the server and create them in Datacenter (True/False) \n
            Subhandler: an object of subhandler.
        )
        """
        datacenterNode = None
        returnVal = list()
        for node in nodes:
            value = 0
            try:
                nodeClass = (await node.read_node_class()).name
                name = (await node.read_browse_name()).Name
                nodeID = node.nodeid.to_string()

                # check Class of the Node and perform needed action
                if nodeClass == "Variable":
                    value = await node.get_value()
                    datatype = (await node.read_data_type()).Identifier

                    if migrate:

                        datacenterNode = await datacenterParentNode.add_variable(idx, name, value,
                                                                                 datatype=datatype) if (
                                    datacenterParentNode is not None) else None
                        subhandler.subscriptionDict[nodeID] = datacenterNode
                        if name == "InputArguments" or name == "OutputArguments":
                            returnVal.append(value)
                        else:
                            subhandler.subscriptionList.append(node)
                        accessLevel = await node.get_access_level()
                        try:
                            await datacenterNode.set_writable(ua.AccessLevel.CurrentWrite in accessLevel)
                        except:
                            pass
                elif nodeClass == "Object":
                    nodeClassRefs = await node.get_references(40)  # reference 40 la reference toi: "HasTypeDefinition",
                    # giup minh xem duoc ro rang hon Folder type
                    nodeClass = nodeClassRefs[0].BrowseName.Name
                    if nodeClass == "FolderType":
                        if migrate:
                            datacenterNode = await datacenterParentNode.add_folder(idx, name) if (
                                        datacenterParentNode is not None) else None
                            # subhandler.subscriptionDict[nodeID] = datacenterNode
                            # subhandler.subscriptionList.append(node)
                    else:
                        raise Exception(f"nodeClass of type {nodeClass} is not handled")
                elif nodeClass == "Method":
                    datacenterNode = None
                else:
                    datacenterNode = None
                    raise Exception(f"nodeClass of type {nodeClass} is not handled")

                print("=" * 20, f"\n{name}:{nodeID}:{nodeClass}\nValue={value}")
                # If we're browsing input and output argument of method, we need to return
                # the browsing result back to the method, so we can add it and make method
                # returnVal is a list, and this will be return back to create new method


                # after getting the info of current node, continue to browse its children (if exist)
                children = await node.get_children()
                if children is not None:
                    # in case of Method, we need the input and output argument info. but these
                    # argument is actually the children of the method node, so we have to
                    # browse these children and return back to create Method.
                    # browseNode function can know if the node it's browsing is an input/output argument
                    # of a method or not, and return these argument.
                    if nodeClass == "Method":
                        inoutArgs = await browseNode(client, datacenterNode, children, migrate, subhandler)
                        inArgsFunc = list()
                        outArgsFunc = list()
                        if len(inoutArgs) > 2:
                            inArgs = inoutArgs.pop(0)
                            for inArg in inArgs:
                                uaArg = ua.Argument(
                                    Name=inArg.Name,
                                    DataType=inArg.DataType,
                                    ValueRank=inArg.ValueRank,
                                    ArrayDimensions=inArg.ArrayDimensions,
                                    Description=inArg.Description
                                )
                                inArgsFunc.append(uaArg)
                        outArgs = inoutArgs.pop(0)
                        for outArg in outArgs:
                            uaArg = ua.Argument(
                                Name=outArg.Name,
                                DataType=outArg.DataType,
                                ValueRank=outArg.ValueRank,
                                ArrayDimensions=outArg.ArrayDimensions,
                                Description=outArg.Description
                            )
                            outArgsFunc.append(uaArg)
                        if migrate:
                            methodFunc = functionWrapper(client, nodeID)
                            functionWrapperList.append(methodFunc)
                            datacenterNode = await datacenterParentNode.add_method(idx, name,
                                                                                   methodFunc, inArgsFunc, outArgsFunc)
                    else:
                        await browseNode(client, datacenterNode, children, migrate, subhandler)
            except Exception as e:
                print(f'Can\'t read node {node} at {node.nodeid.to_string()}: {e}')
        returnVal.append(datacenterNode)
        return returnVal


    """
    ================================= SERVER (DATACENTER) SECTION ====================================
    """
    server = Server()

    await server.init()

    server.set_endpoint(dataCenterURL)
    server.set_server_name("DataCenter Server")

    # set all possible endpoint policies for client to connect through
    server.set_security_policy(
        [
            ua.SecurityPolicyType.NoSecurity,
            ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
            ua.SecurityPolicyType.Basic256Sha256_Sign,
        ]
    )

    await server.load_certificate("datacenS_cer.der")
    await server.load_private_key("dskey.pem")

    # setup our namespace. An endpoint can have multiple namespace!
    idx = await server.register_namespace(DCnamespace)
    await server.start()
    print(f'OPC datacenter running at {server.endpoint[0]}://{server.endpoint[1]}')

    """
    ================================= /SERVER (DATACENTER) SECTION ====================================
    """



    async def serverConnect():
        while True:
            await asyncio.sleep(1)

    async def clientConnect():
        rootNode = None
        clientSubscription = None
        client = None
        while True:
            """
               ================================= CLIENT SECTION ====================================
               """
            client = Client(serverURL)
            try:
                await client.set_security_string("Basic256Sha256,SignAndEncrypt,datacenCL_cer.der,dclkey.pem")
                await client.connect()
                print(f"Connected to {serverURL} ...")

                # Find the namespace index
                # nsidx = client.get_namespace_index(namespace)
                # print(f"Namespace Index for '{namespace}': {nsidx}")
                listOfNode = await client.nodes.objects.get_children()
                # print(listOfNode)
                listOfMainNode = listOfNode[1:]
                # aNode = listOfMainNode[0]
                # print(aNode, type(aNode), aNode.get_browse_name())

                # each client will have 1 sub handler
                clientHandler = ClientSubHandler()
                clientSubscription = await client.create_subscription(1, clientHandler)
                rootNode = (await browseNode(client, server.nodes.objects, listOfMainNode, True, clientHandler)).pop()
                await clientSubscription.subscribe_data_change(clientHandler.subscriptionList)

                checkConectionPeriod = 0

                """
                ================================= /CLIENT SECTION ====================================
                """
                while True:
                    checkConectionPeriod += 1
                    if checkConectionPeriod == 5000:
                        await client.check_connection()
                        checkConectionPeriod = 0
                    await clientHandler.executeQueueCmd()
                    await asyncio.sleep(0.001)
            except KeyboardInterrupt:
                break
            except (ConnectionError, ua.UaError):
                if rootNode is not None:
                    await server.delete_nodes([rootNode], recursive=True)
                    # await clientSubscription.delete()
                print("Trying to reconnect in 2 seconds")
                await asyncio.sleep(2)
            except (TimeoutError):
                print("Timeout!")
        await client.disconnect()


    # thread = threading.Thread(target=clientConnect)
    # thread.start()
    await asyncio.gather(serverConnect(), clientConnect())

    await server.stop()



if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    asyncio.run(main())
