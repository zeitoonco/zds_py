# coding=utf-8
import json
import logging
import time

from ServerMediator import ServerMediator
from Utility.Communication import Communication


class CommunicationHandlerInterface:
    logger = logging.getLogger('CommunicationHandlerInterface')

    pingtimes = {}
    sm = None  # type: ServerMediator

    def __init__(self, sm):
        self.sm = ServerMediator(self)

    def ping(self, _id=""):
        if len(_id) == 0:
            _id = Communication.get_random_id()
        self.pingtimes['id'] = time.time()
        self.sm.send('{"type" : "internal" , "node" : "ping" , "id" : "' + _id + '"}')
        return _id

    def onCommand(self, node, data, _id, _from):
        raise NotImplementedError()

    def onCallback(self, node, data, id, _from):
        raise NotImplementedError()

    def onEvent(self, node, data, _from):
        raise NotImplementedError()

    def onInstall(self, id):
        raise NotImplementedError()

    def onEnable(self):
        raise NotImplementedError()

    def onDisable(self):
        raise NotImplementedError()

    def onUninstall(self):
        raise NotImplementedError()

    def onConnect(self):
        pass

    def onDisconnect(self):
        pass

    def getInstallInfo(self):
        raise NotImplementedError()

    def getInstallID(self):
        raise NotImplementedError()

    def getServiceName(self):
        raise NotImplementedError()

    def getServiceVersion(self):
        raise NotImplementedError()

    def changeDatatypeVersion(self, value, datatype, fromVersion, toVersion, newVersion):
        raise NotImplementedError()

    def onError(self, node, id, description):
        raise NotImplementedError()

    def onWarning(self, level, node, id, description):
        raise NotImplementedError()

    def pong(self, id, miliseconds):
        raise NotImplementedError()

    def datareceive(self, data):
        js = json.loads(data)  # todo:dont parse data field
        type = str(js["type"])
        node = str(js["node"])
        if type.lower() == "internal".lower():
            if node.lower() == "pong".lower():
                id = js["node"]
                t = time.time()
                d = t - self.pingtimes[id]
                del self.pingtimes[id]
                self.pong(id, d.count())
            elif node.lower() == "hello".lower():
                id = self.getInstallID()
                self.sm.send(
                    '{"type" : "internal" , "node" : "hello" , "name" : "' + str(self.getServiceName()) +
                    '" , "version" : ' + str(self.getServiceVersion()) +
                    (' , "id" : "' + (str(id) + '"') if len(id) > 0 else "") + "}")

        else:
            dataj = js["data"] if 'data' in js else ""
            fromj = js["from"] if 'from' in js else ""
            idj = js["id"] if 'id' in js else ""
            data = "" if dataj is None else dataj
            _from = "" if fromj is None else fromj
            id = "" if idj is None else  idj
            if type == "fire":  # communication
                self.onEvent(node, data, _from)
            elif type == "callback":
                self.onCallback(node, data, id, _from)
            elif type == "call":  # communication
                if node == "onInstall":
                    if dataj is '':
                        raise ValueError("onInstall: Data field is empty!")

                    self.onInstall(dataj['id'])
                    # todo: receive a bool, that shows if install process was successful, for next line
                    time.sleep(0.2)
                    self.sm.send(
                        Communication.make_callback("onInstall", '{"success":true}', id, self.getServiceName()))
                elif node.lower() == "onUninstall".lower():
                    self.onUninstall()
                elif node.lower() == "onEnable".lower():
                    self.onEnable()
                    # todo: receive a bool, that shows if install process was successful, for next line
                    time.sleep(0.2)
                    self.sm.send(Communication.make_callback("onEnable", '{"success":true}', id, self.getServiceName()))
                elif node.lower() == "onDisable".lower():
                    self.onDisable()
                elif node.lower() == "error".lower():
                    if dataj is '':
                        raise ValueError("onInstall: Data field is empty!")

                    self.onError(dataj["node"], dataj["id"], dataj["description"])
                elif node.lower() == "warning".lower():
                    if dataj is '':
                        raise ValueError("onInstall: Data field is empty!")

                    self.onWarning(dataj["level"], dataj["node"], dataj["id"],
                                   dataj["description"])
                elif node.lower() == "getInstallInfo".lower():
                    self.sm.send(
                        Communication.make_callback("getInstallInfo", self.getInstallInfo(), id, self.getServiceName()))
                elif node.lower() == "changeDatatypeVersion".lower():
                    if dataj is '':
                        raise ValueError("onInstall: Data field is empty!")

                    newVer = 0
                    newdata = self.changeDatatypeVersion(dataj["value"], dataj["datatype"], dataj["fromversion"], dataj[
                        "toversion"], newVer)

                    self.sm.send(Communication.make_callback("changeDatatypeVersion", id, self.getServiceName(),
                                                             '{ "datatype" : "' + dataj["datatype"] +
                                                             '" , "newversion" : "' + str(newVer)
                                                             + '" , "value" : ' + newdata + "}"
                                                             ))
                else:
                    self.onCommand(node, data, id, _from)
        return False

    def connect(self, server_ip, server_port):
        self.sm.connect(server_ip, server_port)

    @staticmethod
    def getNameAndType():
        return "CommunicationHandlerInterface"
