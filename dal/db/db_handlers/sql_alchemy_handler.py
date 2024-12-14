from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from dal_example.dal.db.db_handler import DBHandler


class SqlAlchemyConsts:
    URL = "url"


class SqlAlchemyHandler(DBHandler):

    def __init__(self, **kwargs):
        super().__init__()
        self.__connection_kwargs = kwargs
        self.__connection_string = self.__connection_kwargs.pop(SqlAlchemyConsts.URL, None)
        self._connection: Engine | None = None
        self._session_maker: sessionmaker | None = None

    def connect(self):
        self._connection = create_engine(self.__connection_string, **self.__connection_kwargs)
        self._session_maker = sessionmaker(bind=self.connection)

    def disconnect(self):
        self._connection.dispose()

    @property
    def connection(self) -> Engine:
        return self._connection

    @property
    def session(self) -> Session:
        return self._session_maker()
