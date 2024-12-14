import uuid
from typing import TypeVar, Type

from dal_example.dal.dao.dao import DataAccessObject, DbHandler
from dal_example.dal.db.db_handlers.sql_alchemy_handler import SqlAlchemyHandler

DeclarativeBase = TypeVar('DeclarativeBase')


class SqlAlchemyDAO(DataAccessObject[DeclarativeBase, SqlAlchemyHandler]):

    def __init__(self, db_handler: DbHandler, model_class: Type[DeclarativeBase]):
        super().__init__(db_handler)
        self.model_class = model_class

    def create(self, new_object: DeclarativeBase) -> DeclarativeBase:
        with self.db_handler.session as session:
            session.add(new_object)
            session.commit()
            session.refresh(new_object)
        return new_object

    def read(self, object_id: uuid) -> DeclarativeBase:
        with self.db_handler.session as session:
            return session.query(self.model_class).filter_by(id=object_id).first()

    def update(self, object_id: uuid, updated_object: DeclarativeBase) -> DeclarativeBase:
        with self.db_handler.session as session:
            db_object = session.query(self.model_class).filter_by(id=object_id).first()
            if db_object:
                for key, value in updated_object.__dict__.items():
                    setattr(db_object, key, value)
                session.commit()
                session.refresh(db_object)
            return db_object

    def delete(self, object_id: uuid) -> None:
        with self.db_handler.session as session:
            db_object = session.query(self.model_class).filter_by(id=object_id).first()
            if db_object:
                session.delete(db_object)
                session.commit()
