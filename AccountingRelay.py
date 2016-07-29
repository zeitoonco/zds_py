# coding=utf-8
import json
import logging
import os

import CommunicationHandlerInterface
from DataTypes.InstallInfo import InstallInfo


class AccountingRelay(CommunicationHandlerInterface.CommunicationHandlerInterface):
    logger = logging.getLogger('HelloWorld')

    def getServiceName(self):
        return "AccountingRelay"

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
        with open('AccountingRelayCHI.config.json', 'w') as outfile:
            json.dump(id, outfile)
        with open('AccountingRelay.sql') as sql:
            s = sql.read().replace("\n", " ")
            self.sm.database.executeSync(s)

    def onEnable(self):
        # # self.sm.database.query('CREATE TABLE "helloworldtest"(  id integer NOT NULL  ,name TEXT NOT NULL)')
        # print "Running..."
        # res = self.sm.database.querySync('SELECT * FROM "HelloWorldCHI".helloworldtest')
        #
        # print "Ok"

        self.sm.communication.registerCommand('"AccountingRelay.getConfig","AccountingRelay.setConfig"')

    def getInstallInfo(self):
        info = InstallInfo()
        info.name = 'AccountingRelay'
        info.title = 'Accounting Relay'
        info.datatypes.append({"name": "AccountingRelay.genericInput", "version": 1})
        info.datatypes.append({"name": "AccountingRelay.genericOutput", "version": 1})
        info.commands.append({"name": "AccountingRelay.getConfig",
                              "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1,
                              "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.setConfig",
                              "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1,
                              "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
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

    def onCommand(self, node, data, _id, _from):
        op = getattr(self, str(node).replace(self.getServiceName(), '').replace('.', ''), None)
        if callable(op):
            op(data, _id, _from, node)
        else:
            raise NotImplementedError

    def getConfig(self, data, _id, _from, node):
        self.sm.communication.runCallback(name=node, data='"OK"', id=_id)
        print 'ok?'
