import json


class DTTableString:
    jsonData = {'rows': [], 'columns': []}

    def __init__(self, name, _receivedData=''):
        self.name = name
        if len(_receivedData) > 0:
            self.fromString(_receivedData)
        pass

    def rowCount(self):
        return len(self.jsonData['rows'])

    def columnCount(self):
        return len(self.jsonData['column'])

    def columnName(self, columnNumber):
        return self.jsonData["columns"][columnNumber]["name"]

    def columnDataType(self, columnNumber):
        return getattr(columnDataType, self.jsonData["columns"][columnNumber]["type"])

    def columnDataSize(self, columnNumber):
        return int(self.jsonData["columns"][columnNumber]["size"])

    def fieldValue(self, rowNumber, colNumber, ifNull=None):
        if ifNull is None:
            return self.jsonData["rows"][rowNumber][colNumber]
        else:
            return self.jsonData["rows"][rowNumber][colNumber] if self.jsonData["rows"][rowNumber][
                                                                      colNumber] is not None else ifNull

    def fieldIsNull(self, rowNumber, columnNumber):
        return True if self.jsonData["rows"][rowNumber][columnNumber] is None else False

    def fieldSize(self, rowNumber, columnNumber):
        pass;

    def fieldValueInt(self, rowNumber, colNumber, ifNull=0):
        return int(self.jsonData["rows"][rowNumber][colNumber]) if self.jsonData["rows"][rowNumber][
                                                                       colNumber] is not None else ifNull

    # Equivalent to std::string toString(int indent = -1, std::string indentContent = defaultIndentContent) const
    def __repr__(self):
        return json.dumps(self.jsonData)

    def fromString(self, data):
        self.jsonData = json.loads(data)

    # Necessary ?
    # DTBase &operator=(std::string)
    #
    # DTBase &operator=(DTBase &dtvar)
    #
    # bool operator==(DTBase &dtvar)
    #
    # bool operator!=(DTBase &dtvar)

    def columnRemove(self, name):
        index = -1
        for idx, val in self.jsonData['columns']:
            if val["name"] == name:
                index = idx
                break
        if index == -1:
            raise Exception("Invalid given column name.")
        self.columnRemoveAt(index)

    def columnRemoveAt(self, index):
        try:
            del self.jsonData["columns"][index]
        except:
            raise Exception("invalid column index")

        for idx, val in self.jsonData['rows']:
            del self.jsonData["rows"][idx][index]

    def columnAdd(self, name, dtype, size):
        self.jsonData["columns"].append({'name': name, 'datatype': dtype, 'size': size})
        for idx, val in self.jsonData['rows']:
            self.jsonData["rows"][idx].append(None)

    def rowAdd(self, row):
        if len(row) != len(self.jsonData['columns']):
            raise Exception("Invalid Row len")
        self.jsonData["rows"].append(row)

    def rowRemove(self, index):
        del self.jsonData["rows"][index]

    def clearRows(self):
        self.jsonData["rows"] = []

    def clear(self):
        self.jsonData["rows"] = {'rows': [], 'columns': []}


class columnDataType:
    TEXT = 1
    INTEGER = 2
    FLOAT = 3
    BINARY = 4
    BOOLEAN = 5
    DATE = 6
    UNKNOWN = 7
    __MAX = 8
