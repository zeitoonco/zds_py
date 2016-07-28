import json


class InstallInfo:
    '''
    "name" : "$$$servicename" ,
    "title" : "$$$ Service Title" ,
    "version" : "$$$3" ,
    "commands" : [
                    {"name" : "$$$name" , "inputdatatype" : "$$$datatype1" , "inputdatatypeversion" : "$$$2" , "outputdatatype" : "$$$datatype2" , "outputdatatypeversion" : "$$$1"} ,
                    {"name" : "$$$name2" , "inputdatatype" : "$$$datatype3" , "inputdatatypeversion" : "$$$1" , "outputdatatype" : "$$$datatype4" , "outputdatatypeversion" : "$$$10"}
                    , ... ] ,
    "events" : [ {"name" : "$$$name" , "datatype" : "$$$datatype2" , "datatypeversion" : "$$$3"} , ... ] ,
    "hooks" : [ {"name" : "$$$eventname" , "datatype" : "$$$datatype2" , "datatypeversion" : "$$$3"} , ... ] ,
    "requirements" : [ {"name" : "$$$servicename" , "version" : "$$$minversion" } , ... ] ,
    "datatypes" : [ {"name" : "$$$datatypename" , "version" : "$$$123"} , ... ] ,
    } }

    '''
    commands = []
    events = []
    hooks = []
    requirements = []
    datatypes = []

    def toJSON(self):
        return json.dumps(dict(self.__dict__, **{"commands": self.commands, "events": self.events, "hooks": self.hooks,
                                                 "requirements": self.requirements, "datatypes": self.datatypes}))
