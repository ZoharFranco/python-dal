from typing import Dict

from mongoengine import connect, connection
from pymongo import MongoClient
from pymongo.synchronous.database import Database

from dal_example.dal.db.db_handler import DBHandler


class MongoHandler(DBHandler):

    def __init__(self, host: str, db_name: str, **kwargs):
        super().__init__()
        self.connection_kwargs: Dict = kwargs
        self.host: str = host
        self.db_name: str = db_name
        self._connection: MongoClient | None = None
        self._session: Database | None = None

    def connect(self):
        connect(self.db_name, host=self.host, **self.connection_kwargs)
        self._connection: MongoClient = connection.get_connection()
        self._session: Database = self.connection.get_database(self.db_name)

    def disconnect(self):
        self._connection.close()

    @property
    def connection(self) -> MongoClient:
        return self._connection

    @property
    def session(self) -> Database:
        return self._session
