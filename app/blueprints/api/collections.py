from app.blueprints.api.models import Collection
from .import bp as api
from flask import json, jsonify, request
from .auth import token_auth
from app import db

@api.route('/collections/<int:id>', methods=['GET'])
@token_auth.login_required
def get_collection(id):
    return jsonify(Collection.query.get(id).to_dict())

