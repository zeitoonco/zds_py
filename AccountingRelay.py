# coding=utf-8
import json
import logging
import os
import re

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
            # self.sm.database.executeSync(s)

    def onUninstall(self):
        with open('AccountingRelayCHI.config.json', 'w') as outfile:
            json.dump("", outfile)

    def onEnable(self):
        # # self.sm.database.query('CREATE TABLE "helloworldtest"(  id integer NOT NULL  ,name TEXT NOT NULL)')
        # print "Running..."
        # res = self.sm.database.querySync('SELECT * FROM "HelloWorldCHI".helloworldtest')
        #
        # print "Ok"
        # raise Exception
        self.sm.communication.registerCommand(
            '"AccountingRelay.getConfig","AccountingRelay.setConfig","AccountingRelay.newFiscalYear","AccountingRelay.modifyFiscalYear","AccountingRelay.closeFiscalYear","AccountingRelay.removeFiscalYear","AccountingRelay.newAccount","AccountingRelay.modifyAccount","AccountingRelay.removeAccount","AccountingRelay.newDl","AccountingRelay.modifyDL","AccountingRelay.removeDL","AccountingRelay.[de]activeDL","AccountingRelay.newCategory","AccountingRelay.modifyCategory","AccountingRelay.removeCategory","AccountingRelay.newTopic","AccountingRelay.modifyTopic","AccountingRelay.removeTopic","AccountingRelay.addAccountTopic","AccountingRelay.removeAccountTopic","AccountingRelay.newVoucher","AccountingRelay.modifyVoucher","AccountingRelay.removeVoucher","AccountingRelay.finalizeVoucher","AccountingRelay.newVoucherItem","AccountingRelay.modifyVoucherItem","AccountingRelay.removeVoucherItem","AccountingRelay.newGLVoucher","AccountingRelay.removeGLVoucher","AccountingRelay.newGLVoucherItem","AccountingRelay.removeGLVoucherItem","AccountingRelay.newCash","AccountingRelay.modifyCash","AccountingRelay.removeCash","AccountingRelay.newCostCenter","AccountingRelay.modifyCostCenter","AccountingRelay.removeCostCenter","AccountingRelay.newParty","AccountingRelay.modifyParty","AccountingRelay.removeParty","AccountingRelay.addPartyBlacklist","AccountingRelay.removePartyBlacklist","AccountingRelay.newBank","AccountingRelay.modifyBank","AccountingRelay.removeBank","AccountingRelay.newBankAccountType","AccountingRelay.modifyBankAccountType","AccountingRelay.removeBankAccountType","AccountingRelay.newBankAccount","AccountingRelay.modifyBankAccount","AccountingRelay.removeBankAccount","AccountingRelay.newBankBranch","AccountingRelay.modifyBankBranch","AccountingRelay.removeBankBranch","AccountingRelay.newCurrency","AccountingRelay.modifyCurrency","AccountingRelay.removeCurrency","AccountingRelay.newCurrencyExchangeRate","AccountingRelay.modifyCurrencyExchangeRate","AccountingRelay.removeCurrencyExchangeRate","AccountingRelay.newLocation","AccountingRelay.modifyLocation","AccountingRelay.removeLocation","AccountingRelay.query"')

    def getInstallInfo(self):
        info = InstallInfo()
        info.name = 'AccountingRelay'
        info.title = 'Accounting Relay'
        info.datatypes.append({"name": "AccountingRelay.genericInput", "version": 1})
        info.datatypes.append({"name": "AccountingRelay.genericOutput", "version": 1})
        info.commands.append({"name": "AccountingRelay.getConfig",
                              "inputdatatype": "AccountingRelay.genericInput", "inputdatatypeversion": 1,
                              "outputdatatype": "AccountingRelay.genericOutput", "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.setConfig", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newFiscalYear", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.modifyFiscalYear", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.closeFiscalYear", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeFiscalYear", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newAccount", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyAccount", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeAccount", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newDl", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyDL", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeDL", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.activeDL", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.deactiveDL", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newCategory", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyCategory", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeCategory", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newTopic", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyTopic", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeTopic", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.addAccountTopic", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeAccountTopic", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newVoucher", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyVoucher", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeVoucher", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.finalizeVoucher", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newVoucherItem", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.modifyVoucherItem", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeVoucherItem", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newGLVoucher", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeGLVoucher", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.newGLVoucherItem", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeGLVoucherItem", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newCash", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyCash", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeCash", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newCostCenter", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.modifyCostCenter", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeCostCenter", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newParty", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyParty", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeParty", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.addPartyBlacklist", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removePartyBlacklist", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyBank", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeBank", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.newBankAccountType", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.modifyBankAccountType", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeBankAccountType", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newBankAccount", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.modifyBankAccount", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeBankAccount", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newBankBranch", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.modifyBankBranch", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeBankBranch", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newCurrency", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyCurrency", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeCurrency", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.newCurrencyExchangeRate", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.modifyCurrencyExchangeRate", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append(
            {"name": "AccountingRelay.removeCurrencyExchangeRate", "inputdatatype": "AccountingRelay.genericInput",
             "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
             "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.newLocation", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.modifyLocation", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.removeLocation", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
                              "outputdatatypeversion": 1})
        info.commands.append({"name": "AccountingRelay.query", "inputdatatype": "AccountingRelay.genericInput",
                              "inputdatatypeversion": 1, "outputdatatype": "AccountingRelay.genericOutput",
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
                     "removeLocation", "query"]
        caster = {"setConfig": " '{uid}'::BIGINT, '{name}'::TEXT, '{value}'::TEXT ",
                  "getConfig": " '{uid}'::BIGINT, '{name}'::TEXT ",
                  "newFiscalYear": " '{uid}'::BIGINT, '{title}'::TEXT, '{start}'::DATE, '{end}'::DATE ",
                  "closeFiscalYear": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newAccount": " '{uid}'::BIGINT, '{parent}'::BIGINT, '{type}'::INTEGER, '{code}'::VARCHAR(40) , '{title}'::VARCHAR(250) , '{title2}'::VARCHAR(250) , '{isactive}'::BOOLEAN, '{cashflowcategory}'::INTEGER, '{openingbalance}'::NUMERIC(19, 4) , '{balancetype}'::INTEGER, '{hasbaancetypecheck}'::BOOLEAN, '{hasdl}'::BOOLEAN, '{hascurrency}'::BOOLEAN, '{hascurrencyconversion}'::BOOLEAN, '{hastracking}'::BOOLEAN, '{hastrackingcheck}'::BOOLEAN ",
                  "modifyAccount": " '{uid}'::BIGINT, '{id}'::BIGINT, '{parent}'::BIGINT, '{type}'::INTEGER, '{code}'::VARCHAR(40) , '{title}'::VARCHAR(250) , '{title2}'::VARCHAR(250) , '{isactive}'::BOOLEAN, '{cashflowcategory}'::INTEGER, '{balancetype}'::INTEGER, '{hasbaancetypecheck}'::BOOLEAN, '{hasdl}'::BOOLEAN, '{hascurrency}'::BOOLEAN, '{hascurrencyconversion}'::BOOLEAN, '{hastracking}'::BOOLEAN, '{hastrackingcheck}'::BOOLEAN ",
                  "removeAccount": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newDL": " '{uid}'::BIGINT, '{type}'::INTEGER, '{code}'::VARCHAR(40) , '{title}'::VARCHAR(250) , '{title2}'::VARCHAR(250) , '{isactive}'::BOOLEAN ",
                  "modifyDL": " '{uid}'::BIGINT, '{id}'::BIGINT, '{type}'::INTEGER, '{code}'::VARCHAR(40) , '{title}'::VARCHAR(250) , '{title2}'::VARCHAR(250) , '{isactive}'::BOOLEAN ",
                  "removeDL": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "activeDL": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "deactivateDL": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newCategory": " '{uid}'::BIGINT, '{type}'::INTEGER, '{title}'::VARCHAR(250) ",
                  "modifyCategory": " '{uid}'::BIGINT, '{id}'::BIGINT, '{type}'::INTEGER, '{title}'::VARCHAR(250) ",
                  "removeCategory": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newTopic": " '{uid}'::BIGINT, '{category}'::BIGINT, '{title}'::VARCHAR(250) ",
                  "modifyTopic": " '{uid}'::BIGINT, '{id}'::BIGINT, '{category}'::BIGINT, '{title}'::VARCHAR(250) ",
                  "removeTopic": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "addAccountTopic": " '{uid}'::BIGINT, '{account}'::BIGINT, '{topic}'::BIGINT ",
                  "removeAccountTopic": " '{uid}'::BIGINT, '{account}'::BIGINT, '{topic}'::BIGINT ",
                  "newVoucher": " '{uid}'::BIGINT, '{number}'::INTEGER, '{referencenumber}'::INTEGER, '{secondarynumber}'::INTEGER, '{dailynumber}'::INTEGER, '{Date}'::TIMESTAMP WITH TIME ZONE, '{type}'::INTEGER, '{description}'::CHARACTER VARYING(250) , '{fiscalyearid}'::BIGINT, '{state}'::INTEGER ",
                  "modifyVoucher": " '{uid}'::BIGINT, '{id}'::BIGINT, '{number}'::INTEGER, '{referencenumber}'::INTEGER, '{secondarynumber}'::INTEGER, '{dailynumber}'::INTEGER, '{Date}'::TIMESTAMP WITH TIME ZONE, '{type}'::INTEGER, '{description}'::CHARACTER VARYING(250) , '{fiscalyearid}'::BIGINT, '{state}'::INTEGER ",
                  "removeVoucher": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "finalizeVoucher": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newVoucherItem": " '{uid}'::BIGINT, '{voucherid}'::BIGINT, '{rownumber}'::INTEGER, '{accountid}'::BIGINT, '{dlid}'::BIGINT, '{debit}'::NUMERIC(19, 4) , '{credit}'::NUMERIC(19, 4) , '{currencyid}'::BIGINT, '{currencyrate}'::NUMERIC(26, 16) , '{currencydebit}'::NUMERIC(19, 4) , '{currencycredit}'::NUMERIC(19, 4) , '{trackingnumber}'::VARCHAR(40) , '{trackingdate}'::TIMESTAMPTZ, '{description}'::VARCHAR(250) ",
                  "modifyVoucherItem": " '{uid}'::BIGINT, '{id}'::BIGINT, '{voucherid}'::BIGINT, '{rownumber}'::INTEGER, '{accountid}'::BIGINT, '{dlid}'::BIGINT, '{debit}'::NUMERIC(19, 4) , '{credit}'::NUMERIC(19, 4) , '{currencyid}'::BIGINT, '{currencyrate}'::NUMERIC(26, 16) , '{currencydebit}'::NUMERIC(19, 4) , '{currencycredit}'::NUMERIC(19, 4) , '{trackingnumber}'::VARCHAR(40) , '{trackingdate}'::TIMESTAMPTZ, '{description}'::VARCHAR(250) ",
                  "removeVoucherItem": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newGLVoucher": " '{uid}'::BIGINT, '{fiscalyear}'::BIGINT, '{number}'::INTEGER, '{date}'::TIMESTAMPTZ ",
                  "removeGLVoucher": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newGLVoucherItem": " '{uid}'::BIGINT, '{glv}'::BIGINT, '{voucher}'::BIGINT ",
                  "removeGLVoucherItem": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newCash": " '{uid}'::BIGINT, '{title}'::VARCHAR(250) , '{DL}'::BIGINT, '{currency}'::BIGINT, '{rate}'::NUMERIC(26, 16) , '{firstamount}'::NUMERIC(19, 4) , '{firstdate}'::TIMESTAMPTZ, '{balance}'::NUMERIC(19, 4) ",
                  "modifyCash": " '{uid}'::BIGINT, '{id}'::BIGINT, '{title}'::VARCHAR(250) , '{DL}'::BIGINT, '{currency}'::BIGINT, '{rate}'::NUMERIC(26, 16) , '{firstamount}'::NUMERIC(19, 4) , '{firstdate}'::TIMESTAMPTZ, '{balance}'::NUMERIC(19, 4) ",
                  "removeCash": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newCostCenter": " '{uid}'::BIGINT, '{dlid}'::BIGINT, '{type}'::INTEGER ",
                  "modifyCostCenter": " '{uid}'::BIGINT, '{id}'::BIGINT, '{dlid}'::BIGINT, '{type}'::INTEGER ",
                  "removeCostCenter": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newParty": " '{uid}'::BIGINT, '{type}'::INTEGER, '{subtype}'::INTEGER, '{name}'::VARCHAR(250) , '{lastname}'::VARCHAR(250) , '{nameEng}'::VARCHAR(250) , '{lastnameEng}'::VARCHAR(250) , '{economiccode}'::VARCHAR(50) , '{identificationcode}'::VARCHAR(50) , '{website}'::VARCHAR(250) , '{email}'::VARCHAR(250) , '{dlid}'::BIGINT, '{blacklist}'::BOOLEAN ",
                  "modifyParty": " '{uid}'::BIGINT, '{id}'::BIGINT, '{type}'::INTEGER, '{subtype}'::INTEGER, '{name}'::VARCHAR(250) , '{lastname}'::VARCHAR(250) , '{nameEng}'::VARCHAR(250) , '{lastnameEng}'::VARCHAR(250) , '{economiccode}'::VARCHAR(50) , '{identificationcode}'::VARCHAR(50) , '{website}'::VARCHAR(250) , '{email}'::VARCHAR(250) , '{dlid}'::BIGINT, '{blacklist}'::BOOLEAN ",
                  "removeParty": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "addPartyBlacklist": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "removePartyBlacklist": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newBank": " '{uid}'::BIGINT, '{title}'::VARCHAR(250) , '{logo}'::TEXT ",
                  "modifyBank": " '{uid}'::BIGINT, '{id}'::BIGINT, '{title}'::VARCHAR(250) , '{logo}'::TEXT ",
                  "removeBank": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newBankAccountType": " '{uid}'::BIGINT, '{title}'::VARCHAR(250) , '{hascheque}'::BOOLEAN ",
                  "modifyBankAccountType": " '{uid}'::BIGINT, '{id}'::BIGINT, '{title}'::VARCHAR(250) , '{hascheque}'::BOOLEAN ",
                  "removeBankAccountType": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newBankAccount": " '{uid}'::BIGINT, '{bankbranchid}'::BIGINT, '{accountno}'::INTEGER, '{bankaccounttypeid}'::BIGINT, '{dlid}'::BIGINT, '{currencyid}'::BIGINT, '{rate}'::DATE, '{firstamount}'::NUMERIC(19, 4) , '{firstdate}'::TIMESTAMPTZ, '{balance}'::NUMERIC(19, 4) , '{billfirstamount}'::NUMERIC(19, 4) , '{clearformatname}'::VARCHAR(250) , '{owner}'::VARCHAR(4000) ",
                  "modifyBankAccount": " '{uid}'::BIGINT, '{id}'::BIGINT, '{bankbranchid}'::BIGINT, '{accountno}'::INTEGER, '{bankaccounttypeid}'::BIGINT, '{dlid}'::BIGINT, '{currencyid}'::BIGINT, '{rate}'::DATE, '{balance}'::NUMERIC(19, 4) , '{billfirstamount}'::NUMERIC(19, 4) , '{clearformatname}'::VARCHAR(250) , '{owner}'::VARCHAR(4000) ",
                  "removeBankAccount": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newBankBranch": " '{uid}'::BIGINT, '{bankid}'::BIGINT, '{code}'::VARCHAR(250) , '{title}'::VARCHAR(250) , '{locationid}'::BIGINT ",
                  "modifyBankBranch": " '{uid}'::BIGINT, '{id}'::BIGINT, '{bankid}'::BIGINT, '{code}'::VARCHAR(250) , '{title}'::VARCHAR(250) , '{locationid}'::BIGINT ",
                  "removeBankBranch": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newCurrency": " '{uid}'::BIGINT, '{title}'::VARCHAR(250) , '{exchangeunit}'::INTEGER, '{precisioncount}'::INTEGER, '{precisionname}'::VARCHAR(40) , '{precisionnameEng}'::VARCHAR(40) , '{sign}'::VARCHAR(40) ",
                  "modifyCurrency": " '{uid}'::BIGINT, '{id}'::BIGINT, '{title}'::VARCHAR(250) , '{exchangeunit}'::INTEGER, '{precisioncount}'::INTEGER, '{precisionname}'::VARCHAR(40) , '{precisionnameEng}'::VARCHAR(40) , '{sign}'::VARCHAR(40) ",
                  "removeCurrency": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newCurrencyExchangeRate": " '{uid}'::BIGINT, '{currency}'::BIGINT, '{effectivedate}'::TIMESTAMPTZ, '{exchangerate}'::DATE, '{fiscalyearid}'::BIGINT ",
                  "modifyCurrencyExchangeRate": " '{uid}'::BIGINT, '{id}'::BIGINT, '{currency}'::BIGINT, '{effectivedate}'::TIMESTAMPTZ, '{exchangerate}'::DATE, '{fiscalyearid}'::BIGINT ",
                  "removeCurrencyExchangeRate": " '{uid}'::BIGINT, '{id}'::BIGINT ",
                  "newLocation": " '{uid}'::BIGINT, '{title}'::VARCHAR(250) , '{code}'::VARCHAR(40) , '{parentid}'::BIGINT, '{type}'::INTEGER, '{ministryoffinancecode}'::VARCHAR(50) , '{ministryoffinancecodeoftownship}'::VARCHAR(50) ",
                  "modifyLocation": " '{uid}'::BIGINT, '{id}'::BIGINT, '{title}'::VARCHAR(250) , '{code}'::VARCHAR(40) , '{parentid}'::BIGINT, '{type}'::INTEGER, '{ministryoffinancecode}'::VARCHAR(50) , '{ministryoffinancecodeoftownship}'::VARCHAR(50) ",
                  "removeLocation": " '{uid}'::BIGINT, '{id}'::BIGINT "}
        method = str(node).replace(self.getServiceName(), '').replace('.', '')
        if method in whitelist:
            try:
                if callable(op):
                    res = op(data, _id, _from, node)
                elif method in caster:

                    q = "SELECT %s(%s) AS res" % (
                        method, str(caster[method]).format(**data))
                    res = self.sm.database.singleFieldQuerySync(q)
                else:
                    raise NotImplementedError
                self.sm.communication.runCallback(name=node, data='{"success":true,"result": ' + res + '}', id=_id)
            except Exception, e:
                self.sm.communication.runCallback(name=node, data='{"success":false}', id=_id)
        else:
            raise NotImplementedError

    def query(self, data, _id, _from, node):
        table = re.sub(r'\W+', '', data['table'])
        query = 'SELECT '

        if 'columns' in data:
            query += ','.join(data['columns'])
        else:
            query += ' * '
        query += ' FROM ' + table + ' '

        if 'where' in data:
            total = len(data['where'])
            i = 0
            query += " WHERE "
            for row in data['where']:
                i += 1
                col = row[0].replace("'", "\\'").replace("\"", '\\"')
                op = row[1].replace("'", "\\'").replace("\"", '\\"')
                text = row[2].replace("'", "\\'").replace("\"", '\\"')
                cond = row[3].replace("'", "\\'").replace("\"", '\\"')
                query += ' "' + col + '" ' + ' ' + op + " '" + text + "' "
                if i < total:
                    query += cond + " "
        if 'order' in data:
            query += " ORDER BY " + data['order'][0].replace("'", "\\'").replace("\"", '\\"') + " " + data['order'][
                0].replace("'", "\\'").replace("\"", '\\"')

        if 'limit' in data:
            query += " LIMIT " + data['order'][0].replace("'", "\\'").replace("\"", '\\"')
        query += ";"
        res = self.sm.database.querySync(query)
        return res

        # def getConfig(self, data, _id, _from, node):
        #     # return "okkkk + " + data['name']
        #     q = "SELECT getConfig('%s','%s') AS res" % (data['userid'], data['name'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def setConfig(self, data, _id, _from, node):
        #     q = "SELECT setConfig('%s','%s','%s') AS res" % (data['userid'], data['name'], data['value'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newFiscalYear(self, data, _id, _from, node):
        #     q = "SELECT newFiscalYear('%s','%s','%s','%s') AS res" % (
        #         data['userid'], data['title'], data['start'], data['end'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyFiscalYear(self, data, _id, _from, node):
        #     q = "SELECT modifyFiscalYear('%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                       int(data['id']), data['title'], data['start'],
        #                                                                       data['end'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def closeFiscalYear(self, data, _id, _from, node):
        #     q = "SELECT closeFiscalYear('%s','%s') AS res" % (data['userid'], int(data['id']))
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeFiscalYear(self, data, _id, _from, node):
        #     q = "SELECT removeFiscalYear('%s','%s') AS res" % (data['userid'], int(data['id']))
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newAccount(self, data, _id, _from, node):
        #     q = "SELECT newAccount('{0:s}'::BIGINT,'{1:s}'::BIGINT,'{2:s}'::INTEGER,'{3:s}'::TEXT,'{4:s}'::TEXT,'{5:s}'::TEXT," \
        #         "'{6:s}'::BOOL,'{7:s}'::INT,'{8:s}'::INT,'{9:s}'::BOOL,'{10:s}'::BOOL,'{11:s}'::BOOL,'{12:s}'::BOOL,'{13:s}'::BOOL,'{14:s}'::BOOL) AS res".format(
        #         data['userid'],
        #         data["parent"], data["type"], data["code"], data["title"], data["title2"], data["isactive"],
        #         data["cashflowcategory"], data["openingbalance"], data["balancetype"], data["hasbalancetypecheck"],
        #         data["hasdl"], data["hascurrency"], data["hascurrencyconversion"], data["hastracking"],
        #         data["hastrackingcheck"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyAccount(self, data, _id, _from, node):
        #     q = "SELECT modifyAccount('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}',{6:s},'{7:s}','{8:s}','{9:s}','{10:s}','{11:s}','{12:s}','{13:s}','{14:s}','{15:s}') AS res".format(
        #         data['userid'],
        #         data["id"], data["parent"], data["type"], data["code"], data["title"], data["title2"], data["isactive"],
        #         data["cashflowcategory"], data["balancetype"], data["hasbaancetypecheck"], data["hasdl"],
        #         data["hascurrency"], data["hascurrencyconversion"], data["hastracking"],
        #         data["hastrackingcheck"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeAccount(self, data, _id, _from, node):
        #     q = "SELECT removeAccount('%s','%s') AS res" % (data['userid'], int(data['id']))
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newDl(self, data, _id, _from, node):
        #     q = "SELECT newDl('%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                 data['code'], data['title'], data['title2'],
        #                                                                 data['type'], data['isactive'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyDL(self, data, _id, _from, node):
        #     q = "SELECT modifyDL('%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                         data['id'], data['code'], data['title'],
        #                                                                         data['title2'], data['type'],
        #                                                                         data['isactive'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeDL(self, data, _id, _from, node):
        #     q = "SELECT removeDL('%s','%s') AS res" % (data['userid'], data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def activeDL(self, data, _id, _from, node):
        #     q = "SELECT activeDL('%s','%s') AS res" % (data['userid'], data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def deactiveDL(self, data, _id, _from, node):
        #     q = "SELECT deactiveDL('%s','%s') AS res" % (data['userid'], data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newCategory(self, data, _id, _from, node):
        #     q = "SELECT newCategory('%s','%s','%s') AS res" % (
        #         data['userid'], data['type'], data['title'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyCategory(self, data, _id, _from, node):
        #     q = "SELECT modifyCategory('%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                     data['id'], data['title'], data['type'],
        #                                                                     data['category'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeCategory(self, data, _id, _from, node):
        #     q = "SELECT removeCategory('%s','%s') AS res" % (data['userid'], data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newTopic(self, data, _id, _from, node):
        #     q = "SELECT newTopic('%s','%s','%s','%s') AS res" % (
        #         data['userid'], data['title'], data['parent'], data['category'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyTopic(self, data, _id, _from, node):
        #     q = "SELECT modifyTopic('%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                  data['id'], data['title'], data['parent'],
        #                                                                  data['category'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeTopic(self, data, _id, _from, node):
        #     q = "SELECT removeTopic('%s','%s') AS res" % (data['userid'],
        #                                                   data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def addAccountTopic(self, data, _id, _from, node):
        #     q = "SELECT addAccountTopic('%s','%s','%s') AS res" % (data['userid'],
        #                                                            data['account'], data['topic'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeAccountTopic(self, data, _id, _from, node):
        #     q = "SELECT removeAccountTopic('%s','%s','%s') AS res" % (data['userid'],
        #                                                               data['account'], data['topic'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newVoucher(self, data, _id, _from, node):
        #     q = "SELECT newVoucher('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                                          data['number'],
        #                                                                                          data['date'],
        #                                                                                          data['referencenumber'],
        #                                                                                          data['secondarynumber'],
        #                                                                                          data['state'],
        #                                                                                          data['type'],
        #                                                                                          data['description'],
        #                                                                                          data['dailynumber'],
        #                                                                                          data['issuersystem'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyVoucher(self, data, _id, _from, node):
        #     q = "SELECT modifyVoucher('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                                                  data['id'],
        #                                                                                                  data['number'],
        #                                                                                                  data['date'], data[
        #                                                                                                      'referencenumber'],
        #                                                                                                  data[
        #                                                                                                      'secondarynumber'],
        #                                                                                                  data['state'],
        #                                                                                                  data['type'],
        #                                                                                                  data[
        #                                                                                                      'description'],
        #                                                                                                  data[
        #                                                                                                      'dailynumber'],
        #                                                                                                  data[
        #                                                                                                      'issuersystem'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeVoucher(self, data, _id, _from, node):
        #     q = "SELECT removeVoucher('%s','%s') AS res" % (data['userid'],
        #                                                     data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def finalizeVoucher(self, data, _id, _from, node):
        #     q = "SELECT finalizeVoucher('%s','%s') AS res" % (data['userid'],
        #                                                       data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newVoucherItem(self, data, _id, _from, node):
        #     q = "SELECT newVoucherItem('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}',{6:s},'{7:s}','{8:s}','{9:s}','{10:s}','{11:s}','{12:s}','{13:s}') AS res".format(
        #         data['userid'],
        #         data["voucherid"], data["rownumber"], data["accountid"], data["dlid"], data["debit"], data["credit"],
        #         data["currencyid"], data["currencyrate"], data["currencydebit"], data["currencycredit"],
        #         data["trackingnumber"], data["trackingdate"], data["description"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyVoucherItem(self, data, _id, _from, node):
        #     q = "SELECT modifyVoucherItem('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}',{6:s},'{7:s}','{8:s}','{9:s}','{10:s}','{11:s}','{12:s}','{13:s','{14:s'}) AS res".format(
        #         data['userid'],
        #         data["id"], data["voucherid"], data["rownumber"], data["accountid"], data["dlid"], data["debit"],
        #         data["credit"], data["currencyid"], data["currencyrate"], data["currencydebit"], data["currencycredit"],
        #         data["trackingnumber"], data["trackingdate"], data["description"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeVoucherItem(self, data, _id, _from, node):
        #     q = "SELECT removeVoucherItem('%s','%s') AS res" % (data['userid'],
        #                                                         data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newGLVoucher(self, data, _id, _from, node):
        #     q = "SELECT newGLVoucher('%s','%s','%s') AS res" % (data['userid'],
        #                                                         data['number'], data['date'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeGLVoucher(self, data, _id, _from, node):
        #     q = "SELECT removeGLVoucher('%s','%s') AS res" % (data['userid'],
        #                                                       data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newGLVoucherItem(self, data, _id, _from, node):
        #     q = "SELECT newGLVoucherItem('%s','%s') AS res" % (data['userid'],
        #                                                        data['voucherid'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeGLVoucherItem(self, data, _id, _from, node):
        #     q = "SELECT removeGLVoucherItem('%s','%s') AS res" % (data['userid'],
        #                                                           data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newCash(self, data, _id, _from, node):
        #     q = "SELECT newCash('%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                             data['title'], data['DL'],
        #                                                                             data['currency'], data['rate'],
        #                                                                             data['firstamount'], data['firstdate'],
        #                                                                             data['balance'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyCash(self, data, _id, _from, node):
        #     q = "SELECT modifyCash('%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                                     data['id'], data['title'],
        #                                                                                     data['DL'], data['currency'],
        #                                                                                     data['rate'],
        #                                                                                     data['firstamount'],
        #                                                                                     data['firstdate'],
        #                                                                                     data['balance'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeCash(self, data, _id, _from, node):
        #     q = "SELECT removeCash('%s','%s') AS res" % (data['userid'],
        #                                                  data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newCostCenter(self, data, _id, _from, node):
        #     q = "SELECT newCostCenter('%s','%s','%s') AS res" % (data['userid'],
        #                                                          data['dlid'], data['type'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyCostCenter(self, data, _id, _from, node):
        #     q = "SELECT modifyCostCenter('%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                  data['id'], data['dlid'], data['type'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeCostCenter(self, data, _id, _from, node):
        #     q = "SELECT removeCostCenter('%s','%s') AS res" % (data['userid'],
        #                                                        data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newParty(self, data, _id, _from, node):
        #     q = "SELECT newParty('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
        #         data['userid'],
        #         data["type"], data["subtype"], data["name"], data["lastname"], data["nameEng"], data["lastnameEng"],
        #         data["economiccode"], data["identificationcode"], data["website"], data["email"], data["dlid"],
        #         data["blacklist"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyParty(self, data, _id, _from, node):
        #     q = "SELECT modifyParty('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
        #         data['userid'],
        #         data["id"], data["type"], data["subtype"], data["name"], data["lastname"], data["nameEng"],
        #         data["lastnameEng"],
        #         data["economiccode"], data["identificationcode"], data["website"], data["email"], data["dlid"],
        #         data["blacklist"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeParty(self, data, _id, _from, node):
        #     q = "SELECT removeParty('%s','%s') AS res" % (data['userid'],
        #                                                   data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def addPartyBlacklist(self, data, _id, _from, node):
        #     q = "SELECT addPartyBlacklist('%s','%s') AS res" % (data['userid'],
        #                                                         data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removePartyBlacklist(self, data, _id, _from, node):
        #     q = "SELECT removePartyBlacklist('%s','%s') AS res" % (data['userid'],
        #                                                            data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newBank(self, data, _id, _from, node):
        #     q = "SELECT newBank('%s','%s','%s') AS res" % (data['userid'],
        #                                                    data['title'], data['logo'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyBank(self, data, _id, _from, node):
        #     q = "SELECT modifyBank('%s','%s','%s') AS res" % (data['userid'],
        #                                                       data['title'], data['logo'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeBank(self, data, _id, _from, node):
        #     q = "SELECT removeBank('%s','%s') AS res" % (data['userid'],
        #                                                  data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newBankAccountType(self, data, _id, _from, node):
        #     q = "SELECT newBankAccountType('%s','%s','%s') AS res" % (data['userid'],
        #                                                               data['title'], data['hascheque'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyBankAccountType(self, data, _id, _from, node):
        #     q = "SELECT modifyBankAccountType('%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                       data['id'], data['title'], data['hascheque'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeBankAccountType(self, data, _id, _from, node):
        #     q = "SELECT removeBankAccountType('%s','%s') AS res" % (data['userid'],
        #                                                             data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newBankAccount(self, data, _id, _from, node):
        #     q = "SELECT newBankAccount('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
        #         data['userid'],
        #         data["bankbranchid"],
        #         data["accountno"],
        #         data["bankaccounttypeid"],
        #         data["dlid"],
        #         data["currencyid"],
        #         data["rate "],
        #         data["firstamount "],
        #         data["firstdate "],
        #         data["balance "],
        #         data["billfirstamount "],
        #         data["clearformatname "],
        #         data["owner"],)
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyBankAccount(self, data, _id, _from, node):
        #     q = "SELECT modifyBankAccount('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
        #         data['userid'],
        #         data["id"], data["bankbranchid"],
        #         data["accountno"],
        #         data["bankaccounttypeid"],
        #         data["dlid"],
        #         data["currencyid"],
        #         data["rate "],
        #         data["firstamount "],
        #         data["firstdate "],
        #         data["balance "],
        #         data["billfirstamount "],
        #         data["clearformatname "],
        #         data["owner"],)
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeBankAccount(self, data, _id, _from, node):
        #     q = "SELECT removeBankAccount('%s','%s') AS res" % (data['userid'],
        #                                                         data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newBankBranch(self, data, _id, _from, node):
        #     q = "SELECT newBankBranch('%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                    data['bankid'], data['code'], data['title'],
        #                                                                    data['locationid'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyBankBranch(self, data, _id, _from, node):
        #     q = "SELECT modifyBankBranch('%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                            data['id'], data['bankid'], data['code'],
        #                                                                            data['title'], data['locationid'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeBankBranch(self, data, _id, _from, node):
        #     q = "SELECT removeBankBranch('%s','%s') AS res" % (data['userid'],
        #                                                        data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newCurrency(self, data, _id, _from, node):
        #     q = "SELECT newCurrency('%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                            data["title"],
        #                                                                            data["exchangeunit"],
        #                                                                            data["precisioncount"],
        #                                                                            data["precisionname"],
        #                                                                            data["precisionnameEng"],
        #                                                                            data["sign"],)
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyCurrency(self, data, _id, _from, node):
        #     q = "SELECT modifyCurrency('%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                                    data["id"],
        #                                                                                    data["title"],
        #                                                                                    data["exchangeunit"],
        #                                                                                    data["precisioncount"],
        #                                                                                    data["precisionname"],
        #                                                                                    data["precisionnameEng"],
        #                                                                                    data["sign"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeCurrency(self, data, _id, _from, node):
        #     q = "SELECT removeCurrency('%s','%s') AS res" % (data['userid'],
        #                                                      data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newCurrencyExchangeRate(self, data, _id, _from, node):
        #     q = "SELECT newCurrencyExchangeRate('%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                         data["currency"],
        #                                                                         data["effectivedate"],
        #                                                                         data["exchangerate"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyCurrencyExchangeRate(self, data, _id, _from, node):
        #     q = "SELECT modifyCurrencyExchangeRate('%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                                 data["id"],
        #                                                                                 data["currency"],
        #                                                                                 data["effectivedate"],
        #                                                                                 data["exchangerate"])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeCurrencyExchangeRate(self, data, _id, _from, node):
        #     q = "SELECT removeCurrencyExchangeRate('%s','%s') AS res" % (data['userid'],
        #                                                                  data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def newLocation(self, data, _id, _from, node):
        #     q = "SELECT newLocation('%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                            data["title"],
        #                                                                            data["code"],
        #                                                                            data["parent"],
        #                                                                            data["type"],
        #                                                                            data["ministryoffinancecode"],
        #                                                                            data["ministryoffinancecodeoftownship"],)
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def modifyLocation(self, data, _id, _from, node):
        #     q = "SELECT modifyLocation('%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (data['userid'],
        #                                                                                    data["id"],
        #                                                                                    data["title"],
        #                                                                                    data["code"],
        #                                                                                    data["parent"],
        #                                                                                    data["type"],
        #                                                                                    data["ministryoffinancecode"],
        #                                                                                    data[
        #                                                                                        "ministryoffinancecodeoftownship"],)
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
        #
        # def removeLocation(self, data, _id, _from, node):
        #     q = "SELECT removeLocation('%s','%s') AS res" % (data['userid'],
        #                                                      data['id'])
        #     res = self.sm.database.singleFieldQuerySync(q)
        #     return res
