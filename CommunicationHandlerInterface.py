# coding=utf-8
import json
import time

import ServerMediator
from Utility.Communication import Communication

from twisted.internet.protocol import Protocol, ReconnectingClientFactory

class CommunicationHandlerInterface:
    pingtimes = {}
    sm = None  # type: ServerMediator

    def __init__(self, sm):
        self.sm = ServerMediator.ServerMediator(self)

    def ping(self, _id=""):
        if len(_id) == 0:
            _id = Communication.get_random_id()
        self.pingtimes['id'] = time.time()
        self.sm.send('{"type" : "internal" , "node" : "ping" , "id" : "' + _id + '"}')
        return _id

    def on_command(self, node, data, id, _from):
        raise NotImplementedError()

    def on_callback(self, node, data, id, _from):
        raise NotImplementedError()

    def on_event(self, node, data, _from):
        raise NotImplementedError()

    def on_install(self, id):
        raise NotImplementedError()

    def on_enable(self):
        raise NotImplementedError()

    def on_disable(self):
        raise NotImplementedError()

    def on_uninstall(self):
        raise NotImplementedError()

    def on_connect(self):
        raise NotImplementedError()

    def on_disconnect(self):
        raise NotImplementedError()

    def get_install_info(self):
        raise NotImplementedError()

    def get_install_id(self):
        raise NotImplementedError()

    def get_service_name(self):
        raise NotImplementedError()

    def get_service_version(self):
        raise NotImplementedError()

    def change_vatatype_version(self, value, datatype, fromVersion, toVersion, newVersion):
        raise NotImplementedError()

    def on_error(self, node, id, description):
        raise NotImplementedError()

    def on_warning(self, level, node, id, description):
        raise NotImplementedError()

    def pong(self, id, miliseconds):
        raise NotImplementedError()

    def data_receive(self, data):
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
                id = self.get_install_id()
                self.sm.send(
                    '{"type" : "internal" , "node" : "hello" , "name" : "' + self.get_service_name() +
                    '" , "version" : ' + self.get_service_version() + (
                        ' , "id" : "' + id + '"' if id.length() > 0 else "") + "}")

        else:
            dataj = js["data"]
            fromj = js["from"]
            idj = js["id"]
            data = "" if dataj is None else dataj
            _from = "" if fromj is None else fromj
            id = "" if idj is None else  idj
            if type == "fire":  # communication
                self.on_event(node, data, _from)
            elif type == "callback":
                self.on_callback(node, data, id, _from)
            elif type == "call":  # communication
                if node == "onInstall":
                    if dataj is '':
                        raise ValueError("onInstall: Data field is empty!")

                    self.on_install(dataj["id"])
                    # todo: receive a bool, that shows if install process was successful, for next line
                    time.sleep(0.2)
                    self.sm.send(
                        Communication.make_callback("onInstall", id, self.get_service_name(), '{"success":true}'))
            elif node.lower() == "onUninstall".lower():
                self.on_uninstall()
            elif node.lower() == "onEnable".lower():
                self.on_enable()
                # todo: receive a bool, that shows if install process was successful, for next line
                time.sleep(0.2)
                self.sm.send(Communication.make_callback("onEnable", id, self.get_service_name(), "{\"success\":true}"))
            elif node.lower() == "onDisable".lower():
                self.on_disable()
            elif node.lower() == "error".lower():
                if dataj is '':
                    raise ValueError("onInstall: Data field is empty!")

                self.on_error(dataj["node"], dataj["id"], dataj["description"])
            elif node.lower() == "warning".lower():
                if dataj is '':
                    raise ValueError("onInstall: Data field is empty!")

                self.on_warning(dataj["level"], dataj["node"], dataj["id"],
                                dataj["description"])
            elif node.lower() == "getInstallInfo".lower():
                self.sm.send(Communication.make_callback("getInstallInfo", id, self.get_service_name(),
                                                         self.get_install_info()))
            elif node.lower() == "changeDatatypeVersion".lower():
                if dataj is '':
                    raise ValueError("onInstall: Data field is empty!")

                newVer = 0
                newdata = self.change_vatatype_version(dataj["value"], dataj["datatype"], dataj["fromversion"], dataj[
                    "toversion"], newVer)

                self.sm.send(Communication.make_callback("changeDatatypeVersion", id, self.get_service_name(),
                                                         '{ "datatype" : "' + dataj["datatype"] +
                                                         '" , "newversion" : "' + str(newVer)
                                                         + '" , "value" : ' + newdata + "}"
                                                         ))
            else:
                self.on_command(node, data, id, _from)
                return False

    def connect(self, server_ip, server_port):
        self.sm.connect(server_ip, server_port)

    @staticmethod
    def get_name_and_type():
        return "CommunicationHandlerInterface"
