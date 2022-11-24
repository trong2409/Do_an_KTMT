from opcua import ua, uamethod, Server, Client

@uamethod
def get_server_value(parent, index):
    # DataCenter get data from Server
    global dataNode
    # dataNode = client.get_node("ns=2;i=2")
    try:
        data = dataNode[index].get_value()
    except:
        data = "99"
    return data

dataNode = list()

if __name__ == "__main__":
    # # # ============ client =====================
    server_url = "opc.tcp://10.230.219.253:4840"
    client = Client(server_url)
    client.connect()
    print(f'DataCenter connected to {server_url}')
    print('==========================================')

    for i in range(0, 9):
        dataNode.append(client.get_node(f"ns=2;i={i+2}"))

    print(f'All nodes get successfully')
    print('==========================================')

    # ============ server =====================
    server = Server()
    url = "opc.tcp://10.230.219.253:4840"
    server.set_endpoint(url)

    name = "OPCUA_SIMUALTION_SERVER"
    addspace = server.register_namespace(name)
    node = server.get_objects_node()

    # create a object for getVal and setVal method
    method_object = node.add_object(addspace, "MethodObject")
    # add methods to created object
    getval = method_object.add_method(addspace, "getSerVal", get_server_value, [ua.VariantType.UInt16], [ua.VariantType.String])
    # setval = method_object.add_method(addspace, "setSerVal", get_server_value, [ua.VariantType.String], [ua.VariantType.Int64])

    # Start server
    server.start()
    print("DataCentre started at {}".format(url))

    try:
        while True:
            pass
        # embed()
    finally:
        server.stop()
