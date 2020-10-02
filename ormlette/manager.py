
from ormlette import connection


class Manager:
    def __init__(self, model, table):

        self.model = model
        self.table = table

    def get(self, **kwargs):
        filter_str = ' AND '.join([f'{col}=%({col})s' for col in list(kwargs)])
        command = f"""SELECT * FROM {self.table} WHERE {filter_str}"""
        cursor = connection.cursor()
        cursor.execute(command, kwargs)
        data = {col.name: val for col, val in zip(cursor.description, cursor.fetchone())}
        cursor.close()
        instance = self.model(**data)
        return instance
