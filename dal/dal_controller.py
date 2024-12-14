from typing import Type

from dal_example.dal.configs import CONFIGS
from dal_example.dal.repository.repository import Repository


class DALController:

    def __init__(self):
        self._configs = CONFIGS
        self.repositories = {}
        for config in self._configs:
            db_handler = config.db_handler(**config.db_properties)
            dao = config.dao(db_handler)
            repository = config.repository.value(dao)
            self.repositories[config.repository.name] = repository

    def get_repository(self, repository: Type[Repository]):
        return self.repositories[repository]


da = DALController()
print(da.repositories)
