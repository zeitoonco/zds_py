# coding=utf-8
import json
import logging

from CommunicationMediator import CommunicationMediator
from DatabaseMediator import DatabaseMediator
from SettingMediator import SettingMediator
from Utility.Communication import Communication
from Utility.TCPClient import TCPClient


class ServerMediator:
    owner = None  # type: CommunicationHandlerInterface
    tcpc = None  # type: TCPClient
    communication = None  # type: CommunicationMediator
    setting = None  # type: SettingMediator
    database = None  # type: DatabaseMediator

    logger = logging.getLogger('ServerMediator')

    def onNetConnect(self):
        self.owner.onConnect()

    def onNetDisconnect(self):
        self.owner.onDisconnect()

    def __init__(self, chi):
        self.owner = chi
        self.communication = CommunicationMediator(self)
        self.setting = SettingMediator(self)
        self.database = DatabaseMediator(self)
        self.tcpc = TCPClient()
        self.tcpc.registerOnMessageCallBack(self.dataReceived)
        self.tcpc.registerOnClientConnectCallBack(self.onNetConnect)
        self.tcpc.registerOnClientDisconnectCallBack(self.onNetDisconnect)

    def connect(self, address=None, port=None):
        self.tcpc.Connect(address, port)
        self.tcpc.Run()

    def disconnect(self):
        self.tcpc.Disconnect()

    def isConnected(self):
        return self.tcpc.isConnected()

    def dataReceived(self, data):
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
        self.send(Communication.make_command(node, id, self.getServiceName(), data))

    def send(self, data):
        self.tcpc.send(data)

    def joinNet(self):
        self.tcpc.Join()

    @staticmethod
    def getNameAndType():
        return "ServerMediator"

    def getServiceName(self):
        raise NotImplementedError
