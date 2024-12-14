from enum import Enum
from typing import Type

from pydantic import BaseModel

from dal_example.dal.dao.dao import DataAccessObject
from dal_example.dal.dao.daos.notification_dao import NotificationDAO
from dal_example.dal.db.db_handler import DBHandler
from dal_example.dal.db.db_handlers.sql_alchemy_handler import SqlAlchemyHandler
from dal_example.dal.repository.repositiories.notification_repository import NotificationRepository


class Repositories(Enum):
    NOTIFICATION_REPOSITORY = NotificationRepository


class DALConfig(BaseModel):
    db_properties: dict
    db_handler: Type[DBHandler]
    dao: Type[DataAccessObject]
    repository: Repositories


CONFIGS = [
    DALConfig(
        repository=Repositories.NOTIFICATION_REPOSITORY,
        db_properties={
            "url": "sqlite:///notifications.db",
        },
        db_handler=SqlAlchemyHandler,
        dao=NotificationDAO
    )
]
