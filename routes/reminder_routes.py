from flask import Blueprint, request, jsonify
from controllers.reminder_controller import (
    create_reminder,
    list_reminders,
    get_reminder,
    update_reminder,
    delete_reminder,
)

reminder_bp = Blueprint('reminders', __name__)


@reminder_bp.route('/', methods=['POST'])
def create():
    data = request.get_json() or {}
    if 'title' not in data:
        return jsonify({'error': 'title is required'}), 400
    reminder = create_reminder(data)
    return jsonify(reminder), 201


@reminder_bp.route('/', methods=['GET'])
def list_all():
    reminders = list_reminders()
    return jsonify(reminders), 200


@reminder_bp.route('/<reminder_id>', methods=['GET'])
def detail(reminder_id):
    reminder = get_reminder(reminder_id)
    if not reminder:
        return jsonify({'error': 'not found'}), 404
    return jsonify(reminder), 200


@reminder_bp.route('/<reminder_id>', methods=['PUT'])
def edit(reminder_id):
    data = request.get_json() or {}
    reminder = update_reminder(reminder_id, data)
    if not reminder:
        return jsonify({'error': 'not found'}), 404
    return jsonify(reminder), 200


@reminder_bp.route('/<reminder_id>', methods=['DELETE'])
def remove(reminder_id):
    ok = delete_reminder(reminder_id)
    if not ok:
        return jsonify({'error': 'not found'}), 404
    return jsonify({'deleted': True}), 200
