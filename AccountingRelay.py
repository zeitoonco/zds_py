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
        whitelist = ["getConfig", "setConfig", "newFiscalYear", "modifyFiscalYear", "closeFiscalYear",
                     "removeFiscalYear", "newAccount", "modifyAccount", "removeAccount", "newDl", "modifyDL",
                     "removeDL", "activeDL", "deactiveDL", "newCategory", "modifyCategory", "removeCategory",
                     "newTopic", "modifyTopic", "removeTopic", "addAccountTopic", "removeAccountTopic", "newVoucher",
                     "modifyVoucher", "removeVoucher", "finalizeVoucher", "newVoucherItem", "modifyVoucherItem",
                     "removeVoucherItem", "newGLVoucher", "removeGLVoucher", "newGLVoucherItem", "removeGLVoucherItem",
                     "newCash", "modifyCash", "removeCash", "newCostCenter", "modifyCostCenter", "removeCostCenter",
                     "newParty", "modifyParty", "removeParty", "addPartyBlacklist", "removePartyBlacklist", "newBank",
                     "modifyBank", "removeBank", "newBankAccountType", "modifyBankAccountType", "removeBankAccountType",
                     "newBankAccount", "modifyBankAccount", "removeBankAccount", "newBankBranch", "modifyBankBranch",
                     "removeBankBranch", "newCurrency", "modifyCurrency", "removeCurrency", "newCurrencyExchangeRate",
                     "modifyCurrencyExchangeRate", "removeCurrencyExchangeRate", "newLocation", "modifyLocation",
                     "removeLocation"]
        if callable(op) and str(node).replace(self.getServiceName(), '').replace('.', '') in whitelist:
            try:
                res = op(data, _id, _from, node)
                self.sm.communication.runCallback(name=node, data=res, id=_id)
            except:
                self.sm.communication.runCallback(name=node, data="{'error': True}", id=_id)
        else:
            raise NotImplementedError

    def getConfig(self, data, _id, _from, node):
        print 'ok?'

    def setConfig(self, data, _id, _from, node):
        sql = "Blah Blah Blah"
        # self.SafeCall(sql,_id,_from,node)

    def newFiscalYear(self, data, _id, _from, node):
        pass

    def modifyFiscalYear(self, data, _id, _from, node):
        pass

    def closeFiscalYear(self, data, _id, _from, node):
        pass

    def removeFiscalYear(self, data, _id, _from, node):
        pass

    def newAccount(self, data, _id, _from, node):
        pass

    def modifyAccount(self, data, _id, _from, node):
        pass

    def removeAccount(self, data, _id, _from, node):
        pass

    def newDl(self, data, _id, _from, node):
        pass

    def modifyDL(self, data, _id, _from, node):
        pass

    def removeDL(self, data, _id, _from, node):
        pass

    def activeDL(self, data, _id, _from, node):
        pass

    def deactiveDL(self, data, _id, _from, node):
        pass

    def newCategory(self, data, _id, _from, node):
        pass

    def modifyCategory(self, data, _id, _from, node):
        pass

    def removeCategory(self, data, _id, _from, node):
        pass

    def newTopic(self, data, _id, _from, node):
        pass

    def modifyTopic(self, data, _id, _from, node):
        pass

    def removeTopic(self, data, _id, _from, node):
        pass

    def addAccountTopic(self, data, _id, _from, node):
        pass

    def removeAccountTopic(self, data, _id, _from, node):
        pass

    def newVoucher(self, data, _id, _from, node):
        pass

    def modifyVoucher(self, data, _id, _from, node):
        pass

    def removeVoucher(self, data, _id, _from, node):
        pass

    def finalizeVoucher(self, data, _id, _from, node):
        pass

    def newVoucherItem(self, data, _id, _from, node):
        pass

    def modifyVoucherItem(self, data, _id, _from, node):
        pass

    def removeVoucherItem(self, data, _id, _from, node):
        pass

    def newGLVoucher(self, data, _id, _from, node):
        pass

    def removeGLVoucher(self, data, _id, _from, node):
        pass

    def newGLVoucherItem(self, data, _id, _from, node):
        pass

    def removeGLVoucherItem(self, data, _id, _from, node):
        pass

    def newCash(self, data, _id, _from, node):
        pass

    def modifyCash(self, data, _id, _from, node):
        pass

    def removeCash(self, data, _id, _from, node):
        pass

    def newCostCenter(self, data, _id, _from, node):
        pass

    def modifyCostCenter(self, data, _id, _from, node):
        pass

    def removeCostCenter(self, data, _id, _from, node):
        pass

    def newParty(self, data, _id, _from, node):
        pass

    def modifyParty(self, data, _id, _from, node):
        pass

    def removeParty(self, data, _id, _from, node):
        pass

    def addPartyBlacklist(self, data, _id, _from, node):
        pass

    def removePartyBlacklist(self, data, _id, _from, node):
        pass

    def newBank(self, data, _id, _from, node):
        pass

    def modifyBank(self, data, _id, _from, node):
        pass

    def removeBank(self, data, _id, _from, node):
        pass

    def newBankAccountType(self, data, _id, _from, node):
        pass

    def modifyBankAccountType(self, data, _id, _from, node):
        pass

    def removeBankAccountType(self, data, _id, _from, node):
        pass

    def newBankAccount(self, data, _id, _from, node):
        pass

    def modifyBankAccount(self, data, _id, _from, node):
        pass

    def removeBankAccount(self, data, _id, _from, node):
        pass

    def newBankBranch(self, data, _id, _from, node):
        pass

    def modifyBankBranch(self, data, _id, _from, node):
        pass

    def removeBankBranch(self, data, _id, _from, node):
        pass

    def newCurrency(self, data, _id, _from, node):
        pass

    def modifyCurrency(self, data, _id, _from, node):
        pass

    def removeCurrency(self, data, _id, _from, node):
        pass

    def newCurrencyExchangeRate(self, data, _id, _from, node):
        pass

    def modifyCurrencyExchangeRate(self, data, _id, _from, node):
        pass

    def removeCurrencyExchangeRate(self, data, _id, _from, node):
        pass

    def newLocation(self, data, _id, _from, node):
        pass

    def modifyLocation(self, data, _id, _from, node):
        pass

    def removeLocation(self, data, _id, _from, node):
        pass
