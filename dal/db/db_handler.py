from abc import abstractmethod, ABC


class DBHandler(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def connection(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def session(self):
        raise NotImplementedError
