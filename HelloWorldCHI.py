# coding=utf-8
import json
import logging
import os

import CommunicationHandlerInterface
from DataTypes.InstallInfo import InstallInfo
from Utility.Communication import Communication


class HelloWorld(CommunicationHandlerInterface.CommunicationHandlerInterface):
    logger = logging.getLogger('HelloWorld')

    def getServiceName(self):
        return "HelloWorldCHI"

    def getServiceVersion(self):
        return 0.1

    def getInstallID(self):
        if os.path.exists('config.json'):
            with open('config.json') as data_file:
                data = json.load(data_file)
                if len(data) > 0:
                    return str(data)
        return ''

    def onInstall(self, id):
        with open('config.json', 'w') as outfile:
            json.dump(id, outfile)

    def onEnable(self):
        # self.sm.database.query('CREATE TABLE "helloworldtest"(  id integer NOT NULL  ,name TEXT NOT NULL)')
        print "Running..."
        res = self.sm.communication.runCommandSync("_core.getServiceInfo", json.dumps({'name': self.getServiceName()}),
                                                   cid=Communication.get_random_id())
        print "Ok" + res

    def getInstallInfo(self):
        info = InstallInfo()
        info.name = 'HelloWorldCHI'
        info.title = 'Hello World'
        return info.toJSON()

    def onConnect(self):
        pass
        # self.sm.communication.runCommand("turnoff", json.dumps({'id': 12}))

    def onError(self, node, id, description):
        pass

    def onCallback(self, node, data, id, _from):
        pass

    def pong(self, id, miliseconds):
        self.sm.send(
            '{"type" : "internal" , "node" : "ping" , "name" : "' + self.getServiceName() +
            '" , "version" : "5"'
            + ((' , "id" : "' + self.getInstallID() + '"') if len(id) > 0  else "") + "}")
