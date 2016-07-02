# coding=utf-8
import json


class SettingMediator:
    sm = None

    def __init__(self, ism):
        self.sm = ism

    def remove(self, name):
        self.sm.communication.runCommand("removesetting", '{"name" : "' + name + '"}')
        pass

    def add(self, name, defValue, isPublic=False, readOnly=False):
        self.sm.communication.runCommand('registersetting',
                                         '{"name" : "' + name + '" , "defvalue" : "' + defValue + '" , "public" : "' + str(
                                             isPublic) + '" , "readonly" : "' + str(readOnly) + '"}')

    def get(self, name):
        resp_data = self.sm.communication.runCommandSync("getsetting", '{"name" : "' + name + '"}')
        js = json.loads(resp_data)
        return js["value"]

    def getAsync(self, name):
        self.sm.communication.runCommand("getsetting", '{"name" : "' + name + '"}')

    def set(self, name, value):
        self.sm.communication.runCommand("setsetting",
                                         '{"name" : "' + name + '", "value" : "' + value + '"}')
