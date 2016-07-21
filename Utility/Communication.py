# coding=utf-8
import logging
import random


class Communication:
    logger = logging.getLogger('Utility.Communication')

    def __init__(self):
        pass

    @staticmethod
    def get_random_id():
        return random.randint(100000000,999999999)

    @staticmethod
    def make_command(node, data, _id="", _from="", session=""):
        _id = str(_id)
        return ('{"type" : "call" , "node" : "' + node + '" ' +
                ((', "id" : "' + _id + '" ') if len(_id) > 0 else "") +
                ((', "from" : "' + _from + '" ') if len(_from) > 0 else "") +
                ((', "data" : ' + data + " ") if len(data) > 0 else "") +
                ((', "session" : ' + session + " ") if len(session) > 0 else "") +
                "}")

    @staticmethod
    def make_callback(node, data, _id="", _from=""):
        return ('{"type" : "callback" , "node" : "' + node + '" ' +
                ((', "id" : "' + _id + '" ') if len(_id) > 0 else "") +
                ((', "from" : "' + _from + '" ') if len(_from) > 0 else "") +
                ((', "data" : ' + data + " ") if len(data) > 0 else "") +
                "}")

    @staticmethod
    def make_event(node, _from, data):
        return ('{"type" : "fire" , "node" : "' + node + '" ' +
                ((', "from" : "' + _from + '" ') if len(_from) > 0 else "") +
                ((', "data" : ' + data + " ") if len(data) > 0 else "") +
                "}")

    @staticmethod
    def make_error(node, _id, desc):
        return ('{"type" : "call" , "node" : "error" , "data" : {"node" : "' +
                node + '" , "id" : "' + _id + '" , "description" : "' + desc + "\"} }")
