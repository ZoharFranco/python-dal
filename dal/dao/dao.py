import uuid
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pydantic import BaseModel

from dal_example.dal.db.db_handler import DBHandler

Object = TypeVar('Object')
DbHandler = TypeVar('DbHandler', bound=DBHandler)


class DataAccessObject(ABC, Generic[Object, DbHandler]):

    def __init__(self, db_handler: DbHandler):
        self._db_handler = db_handler
        self.connect()

    @property
    def db_handler(self) -> DbHandler:
        return self._db_handler

    def connect(self):
        self.db_handler.connect()

    def disconnect(self):
        self.db_handler.disconnect()

    @abstractmethod
    def create(self, new_object: Object) -> Object:
        raise NotImplementedError

    @abstractmethod
    def read(self, object_id: uuid) -> Object:
        raise NotImplementedError

    @abstractmethod
    def update(self, object_id: uuid, updated_object: Object) -> Object:
        raise NotImplementedError

    @abstractmethod
    def delete(self, object_id: uuid) -> None:
        raise NotImplementedError
