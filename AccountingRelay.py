# coding=utf-8
import json
import logging
import os

import CommunicationHandlerInterface
from DataTypes.InstallInfo import InstallInfo


class AccountingRelay(CommunicationHandlerInterface.CommunicationHandlerInterface):
    logger = logging.getLogger('HelloWorld')

    def getServiceName(self):
        return "AccountingRelayCHI"

    def getServiceVersion(self):
        return 0.1

    def getInstallID(self):
        if os.path.exists('AccountingRelayCHI.config.json'):
            with open('AccountingRelayCHI.config.json') as data_file:
                data = json.load(data_file)
                if len(data) > 0:
                    return str(data)
        return ''

    def onInstall(self, id):
        with open('AccountingRelayCHIconfig.json', 'w') as outfile:
            json.dump(id, outfile)
        with open('AccountingRelay.sql') as sql:
            self.sm.database.executeSync(sql.read())

    def onEnable(self):
        # # self.sm.database.query('CREATE TABLE "helloworldtest"(  id integer NOT NULL  ,name TEXT NOT NULL)')
        # print "Running..."
        # res = self.sm.database.querySync('SELECT * FROM "HelloWorldCHI".helloworldtest')
        #
        # print "Ok"
        pass

    def getInstallInfo(self):
        info = InstallInfo()
        info.name = 'AccountingRelay'
        info.title = 'Accounting Relay'
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
