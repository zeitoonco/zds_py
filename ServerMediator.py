# coding=utf-8
import json

from Utility.Communication import Communication
from Utility.TCPClient import TCPClient


class ServerMediator:
    owner = None
    tcpc = None  # type: TCPClient
    communication = None
    setting = None
    database = None

    def on_net_connect(self):
        pass

    def on_net_disconnect(self):
        pass

    def __init__(self, chi):
        self.owner = chi
        self.tcpc = TCPClient()
        self.tcpc.registerOnMessageCallBack(self.data_received)
        self.tcpc.registerOnClientConnectCallBack(self.on_net_connect())
        self.tcpc.registerOnClientDisconnectCallBack(self.on_net_disconnect())

    def connect(self, address=None, port=None):
        self.tcpc.connect(address, port)
        self.tcpc.run()

    def disconnect(self):
        self.tcpc.disconnect()

    def is_connected(self):
        return self.tcpc.isConnected()

    def data_received(self, data):
        js = json.loads(data)

        type = js["type"]

        node = js["node"]
        # todo: if type call & & node error -> > errReceived()
        if type == "internal" and node == "ping":
            self.send('{"type" : "internal" , "node" : "pong" , "id" : "' + js["id"] + '"}')
        else:
            if type == "callback":
                if self.communication.dataReceive(data):
                    return
        if type == "call" and node == "error":  # TODO: Check
            if self.communication.errorReceive(data):
                return
        self.owner.datareceive(data)

    def send_cmd(self, node, id, data):
        self.send(Communication.make_command(node, id, self.get_service_name(), data))

    def send(self, data):
        self.tcpc.send(data)

    def join_net(self):
        self.tcpc.joinOnConnectionThread()

    @staticmethod
    def get_name_and_type():
        return "ServerMediator"

    def get_service_name(self):
        raise NotImplementedError
