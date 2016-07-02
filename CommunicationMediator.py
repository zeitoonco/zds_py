# coding=utf-8
from collections import namedtuple
import json

from Utility.Communication import Communication


class CommunicationMediator:
    sm = None
    idData = namedtuple("idData", "data set isException")

    idList = {}
    MtxIdList = None

    def __init__(self, ism):
        self.sm = ism

    def run_command(self, name, data, cid=None, session=None):
        self.sm.send(Communication.make_command(name, cid, self.sm.owner.getServiceName(), data, session))

    def run_command_sync(self, name, data, cid=None, session=None):
        self.sm.send(Communication.make_command(name, id, self.sm.owner.getServiceName(), data, session))
        x = self.idData("", False)
        dt = ''
        return dt

    def run_callback(self, name, data, id):
        self.sm.send(Communication.make_callback(name, id, self.sm.owner.getServiceName(), data))

    def run_event(self, name, data):
        self.sm.send(Communication.make_event(name, self.sm.owner.getServiceName(), data))

    def register_event(self, name):
        self.sm.send(Communication.make_command("_core.registerEvent", "", self.sm.owner.getServiceName(),
                                                      "{\"names\" : [" + name + "]}"))

    def remove_event(self, name):
        self.sm.send(Communication.make_command("_core.removeEvent", "", self.sm.owner.getServiceName(),
                                                      "{\"names\" : [" + name + "]}"))

    def register_command(self, name):
        self.sm.send(Communication.make_command("_core.registerCommand", "", self.sm.owner.getServiceName(),
                                                      "{\"names\" : [" + name + "]}"))

    def remove_command(self, name):
        self.sm.send(Communication.make_command("_core.removeCommand", "", self.sm.owner.getServiceName(),
                                                      "{\"names\" : [" + name + "]}"))

    def register_hook(self, name, session=""):
        self.sm.send(Communication.make_command("_core.registerHook", "", self.sm.owner.getServiceName(),
                                                      "{\"names\" : [" + name + "]}"))

    def remove_hook(self, name):
        self.sm.send(Communication.make_command("_core.registerHook", "", self.sm.owner.getServiceName(),
                                                      "{\"names\" : [" + name + "]}"))

    def error_report(self, node, id, desc):
        self.sm.send(Communication.make_error(node, id, desc))

    def data_receive(self, data):
        js = json.loads(data)
        id = None
        dt = None

        id = js["id"]
        dt = js["data"]

        if id == self.idList.keys()[-1]:
            return False
        x = self.idData(self.idList[id])
        x.data = dt
        x.set = True
        return True

    def error_receive(self, data):
        js = json.loads(data)
        id = None
        dt = None
        id = js["id"]
        dt = js["data"]["description"]

        if id == self.idList.keys()[-1]:
            return False
        x = self.idData(self.idList[id])
        x.data = dt
        x.set = True
        x.isException = True
        return True

    @staticmethod
    def get_name_and_type():
        return "CommunicationMediator"
