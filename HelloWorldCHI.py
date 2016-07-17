# coding=utf-8

import CommunicationHandlerInterface
from DataTypes.InstallInfo import InstallInfo


class HelloWorld(CommunicationHandlerInterface.CommunicationHandlerInterface):
    def getServiceName(self):
        return "HelloWorldCHI"

    def getServiceVersion(self):
        return 0.1

    def getInstallID(self):
        return '1041053949'

    def onInstall(self, id):
        pass;

    def onEnable(self):
        pass

    def getInstallInfo(self):
        info = InstallInfo()
        info.name = 'HelloWorldCHI'
        info.title = 'Hello World'
        return info.toJSON()

    def onConnect(self):
        # self.sm.communication.runCommand("turnoff", json.dumps({'id': 12}))
        pass

    def onError(self, node, id, description):
        pass

    def pong(self, id, miliseconds):
        self.sm.send(
            '{"type" : "internal" , "node" : "ping" , "name" : "' + self.getServiceName() +
            '" , "version" : "5"'
            + ((' , "id" : "' + self.getInstallID() + '"') if len(id) > 0  else "") + "}")
