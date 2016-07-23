# coding=utf-8
import json
import logging
import time
from collections import namedtuple

from Utility.Communication import Communication


class CommunicationMediator:
    sm = None  # type: ServerMediator
    idData = namedtuple("idData", "data set isException")

    idList = {}
    MtxIdList = None
    logger = logging.getLogger('CommunicationMediator')

    def __init__(self, ism):
        self.sm = ism

    def runCommand(self, name, data, cid='', session=''):
        self.sm.send(Communication.make_command(node=name, _id=cid, _from=self.sm.owner.getServiceName(), data=data,
                                                session=session))

    def runCommandSync(self, name, data, cid='', session=''):
        self.sm.send(Communication.make_command(node=name, _id=cid, _from=self.sm.owner.getServiceName(), data=data,
                                                session=session))
        x = self.idData(cid, False, False)
        cid = str(cid)
        self.idList[cid] = x

        while self.idList[cid].set is False:
            # todo: put a timeout   for commands
            time.sleep(0.030)
        dt = self.idList[cid].data
        if self.idList[cid].isException:
            raise "Error received from Core: " + dt
        del self.idList[cid]
        return dt

    def runCallback(self, name, data, id):
        self.sm.send(Communication.make_callback(node=name, _id=id, _from=self.sm.owner.getServiceName(), data=data))

    def runEvent(self, name, data):
        self.sm.send(Communication.make_event(name, self.sm.owner.getServiceName(), data))

    def registerEvent(self, name):
        self.sm.send(
            Communication.make_command("_core.registerEvent", _id="", _from=self.sm.owner.getServiceName(), data=
            '{"names" : [' + name + "]}"))

    def removeEvent(self, name):
        self.sm.send(Communication.make_command("_core.removeEvent", "", self.sm.owner.getServiceName(),
                                                '{"names" : [' + name + "]}"))

    def registerCommand(self, name):
        self.sm.send(Communication.make_command("_core.registerCommand", "", self.sm.owner.getServiceName(),
                                                '{"names" : [' + name + "]}"))

    def removeCommand(self, name):
        self.sm.send(Communication.make_command("_core.removeCommand", "", self.sm.owner.getServiceName(),
                                                '{"names" : [' + name + "]}"))

    def registerHook(self, name, session=""):
        self.sm.send(Communication.make_command("_core.registerHook", "", self.sm.owner.getServiceName(),
                                                '{"names" : [' + name + "]}"))

    def removeHook(self, name):
        self.sm.send(Communication.make_command("_core.registerHook", "", self.sm.owner.getServiceName(),
                                                '{"names" : [' + name + "]}"))

    def errorReport(self, node, id, desc):
        self.sm.send(Communication.make_error(node, id, desc))

    def dataReceive(self, data):
        js = json.loads(data)
        try:
            id = str(js["id"])
            dt = js["data"]
        except:
            return False
        if id not in self.idList:
            return False

        x = self.idData(dt, True, False)
        self.idList[id] = x
        return True

    def errorReceive(self, data):
        js = json.loads(data)

        try:
            id = str(js["data"]["id"])
            dt = js["data"]["description"]
        except:
            return False
        if id not in self.idList:
            return False

        x = self.idData(dt, True, True)
        self.idList[id] = x
        return True

    @staticmethod
    def getNameAndType():
        return "CommunicationMediator"
