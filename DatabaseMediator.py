# coding=utf-8
import json

from DataTypes.Structs import DSInteger, DSString
from DataTypes.TableString import DTTableString
from Utility.Communication import Communication


class DatabaseMediator:
    sm = None

    def __init__(self, ism):
        self.sm = ism

    def wrapSqlCmd(self, sql):
        j = {'query': sql}
        return json.dumps(j)

    def query(self, cmd):
        self.sm.communication.runCommand("database.query", self.wrapSqlCmd(cmd), cid=Communication.get_random_id())

    def querySync(self, cmd):
        return DTTableString("", self.sm.communication.runCommandSync("database.query", self.wrapSqlCmd(cmd),
                                                                      Communication.get_random_id()))

    def execute(self, cmd):
        self.sm.communication.runCommand("database.execute", self.wrapSqlCmd(cmd), cid=Communication.get_random_id())

    def executeSync(self, cmd):
        res = DSInteger(self.sm.communication.runCommandSync("database.execute", self.wrapSqlCmd(cmd),
                                                             Communication.get_random_id()))
        return res.value

    def singleFieldQuery(self, cmd):  # from? which node? applies to all these methods
        self.sm.communication.runCommand("database.singlefieldquery", self.wrapSqlCmd(cmd),
                                         cid=Communication.get_random_id())

    def singleFieldQuerySync(self, cmd):
        res = DSString(self.sm.communication.runCommandSync("database.singlefieldquery", self.wrapSqlCmd(cmd),
                                                            Communication.get_random_id()))

        return res.value
