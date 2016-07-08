# coding=utf-8

import CommunicationHandlerInterface
from DataTypes.InstallInfo import InstallInfo
from Utility.Communication import Communication


class HelloWorld(CommunicationHandlerInterface.CommunicationHandlerInterface):
    def getServiceName(self):
        return "HelloWorldCHI"

    def getServiceVersion(self):
        return 0.1

    def getInstallID(self):
        return '23'

    def getInstallInfo(self):
        info = InstallInfo()
        info.name = 'helloworld'
        info.title = 'Hello World'
        return info.toJSON()

    def onConnect(self):
        # self.sm.communication.runCommand("turnoff", json.dumps({'id': 12}))
        pass

    def pong(self, id, miliseconds):
        self.sm.send(
            '{"type" : "internal" , "node" : "ping" , "name" : "' + self.getServiceName() +
            '" , "version" : "5"'
            + (' , "id" : "' + self.getInstallID() + '"' if len(id) > 0  else "") + "}")
