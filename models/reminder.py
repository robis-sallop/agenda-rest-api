from datetime import datetime
from mongoengine import Document, StringField, DateTimeField


class Reminder(Document):
    title = StringField(required=True, max_length=200)
    detail = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
    status = StringField(default='pendiente')

    meta = {
        'collection': 'recordatorios'
    }
