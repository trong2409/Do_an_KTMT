from opcua import ua, uamethod, Server, Client

# @uamethod
# def get_server_value(parent):
#     # DataCenter get data from Server
#     global client
#     dataNode = client.get_node("ns=2;i=2")
#     data = dataNode.get_value()
#     return data



@uamethod
def set_server_value(parent, dataIn):
    # DataCenter set value to Server
    global dataNode

    dataNode.set_value(dataIn)
    data = dataNode.get_value()

    return data
    # return [ua.Variant(0, ua.VariantType.Int64)]


if __name__ == "__main__":
    # ============ client =====================
    server_url = "opc.tcp://192.168.0.101:4840"
    client = Client(server_url)
    client.connect()
    print(f'DataCenter connected to {server_url}')
    print('==========================================')

    dataNode = client.get_node("ns=2;i=2")

    # ============ server =====================
    server = Server()
    url = "opc.tcp://192.168.0.115:4840"
    server.set_endpoint(url)

    name = "OPCUA_SIMUALTION_SERVER"
    addspace = server.register_namespace(name)
    node = server.get_objects_node()

    # create a object for getVal and setVal method
    method_object = node.add_object(addspace,"MethodObject")
    # add methods to created object
    # getval = method_object.add_method(addspace, "getSerVal", get_server_value, [ua.VariantType.Int64])
    setval = method_object.add_method(addspace, "setSerVal", set_server_value, [ua.VariantType.String], [ua.VariantType.Int64])

    # Start server
    server.start()
    print("DataCentre started at {}".format(url))

    try:
        while True:
            pass
        # embed()
    finally:
        server.stop()