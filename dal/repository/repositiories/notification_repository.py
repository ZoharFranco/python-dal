import uuid

from dal_example.dal.dao.daos.notification_dao import NotificationDAO
from dal_example.dal.db.db_handlers.sql_alchemy_handler import SqlAlchemyHandler
from dal_example.dal.models.notification import Notification
from dal_example.dal.repository.repository import Repository


class NotificationRepository(Repository[Notification, NotificationDAO]):

    def create(self, new_object: Notification) -> Notification:
        return self.dao.create(new_object)

    def read(self, object_id: uuid) -> Notification:
        return self.dao.read(object_id)

    def update(self, object_id: uuid, updated_object: Notification) -> Notification:
        return self.dao.update(object_id, updated_object)

    def delete(self, object_id: uuid) -> None:
        self.dao.delete(object_id)

    def get_longest_notification(self) -> Notification:
        notifications = self.dao.get_all_notifications()
        return max(notifications, key=lambda notification: len(notification.message))

    def user_has_notifications(self, user_id: int) -> bool:
        notifications = self.dao.find_by_user_id(user_id)
        return len(notifications) > 0

    def get_all_user_notifications(self, user_id: int) -> list[Notification]:
        return self.dao.find_by_user_id(user_id)
