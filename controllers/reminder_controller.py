from models.reminder import Reminder
from mongoengine.errors import DoesNotExist, ValidationError
from datetime import datetime


def _serialize(r: Reminder):
    d = r.to_mongo().to_dict()
    d['id'] = str(d.pop('_id'))
    # ensure created_at is ISO string
    if isinstance(d.get('created_at'), datetime):
        d['created_at'] = d['created_at'].isoformat()
    return d


def create_reminder(data: dict):
    reminder = Reminder(
        title=data.get('title'),
        detail=data.get('detail', ''),
        status=data.get('status', 'pendiente')
    )
    reminder.save()
    return _serialize(reminder)


def list_reminders():
    reminders = Reminder.objects()
    return [_serialize(r) for r in reminders]


def get_reminder(reminder_id: str):
    try:
        r = Reminder.objects.get(id=reminder_id)
        return _serialize(r)
    except DoesNotExist:
        return None


def update_reminder(reminder_id: str, data: dict):
    try:
        r = Reminder.objects.get(id=reminder_id)
        # only update allowed fields
        if 'title' in data:
            r.title = data['title']
        if 'detail' in data:
            r.detail = data['detail']
        if 'status' in data:
            r.status = data['status']
        r.save()
        return _serialize(r)
    except DoesNotExist:
        return None


def delete_reminder(reminder_id: str):
    try:
        r = Reminder.objects.get(id=reminder_id)
        r.delete()
        return True
    except DoesNotExist:
        return False
