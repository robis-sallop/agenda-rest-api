from flask import Blueprint, request, jsonify, current_app
from functools import wraps
from itsdangerous import URLSafeTimedSerializer as Serializer, BadSignature, SignatureExpired
from controllers.reminder_controller import (
    create_reminder,
    list_reminders,
    get_reminder,
    update_reminder,
    delete_reminder,
)

reminder_bp = Blueprint('reminders', __name__)


def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'authorization required'}), 401
        token = auth_header.replace('Bearer ', '', 1).strip()

        serializer = Serializer(current_app.config['SECRET_KEY'], salt='token-salt')
        try:
            serializer.loads(token, max_age=current_app.config['TOKEN_EXPIRATION_SECONDS'])
        except SignatureExpired:
            return jsonify({'error': 'token expired'}), 401
        except BadSignature:
            return jsonify({'error': 'invalid token'}), 401

        return f(*args, **kwargs)
    return decorated



@reminder_bp.route('/token', methods=['POST'])
def create_token():
    serializer = Serializer(current_app.config['SECRET_KEY'], salt='token-salt')
    token = serializer.dumps({'user': 'api-client'})
    return jsonify({
        'token': token,
        'expires_in': current_app.config['TOKEN_EXPIRATION_SECONDS']
    }), 200


@reminder_bp.route('/', methods=['POST'])
@require_token
def create():
    data = request.get_json() or {}
    if 'title' not in data:
        return jsonify({'error': 'title is required'}), 400
    reminder = create_reminder(data)
    return jsonify(reminder), 201


@reminder_bp.route('/', methods=['GET'])
@require_token
def list_all():
    reminders = list_reminders()
    return jsonify(reminders), 200


@reminder_bp.route('/<reminder_id>', methods=['GET'])
@require_token
def detail(reminder_id):
    reminder = get_reminder(reminder_id)
    if not reminder:
        return jsonify({'error': 'not found'}), 404
    return jsonify(reminder), 200


@reminder_bp.route('/<reminder_id>', methods=['PUT'])
@require_token
def edit(reminder_id):
    data = request.get_json() or {}
    reminder = update_reminder(reminder_id, data)
    if not reminder:
        return jsonify({'error': 'not found'}), 404
    return jsonify(reminder), 200


@reminder_bp.route('/<reminder_id>', methods=['DELETE'])
@require_token
def remove(reminder_id):
    ok = delete_reminder(reminder_id)
    if not ok:
        return jsonify({'error': 'not found'}), 404
    return jsonify({'deleted': True}), 200
