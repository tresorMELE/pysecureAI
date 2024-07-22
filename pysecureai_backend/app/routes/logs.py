from flask import Blueprint, request, jsonify

bp = Blueprint('logs', __name__, url_prefix='/logs')

@bp.route('/', methods=['POST'])
def collect_logs():
    logs = request.get_json()
    # Analyse et stockage des logs
    return jsonify({'message': 'Logs collected successfully'}), 201
