from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
