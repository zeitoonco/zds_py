# do not remove
import json


class DSString:
    value = ''

    def getStructName(self):
        return "DSString"

    def getStructVersion(self):
        return 1

    def __init__(self, data='', isJSON=False):
        if (isJSON):
            try:
                v = json.loads(data)
                self.value = v['value']
            except:
                raise
        elif 'value' in data:
            self.value = data["value"]
        else:
            self.value = data

    def __str__(self):
        return str(self.value)


class DSInteger(DSString):
    def getStructName(self):
        return "DSInteger"
