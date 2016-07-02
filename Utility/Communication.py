# coding=utf-8
import random


class Communication:
    def __init__(self):
        pass

    @staticmethod
    def get_random_id():
        return random.random

    @staticmethod
    def make_command(node, data, _id="", _from="", session=""):
        return ('{"type" : "call" , "node" : "' + node + '" ' +
                (', "id" : "' + _id + '" ' if len(_id) > 0 else "") +
                (', "from" : "' + _from + '" ' if len(_from) > 0 else "") +
                (', "data" : ' + data + " " if len(data) > 0 else "") +
                (', "session" : ' + session + " " if len(session) > 0 else "") +
                "}")

    @staticmethod
    def make_callback(node, data, _id="", _from=""):
        return ('{"type" : "callback" , "node" : "' + node + '" ' +
                (', "id" : "' + _id + '" ' if len(_id) > 0 else "") +
                (', "from" : "' + _from + '" ' if len(_from) > 0 else "") +
                (', "data" : ' + data + " " if len(data) > 0 else "") +
                "}")

    @staticmethod
    def make_event(node, _from, data):
        return ('{"type" : "fire" , "node" : "' + node + "\" " +
                (', "from" : "' + _from + '" ' if len(_from) > 0 else "") +
                (', "data" : ' + data + " " if len(data) > 0 else "") +
                "}")

    @staticmethod
    def make_error(node, _id, desc):
        return ('{"type" : "call" , "node" : "error" , "data" : {"node" : "' +
                node + '" , "id" : "' + _id + '" , "description" : "' + desc + "\"} }")
