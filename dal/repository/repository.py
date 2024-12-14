import uuid
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from dal_example.dal.dao.dao import DataAccessObject

Object = TypeVar("Object")
Dao = TypeVar('Dao', bound=DataAccessObject)


class Repository(ABC, Generic[Object, Dao]):
    def __init__(self, dao: Dao) -> None:
        self._dao = dao

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

    @property
    def dao(self) -> Dao:
        return self._dao
