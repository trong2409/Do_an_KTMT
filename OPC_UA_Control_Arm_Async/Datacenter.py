import asyncua
from asyncua import ua, uamethod, Client, Server
import asyncio
import socket
import logging

_logger = logging.getLogger(__name__)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

class SubHandler(object):

    """
   Subscription Handler. To receive events from server for a subscription
   """

    def __init__(self):
        # a dictionary contain Datacenter nodes
        self.subscriptionDict = dict()
        # a list contain all server nodes that need to subscribe to
        self.subscriptionList = list()
        # a queue
        self.cmdQueue = list()


    def datachange_notification(self, node:asyncua.Node, val, data):
        if self.subscriptionDict[node.nodeid.to_string()] is not None:
            self.cmdQueue.append([node.nodeid.to_string(), val])
            # await self.subscriptionDict[node.nodeid.to_string()].set_value(val)
        # print(node.nodeid.to_string())
        # print(self.subscriptionDict)
        _logger.warning("Python: New data change event %s %s", node, val)

    def event_notification(self, event):
        _logger.warning("Python: New event %s", event)


serverURL = f'opc.tcp://{IPAddr}:4841'
Snamespace = "https://robotarm.opcua.io"

dataCenterURL = f'opc.tcp://{IPAddr}:4840'
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
        tclient = input_args[0]
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
            return await client.nodes.objects.call_method(methodNode, *inputArg)

        return caller

    @uamethod
    def func(parent, *args):
        print(args)
        return args

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

    # setup our namespace. An endpoint can have multiple namespace!
    idx = await server.register_namespace(DCnamespace)
    functionWrapperList = list()

    client = Client(serverURL)

    async def browseNode(datacenterParentNode: asyncua.Node, nodes : list[asyncua.Node], migrate: bool, subhandler: SubHandler):
        """
        async browseNode(
            datacenterParentNode: specify the node of datacenter which we need to "append" the browsing result to
            nodes: list of node from the server that Datacenter is connected to, and start browsing them
            migrate: "copy" the node from the server and create them in Datacenter (True/False)
        )
        """
        methodArgs = list()
        for node in nodes:
            value = 0
            datacenterNode = None
            try:
                nodeClass = (await node.read_node_class()).name
                name = (await node.read_browse_name()).Name
                nodeID = node.nodeid.to_string()

                # check Class of the Node and perform needed action
                if nodeClass == "Variable":
                    value = await node.get_value()
                    if migrate:
                        datacenterNode = await datacenterParentNode.add_variable(idx, name, value) if (datacenterParentNode is not None) else None
                        subhandler.subscriptionDict[nodeID] = datacenterNode
                        subhandler.subscriptionList.append(node)
                elif nodeClass == "Object":
                    nodeClassRefs = await node.get_references(40) #reference 40 la reference toi: "HasTypeDefinition",
                    # giup minh xem duoc ro rang hon Folder type
                    nodeClass = nodeClassRefs[0].BrowseName.Name
                    if nodeClass == "FolderType":
                        if migrate:
                            datacenterNode = await datacenterParentNode.add_folder(idx, name) if (datacenterParentNode is not None) else None
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
                children = await node.get_children()
                if children is not None:
                    # in case of Method, we need the input and output argument info. but these
                    # argument is actually the children of the method node, so we have to
                    # browse these children and get their info, so that we can make method.
                    # to do that, we will need to get result return back from browseNode()
                    # browseNode function can know if the node it's browsing is an input/output argument
                    # of a method or not, and return these argument.
                    if nodeClass == "Method":
                        inoutArgs = await browseNode(datacenterNode, children, migrate, subhandler)
                        inArgs = inoutArgs[0]
                        inArgsFunc = list()
                        for inArg in inArgs:
                            inArgsFunc.append(ua.Argument(
                                Name = inArg.Name,
                                DataType = inArg.DataType,
                                ValueRank = inArg.ValueRank,
                                ArrayDimensions= inArg.ArrayDimensions,
                                Description= inArg.Description
                            ))
                        outArgs = inoutArgs[1]
                        outArgsFunc = list()
                        for outArg in outArgs:
                            outArgsFunc.append(ua.Argument(
                                Name=outArg.Name,
                                DataType=outArg.DataType,
                                ValueRank=outArg.ValueRank,
                                ArrayDimensions=outArg.ArrayDimensions,
                                Description=outArg.Description
                            ))
                        if migrate:
                            methodFunc = functionWrapper(client, nodeID)
                            functionWrapperList.append(methodFunc)
                            method = await datacenterParentNode.add_method(idx, name, methodFunc, inArgsFunc, outArgsFunc)
                            subhandler.subscriptionDict[nodeID] = method
                    else:
                        await browseNode(datacenterNode, children, migrate, subhandler)
            except Exception as e:
                print(f'Can\'t read node {node} at {node.nodeid.to_string()}: {e}')
        return methodArgs

    async def executeQueueCmd(handler: SubHandler):
        while len(handler.cmdQueue) > 0:
                nodeID, val = handler.cmdQueue.pop()
                await handler.subscriptionDict[nodeID].set_value(val)

    async def serverConnect():
        async with server:
            print(await server.get_endpoints())
            while True:
                await asyncio.sleep(0.0001)

    async def clientConnet():
        print(f"Connecting to {serverURL} ...")
        # replace client = Client(serverURL); await client.connect()
        async with client:
            # Find the namespace index
            # nsidx = await client.get_namespace_index(namespace)
            # print(f"Namespace Index for '{namespace}': {nsidx}")
            listOfNode = await client.nodes.objects.get_children()
            # print(listOfNode)
            listOfMainNode = listOfNode[2:]
            # print(folderNode)
            # childFolderNode = await folderNode.get_children()
            # print(childFolderNode)
            # testNode = childFolderNode[0]
            # print(testNode)
            # # A variable Node info
            # print(await testNode.get_value())
            # print(await testNode.get_path())
            # ID = await testNode.read_browse_name()
            # print(ID, ID.Name, ID.NamespaceIndex)
            # nodeClass = await testNode.read_node_class()
            # print(nodeClass, nodeClass.name)
            handler = SubHandler()
            subscription = await client.create_subscription(10, handler)
            await browseNode(server.nodes.objects, listOfMainNode, True, handler)
            await subscription.subscribe_data_change(handler.subscriptionList)
            while True:
                await executeQueueCmd(handler)
                await asyncio.sleep(0.001)

    await asyncio.gather(serverConnect(), clientConnet())


if __name__ == "__main__":
    asyncio.run(main())