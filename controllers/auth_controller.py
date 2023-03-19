from flask import Blueprint, request
from init import db, ma, bcrypt, jwt
from flask_jwt_extended import create_access_token
from datetime import timedelta
from sqlalchemy.exc import IntegrityError
from models.users import User, UserSchema

auth_bp = Blueprint('auth',__name__, url_prefix='/auth')

@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        user = User(
        email = request.json('email'),
        name = request.json('name'),
        password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
        age = request.json('age'),
        )
        db.session.add(user)
        db.session.commit()

        return UserSchema(exclude = ['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'email is already in use, please use another'}, 409

@auth_bp.route('/login/', methods=['POST'])
def user_login():
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token}
    else:
        return {'error': 'Invalid email or password.'}, 401