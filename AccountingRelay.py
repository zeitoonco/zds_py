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
        q = "SELECT getConfig('%s') AS res" % (data['name'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def setConfig(self, data, _id, _from, node):
        q = "SELECT setConfig('%s','%s') AS res" % (data['name'], data['value'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newFiscalYear(self, data, _id, _from, node):
        q = "SELECT newFiscalYear('%s','%s','%s') AS res" % (data['title'], data['start'], data['end'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyFiscalYear(self, data, _id, _from, node):
        q = "SELECT modifyFiscalYear('%s','%s','%s','%s') AS res" % (
            int(data['id']), data['title'], data['start'], data['end'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def closeFiscalYear(self, data, _id, _from, node):
        q = "SELECT closeFiscalYear('%s') AS res" % (int(data['id']))
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeFiscalYear(self, data, _id, _from, node):
        q = "SELECT removeFiscalYear('%s') AS res" % (int(data['id']))
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newAccount(self, data, _id, _from, node):
        q = "SELECT newAccount('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}','{6:s}','{7:s}','{8:s}','{9:s}','{10:s}','{11:s}','{12:s}','{13:s}') AS res".format(
            data["parent"], data["type"], data["code"], data["title"], data["title2"], data["isactive"],
            data["cashflowcategory"], data["openingbalance"], data["balancetype"], data["hasbaancetypecheck"],
            data["hasdl"], data["hascurrency"], data["hascurrencyconversion"], data["hastracking"],
            data["hastrackingcheck"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyAccount(self, data, _id, _from, node):
        q = "SELECT modifyAccount('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}',{6:s},'{7:s}','{8:s}','{9:s}','{10:s}','{11:s}','{12:s}','{13:s}') AS res".format(
            data["id"], data["parent"], data["type"], data["code"], data["title"], data["title2"], data["isactive"],
            data["cashflowcategory"], data["balancetype"], data["hasbaancetypecheck"], data["hasdl"],
            data["hascurrency"], data["hascurrencyconversion"], data["hastracking"],
            data["hastrackingcheck"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeAccount(self, data, _id, _from, node):
        q = "SELECT removeAccount('%s') AS res" % (int(data['id']))
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newDl(self, data, _id, _from, node):
        q = "SELECT newDl('%s','%s','%s','%s','%s') AS res" % (
            data['code'], data['title'], data['title2'], data['type'], data['isactive'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyDL(self, data, _id, _from, node):
        q = "SELECT modifyDL('%s','%s','%s','%s','%s','%s') AS res" % (
            data['id'], data['code'], data['title'], data['title2'], data['type'], data['isactive'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeDL(self, data, _id, _from, node):
        q = "SELECT removeDL('%s') AS res" % (data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def activeDL(self, data, _id, _from, node):
        q = "SELECT activeDL('%s') AS res" % (data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def deactiveDL(self, data, _id, _from, node):
        q = "SELECT deactiveDL('%s') AS res" % (data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newCategory(self, data, _id, _from, node):
        q = "SELECT newCategory('%s','%s','%s') AS res" % (data['title'], data['type'], data['category'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyCategory(self, data, _id, _from, node):
        q = "SELECT modifyCategory('%s','%s','%s','%s') AS res" % (
            data['id'], data['title'], data['type'], data['category'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeCategory(self, data, _id, _from, node):
        q = "SELECT removeCategory('%s') AS res" % (data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newTopic(self, data, _id, _from, node):
        q = "SELECT newTopic('%s','%s','%s') AS res" % (data['title'], data['parent'], data['category'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyTopic(self, data, _id, _from, node):
        q = "SELECT modifyTopic('%s','%s','%s','%s') AS res" % (
            data['id'], data['title'], data['parent'], data['category'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeTopic(self, data, _id, _from, node):
        q = "SELECT removeTopic('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def addAccountTopic(self, data, _id, _from, node):
        q = "SELECT addAccountTopic('%s','%s') AS res" % (
            data['account'], data['topic'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeAccountTopic(self, data, _id, _from, node):
        q = "SELECT removeAccountTopic('%s','%s') AS res" % (
            data['account'], data['topic'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newVoucher(self, data, _id, _from, node):
        q = "SELECT newVoucher('%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data['number'], data['date'], data['referencenumber'], data['secondarynumber'], data['state'], data['type'],
            data['description'], data['dailynumber'], data['issuersystem'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyVoucher(self, data, _id, _from, node):
        q = "SELECT modifyVoucher('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data['id'], data['number'], data['date'], data['referencenumber'], data['secondarynumber'], data['state'],
            data['type'],
            data['description'], data['dailynumber'], data['issuersystem'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeVoucher(self, data, _id, _from, node):
        q = "SELECT removeVoucher('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def finalizeVoucher(self, data, _id, _from, node):
        q = "SELECT finalizeVoucher('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newVoucherItem(self, data, _id, _from, node):
        q = "SELECT newVoucherItem('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}',{6:s},'{7:s}','{8:s}','{9:s}','{10:s}','{11:s}','{12:s}') AS res".format(
            data["voucherid"], data["rownumber"], data["accountid"], data["dlid"], data["debit"], data["credit"],
            data["currencyid"], data["currencyrate"], data["currencydebit"], data["currencycredit"],
            data["trackingnumber"], data["trackingdate"], data["description"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyVoucherItem(self, data, _id, _from, node):
        q = "SELECT modifyVoucherItem('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}',{6:s},'{7:s}','{8:s}','{9:s}','{10:s}','{11:s}','{12:s}','{13:s'}) AS res".format(
            data["id"], data["voucherid"], data["rownumber"], data["accountid"], data["dlid"], data["debit"],
            data["credit"], data["currencyid"], data["currencyrate"], data["currencydebit"], data["currencycredit"],
            data["trackingnumber"], data["trackingdate"], data["description"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeVoucherItem(self, data, _id, _from, node):
        q = "SELECT removeVoucherItem('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newGLVoucher(self, data, _id, _from, node):
        q = "SELECT newGLVoucher('%s','%s') AS res" % (
            data['number'], data['date'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeGLVoucher(self, data, _id, _from, node):
        q = "SELECT removeGLVoucher('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newGLVoucherItem(self, data, _id, _from, node):
        q = "SELECT newGLVoucherItem('%s') AS res" % (
            data['voucherid'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeGLVoucherItem(self, data, _id, _from, node):
        q = "SELECT removeGLVoucherItem('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newCash(self, data, _id, _from, node):
        q = "SELECT newCash('%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data['title'], data['DL'], data['currency'], data['rate'], data['firstamount'], data['firstdate'],
            data['balance'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyCash(self, data, _id, _from, node):
        q = "SELECT modifyCash('%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data['id'], data['title'], data['DL'], data['currency'], data['rate'], data['firstamount'],
            data['firstdate'],
            data['balance'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeCash(self, data, _id, _from, node):
        q = "SELECT removeCash('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newCostCenter(self, data, _id, _from, node):
        q = "SELECT newCostCenter('%s','%s') AS res" % (
            data['dlid'], data['type'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyCostCenter(self, data, _id, _from, node):
        q = "SELECT modifyCostCenter('%s','%s','%s') AS res" % (
            data['id'], data['dlid'], data['type'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeCostCenter(self, data, _id, _from, node):
        q = "SELECT removeCostCenter('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newParty(self, data, _id, _from, node):
        q = "SELECT newParty('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data["type"], data["subtype"], data["name"], data["lastname"], data["nameEng"], data["lastnameEng"],
            data["economiccode"], data["identificationcode"], data["website"], data["email"], data["dlid"],
            data["blacklist"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyParty(self, data, _id, _from, node):
        q = "SELECT modifyParty('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data["id"], data["type"], data["subtype"], data["name"], data["lastname"], data["nameEng"],
            data["lastnameEng"],
            data["economiccode"], data["identificationcode"], data["website"], data["email"], data["dlid"],
            data["blacklist"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeParty(self, data, _id, _from, node):
        q = "SELECT removeParty('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def addPartyBlacklist(self, data, _id, _from, node):
        q = "SELECT addPartyBlacklist('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removePartyBlacklist(self, data, _id, _from, node):
        q = "SELECT removePartyBlacklist('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newBank(self, data, _id, _from, node):
        q = "SELECT newBank('%s','%s') AS res" % (
            data['title'], data['logo'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyBank(self, data, _id, _from, node):
        q = "SELECT modifyBank('%s','%s') AS res" % (
            data['title'], data['logo'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeBank(self, data, _id, _from, node):
        q = "SELECT removeBank('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newBankAccountType(self, data, _id, _from, node):
        q = "SELECT newBankAccountType('%s','%s') AS res" % (
            data['title'], data['hascheque'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyBankAccountType(self, data, _id, _from, node):
        q = "SELECT modifyBankAccountType('%s','%s','%s') AS res" % (
            data['id'], data['title'], data['hascheque'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeBankAccountType(self, data, _id, _from, node):
        q = "SELECT removeBankAccountType('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newBankAccount(self, data, _id, _from, node):
        q = "SELECT newBankAccount('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data["bankbranchid"],
            data["accountno"],
            data["bankaccounttypeid"],
            data["dlid"],
            data["currencyid"],
            data["rate "],
            data["firstamount "],
            data["firstdate "],
            data["balance "],
            data["billfirstamount "],
            data["clearformatname "],
            data["owner"],)
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyBankAccount(self, data, _id, _from, node):
        q = "SELECT modifyBankAccount('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data["id"], data["bankbranchid"],
            data["accountno"],
            data["bankaccounttypeid"],
            data["dlid"],
            data["currencyid"],
            data["rate "],
            data["firstamount "],
            data["firstdate "],
            data["balance "],
            data["billfirstamount "],
            data["clearformatname "],
            data["owner"],)
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeBankAccount(self, data, _id, _from, node):
        q = "SELECT removeBankAccount('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newBankBranch(self, data, _id, _from, node):
        q = "SELECT newBankBranch('%s','%s','%s','%s') AS res" % (
            data['bankid'], data['code'], data['title'], data['locationid'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyBankBranch(self, data, _id, _from, node):
        q = "SELECT modifyBankBranch('%s','%s','%s','%s','%s') AS res" % (
            data['id'], data['bankid'], data['code'], data['title'], data['locationid'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeBankBranch(self, data, _id, _from, node):
        q = "SELECT removeBankBranch('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newCurrency(self, data, _id, _from, node):
        q = "SELECT newCurrency('%s','%s','%s','%s','%s','%s') AS res" % (
            data["title"],
            data["exchangeunit"],
            data["precisioncount"],
            data["precisionname"],
            data["precisionnameEng"],
            data["sign"],)
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyCurrency(self, data, _id, _from, node):
        q = "SELECT modifyCurrency('%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data["id"],
            data["title"],
            data["exchangeunit"],
            data["precisioncount"],
            data["precisionname"],
            data["precisionnameEng"],
            data["sign"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeCurrency(self, data, _id, _from, node):
        q = "SELECT removeCurrency('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newCurrencyExchangeRate(self, data, _id, _from, node):
        q = "SELECT newCurrencyExchangeRate('%s','%s','%s') AS res" % (
            data["currency"],
            data["effectivedate"],
            data["exchangerate"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyCurrencyExchangeRate(self, data, _id, _from, node):
        q = "SELECT modifyCurrencyExchangeRate('%s','%s','%s','%s') AS res" % (
            data["id"],
            data["currency"],
            data["effectivedate"],
            data["exchangerate"])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeCurrencyExchangeRate(self, data, _id, _from, node):
        q = "SELECT removeCurrencyExchangeRate('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def newLocation(self, data, _id, _from, node):
        q = "SELECT newLocation('%s','%s','%s','%s','%s','%s') AS res" % (
            data["title"],
            data["code"],
            data["parent"],
            data["type"],
            data["ministryoffinancecode"],
            data["ministryoffinancecodeoftownship"],)
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def modifyLocation(self, data, _id, _from, node):
        q = "SELECT modifyLocation('%s','%s','%s','%s','%s','%s','%s') AS res" % (
            data["id"],
            data["title"],
            data["code"],
            data["parent"],
            data["type"],
            data["ministryoffinancecode"],
            data["ministryoffinancecodeoftownship"],)
        res = self.sm.database.singleFieldQuerySync(q)
        return res

    def removeLocation(self, data, _id, _from, node):
        q = "SELECT removeLocation('%s') AS res" % (
            data['id'])
        res = self.sm.database.singleFieldQuerySync(q)
        return res
