# coding=utf-8
import json
class DatabaseMediator:
    sm = None

    def __init__(self, ism):
        self.sm = ism

    def wrapSqlCmd(self, sql):
        return '{"query":"' + json.dumps(sql) + '"}'

    def query(self, cmd):
        self.sm.communication.runCommand("database.query", self.wrapSqlCmd(cmd))

    def querySync(self, cmd):
        pass

    def execute(self, cmd):
        self.sm.communication.runCommand("database.execute", self.wrapSqlCmd(cmd))

    def executeSync(self, cmd):
        pass

    def singleFieldQuery(self, cmd):  #from? which node? applies to all these methods
        self.sm.communication.runCommand("database.singlefieldquery", self.wrapSqlCmd(cmd))

    def singleFieldQuerySync(self, cmd):
        pass
