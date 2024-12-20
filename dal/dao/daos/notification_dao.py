from typing import Type
from dal_example.dal.dao.generic_daos.sql_alchemy_dao import SqlAlchemyDAO
from dal_example.dal.db.db_handler import DBHandler
from dal_example.dal.db.db_handlers.sql_alchemy_handler import SqlAlchemyHandler
from dal_example.dal.models.notification import Notification


class NotificationDAO(SqlAlchemyDAO[Notification]):
    def __init__(self, db_handler: DBHandler):
        # Pass both db_handler and Notification model to the parent constructor
        super().__init__(db_handler, Notification)

    def find_by_user_id(self, user_id: int) -> list[Notification]:
        """Find all notifications for a specific user."""
        with self.db_handler.session as session:
            notifications = session.query(Notification).filter_by(user_id=user_id).all()
            return notifications

    def get_all_notifications(self) -> list[Notification]:
        with self.db_handler.session as session:
            notifications = session.query(Notification).all()
            return notifications
