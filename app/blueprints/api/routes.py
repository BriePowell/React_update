from . import bp as api
from flask import jsonify, request
from app.blueprints.auth.models import User

@api.route('/test')
def test():
    return 'This is a test'


@api.route('/users')
def get_users():
    """
    [GET] /api/users - returns all users
    """
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@api.route('/users/<id>')
def get_user(id):
    """
    [GET] /api/users/<user_id> - return user based on id
    """
    user = User.query.get_or_404(id)
    return jsonify({'test': id})

@api.route('/users', methods=['POST'])
def create_user():
    pass

@api.route('/users/<id>', methods=['PUT'])
def update_user():
    pass

@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    pass
