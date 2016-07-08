# coding=utf-8
class DatabaseMediator:
    sm = None

    def __init__(self, ism):
        self.sm = ism

    def wrap_sql_cmd(self, sql):
        pass

    def query(self, cmd):
        pass

    def query_sync(self, cmd):
        pass

    def execute(self, cmd):
        pass

    def execute_sync(self, cmd):
        pass

    def single_field_query(self, cmd):
        pass

    def single_field_query_sync(self, cmd):
        pass
