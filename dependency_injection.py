"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import json
import uuid
from abc import ABC, abstractmethod


class DBConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save(self, obj) -> str:
        pass


class PostgreSQLConnect(DBConnector):
    def connect(self):
        print('PostgreSQL connect')

    def execute(self, sql: str) -> None:
        print(sql)

    def get_data(self, obj) -> dict:
        return {name: getattr(obj, name) for name in vars(obj) if not name.startswith('_')}

    def save(self, obj) -> str:
        data = self.get_data(obj)
        data.update({'id': str(uuid.uuid4())})
        self.execute(json.dumps(data))
        return data['id']


class MySQlConnect(DBConnector):
    def connect(self):
        print('MySQL connect')

    def execute(self, sql: str) -> None:
        print(sql)

    def get_data(self, obj) -> dict:
        return {name: getattr(obj, name) for name in vars(obj) if not name.startswith('_')}

    def save(self, obj) -> str:
        data = self.get_data(obj)
        data.update({'id': str(uuid.uuid4())})
        self.execute(json.dumps(data))
        return data['id']


class User:
    def __init__(self, dbconnect: DBConnector, *args, **kwargs):
        self.__dbconnect = dbconnect
        self.__tablename = 'user'

        self.id = kwargs.pop('id', None)
        self.username = kwargs.pop('username', None)
        self.email = kwargs.pop('email', None)

    def save(self):
        self.__dbconnect.connect()
        self.__dbconnect.save(obj=self)


if __name__ == '__main__':
    psql = MySQlConnect()
    user = User(psql, username='abc', email='abc@abc.pl')
    user.save()
