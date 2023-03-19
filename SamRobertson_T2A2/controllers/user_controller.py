from flask import Blueprint, request
from init import db, bcrypt
from models.users import User, UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/')
@jwt_required()
def list_all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)

@user_bp.route('/<int:id>/')
@jwt_required()
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'User with id {id} not found.'}, 404

@user_bp.route('/update/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_account():
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)
    
    data = UserSchema().load(request.json, partial=True)
    user.email = data.get('email') or user.email
    if data.get('password'):
        user.password = bcrypt.generate_password_hash(request.json.get('password')).decode('utf-8')
    user.first_name = data.get('first_name') or user.first_name
    user.last_name = data.get('last_name') or user.last_name

    db.session.commit()
    return UserSchema(exclude=['password']).dump(user)

@user_bp.route('/del_account', methods=["DELETE"])
@jwt_required()
def delete_account():
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)

    db.session.delete(user)
    db.session.commit()
    return {'message': f'Account "{user.email}" deleted successfully.'}