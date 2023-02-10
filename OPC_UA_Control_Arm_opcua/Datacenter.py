import opcua
from opcua import ua, uamethod, Client, Server
import asyncio
import socket
import logging

_logger = logging.getLogger(__name__)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# contain several item with maping: { "datacenterUnity_x" : unity server node }
UNITY_SERVER_NODES = {}
# a list of datacenter nodes that datacenter listen to! (listen to its self)
DATACENTER_SUBSCRIPTION_LIST = []
# a list that contain multiple wrapper function of this datacenter
functionWrapperList = list()

class ServerSubHandler(object):
    """
      Subscription Handler. To receive events from server for a subscription
      DO NOT PUT LENGTHY FUNCTION CALL RUN HERE, IT WON'T WORK
      """

    def __init__(self):
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
        self.cmdQueue.append([node, val])
        _logger.warning("Python: New data change event %s %s", node, val)

    def event_notification(self, event):
        _logger.warning("Python: New event %s", event)

    async def executeQueueCmd(self):
        while len(self.cmdQueue) > 0:
            node, val = self.cmdQueue.pop()
            name = node.get_browse_name().Name
            print(f'Execute Datacenter cmd: node {name} -> {val}')
            UNITY_SERVER_NODES[name].set_value(val)


class ClientSubHandler(object):

    """
   Subscription Handler. To receive events from server for a subscription
   DO NOT PUT LENGTHY FUNCTION CALL RUN HERE, IT WON'T WORK
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


    def datachange_notification(self, node:opcua.Node, val, data):
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
        self.cmdQueue.append([node, val])
            # self.subscriptionDict[node.nodeid.to_string()].set_value(val)
        # print(node.nodeid.to_string())
        # print(self.subscriptionDict)
        _logger.warning("Python: New data change event %s %s", node, val)

    def event_notification(self, event):
        _logger.warning("Python: New event %s", event)

    async def executeQueueCmd(self):
        while len(self.cmdQueue) > 0:
                node, val = self.cmdQueue.pop()
                name = node.get_browse_name().Name
                print(f'Execute cmd: node {name} -> {val}')
                if name == "datacenterUnity":
                    serverNode = self.subscriptionDict["datacenterUnity"]
                    serverNode.set_value(val)
                elif self.subscriptionDict[node.nodeid.to_string()] is not None:
                    datacenterNode = self.subscriptionDict[node.nodeid.to_string()]
                    datacenterNode.set_value(val)



serverURL = f'opc.tcp://172.18.200.5:4841'
Snamespace = "https://robotarm.opcua.io"

dataCenterURL = f'opc.tcp://{IPAddr}:4840'
DCnamespace = "https://datacenter.opcua.io"

async def main():
    global DATACENTER_SUBSCRIPTION_LIST

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
        def caller(parent, *inputArg):
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
            return client.nodes.objects.call_method(methodNode, *inputArg)

        return caller

    def browseNode(datacenterParentNode: opcua.Node, nodes : list[opcua.Node], migrate: bool, subhandler: ClientSubHandler):
        """
        Ham brosweNode se:
            broswe cac Node trong Server, trich xuat cac thong tin nhu
                name: ten node
                nodeID: ns=x;i=y
                nodeClass: Variable, Object,...
                value: gia tri cua Node. mot so Node khong co value nhu Object Node
            Khi migrate = True, can truyen them tham so subhandler
            Khi nay, ham se co "copy", tao ra cac node va method giong nhu node ben server
            dong thoi tu dong subscribe vao cac node ben server de cap nhat khi co su thay doi
        async browseNode(
            datacenterParentNode: specify the node of datacenter which we need to "append" the browsing result to
            nodes: list of node from the server that Datacenter is connected to, and start browsing them
            migrate: "copy" the node from the server and create them in Datacenter (True/False)
            subhandler: an object of subhandler.
        )
        """
        global UNITY_SERVER_NODES, DATACENTER_SUBSCRIPTION_LIST
        methodArgs = list()
        for node in nodes:
            value = 0
            datacenterNode = None
            try:
                nodeClass = (node.get_node_class()).name
                name = (node.get_browse_name()).Name
                nodeID = node.nodeid.to_string()

                # check Class of the Node and perform needed action
                if nodeClass == "Variable":
                    value = node.get_value()
                    variantType = node.get_data_type_as_variant_type()
                    if migrate:
                        if name == "unity":
                            name = f"datacenterUnity_{len(UNITY_SERVER_NODES)}"
                        datacenterNode = datacenterParentNode.add_variable(idx, name, value, varianttype=variantType) if (datacenterParentNode is not None) else None
                        subhandler.subscriptionDict[nodeID] = datacenterNode
                        subhandler.subscriptionList.append(node)
                        if name == f"datacenterUnity_{len(UNITY_SERVER_NODES)}":
                            # trong truong hop datacenter, minh cung muon thay doi gia tri cua node datacenterUnity nay
                            # va ghi nguoc lai server. de ghi nguoc lai server, minh can luu node cua server [node]
                            # va subscribe node datacenterUnity nay. (nguoc voi ben tren)
                            # ta co 1 dict Item: {"datacenterUnity_x" : server Unity node}
                            UNITY_SERVER_NODES[name] = node
                            DATACENTER_SUBSCRIPTION_LIST.append(datacenterNode)
                        accessLevel = node.get_access_level()
                        try:
                            datacenterNode.set_writable(ua.AccessLevel.CurrentWrite in accessLevel)
                        except:
                            pass
                elif nodeClass == "Object":
                    nodeClassRefs = node.get_references(40) #reference 40 la reference toi: "HasTypeDefinition",
                    # giup minh xem duoc ro rang hon Folder type
                    nodeClass = nodeClassRefs[0].BrowseName.Name
                    if nodeClass == "FolderType":
                        if migrate:
                            datacenterNode = datacenterParentNode.add_folder(idx, name) if (datacenterParentNode is not None) else None
                            subhandler.subscriptionDict[nodeID] = datacenterNode
                            subhandler.subscriptionList.append(node)
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
                # methodArgs is a list, and this will be return back to create new method
                if name == "InputArguments" or name == "OutputArguments":
                    methodArgs.append(value)

                # after getting the info of current node, continue to browse its children (if exist)
                children = node.get_children()
                if children is not None:
                    # in case of Method, we need the input and output argument info. but these
                    # argument is actually the children of the method node, so we have to
                    # browse these children and return back to create Method.
                    # browseNode function can know if the node it's browsing is an input/output argument
                    # of a method or not, and return these argument.
                    if nodeClass == "Method":
                        inoutArgs = browseNode(datacenterNode, children, migrate, subhandler)
                        inArgs = inoutArgs[0]
                        inArgsFunc = list()
                        for inArg in inArgs:
                            uaArg = ua.Argument()
                            uaArg.Name = inArg.Name
                            uaArg.DataType = inArg.DataType
                            uaArg.ValueRank = inArg.ValueRank
                            uaArg.ArrayDimensions = inArg.ArrayDimensions
                            uaArg.Description = inArg.Description
                            inArgsFunc.append(uaArg)
                        outArgs = inoutArgs[1]
                        outArgsFunc = list()
                        for outArg in outArgs:
                            uaArg = ua.Argument()
                            uaArg.Name = outArg.Name
                            uaArg.DataType = outArg.DataType
                            uaArg.ValueRank = outArg.ValueRank
                            uaArg.ArrayDimensions = outArg.ArrayDimensions
                            uaArg.Description = outArg.Description
                            outArgsFunc.append(uaArg)
                        if migrate:
                            methodFunc = functionWrapper(client, nodeID)
                            functionWrapperList.append(methodFunc)
                            method = datacenterParentNode.add_method(idx, name, methodFunc, inArgsFunc, outArgsFunc)
                            subhandler.subscriptionDict[nodeID] = method
                    else:
                        browseNode(datacenterNode, children, migrate, subhandler)
            except Exception as e:
                print(f'Can\'t read node {node} at {node.nodeid.to_string()}: {e}')
        return methodArgs

    """
    ================================= SERVER (DATACENTER) SECTION ====================================
    """
    server = Server()

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

    # setup our namespace. An endpoint can have multiple namespace!
    idx = server.register_namespace(DCnamespace)
    server.start()
    print(f'OPC datacenter running at {server.endpoint[0]}://{server.endpoint[1]}')
    serverHandler = ServerSubHandler()
    # subscription chi create duoc sau khi server start.
    serverSubscription = server.create_subscription(1, serverHandler)

    """
    ================================= /SERVER (DATACENTER) SECTION ====================================
    """

    """
    ================================= CLIENT SECTION ====================================
    """
    client = Client(serverURL)
    client.connect()
    print(f"Connected to {serverURL} ...")

    # Find the namespace index
    # nsidx = client.get_namespace_index(namespace)
    # print(f"Namespace Index for '{namespace}': {nsidx}")
    listOfNode = client.nodes.objects.get_children()
    # print(listOfNode)
    listOfMainNode = listOfNode[1:]
    # aNode = listOfMainNode[0]
    # print(aNode, type(aNode), aNode.get_browse_name())

    # each client will have 1 sub handler
    clientHandler = ClientSubHandler()
    clientSubscription = client.create_subscription(1, clientHandler)
    browseNode(server.nodes.objects, listOfMainNode, True, clientHandler)
    clientSubscription.subscribe_data_change(clientHandler.subscriptionList)

    """
    ================================= /CLIENT SECTION ====================================
    """

    # wait until client browse all the nodes from server, and then we will have node to subcribe to :'(
    print(DATACENTER_SUBSCRIPTION_LIST)
    serverSubscription.subscribe_data_change(DATACENTER_SUBSCRIPTION_LIST)

    async def serverConnect():
        while True:
            await serverHandler.executeQueueCmd()
            await asyncio.sleep(0.005)

    async def clientConnect():
        while True:
            await clientHandler.executeQueueCmd()
            await asyncio.sleep(0.001)

    await asyncio.gather(serverConnect(), clientConnect())
    server.stop()
    client.disconnect()

if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())