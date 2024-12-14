from typing import Optional

from mongoengine import Document, StringField


class User(Document):
    id: str = StringField(primary_key=True)
    name: str = StringField(required=True)
    email: Optional[str] = StringField()

