from flask import Blueprint, request
from init import db, ma, bcrypt, jwt
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from models.address import Address, AddressSchema

address_bp = Blueprint('address',__name__, url_prefix='/address')

@address_bp.route('/register/address', methods=['POST'])
def auth_register():
    try:
        user_address = Address(
            address = request.json('address'),
            city = request.json('city'),
            state = request.json('state'),
            country = request.json('country'),
            id = request.json('User.id')
        )
        db.session.add(user_address)
        db.session.commit()
        return AddressSchema(exclude = ['password']).dump(user_address), 201
    except IntegrityError:
        return {'error': 'this user already has an address, use a patch to update the users details'}, 409

# Displays all the addresses in the database
@address_bp.route('/', methods=['GET'])
@jwt_required()
def get_addresses():
    stmt = db.select(Address)
    addresses = db.session.scalars(stmt)
    return AddressSchema(many=True).dump(addresses)

# User can find their address via their user_id
@address_bp.route('/<int:id>/')
@jwt_required()
def get_an_address(id):
    stmt = db.select(Address).filter_by(user_id=id)
    addresses = db.session.scalars(stmt)
    return AddressSchema(many=True).dump(addresses)


# for users to updating their address
@address_bp.route('/<int:id>/update/', methods=['PUT', 'PATCH'])
@jwt_required()
def alter_address(id):
    stmt = db.select(Address).filter_by(user_id=get_jwt_identity(),id=id)
    address = db.session.scalar(stmt)
    data = AddressSchema().load(request.json, partial=True)

    if address:
        address.street_number = data.get('street_number') or address.street_number
        address.street_name = data.get('street_name') or address.street_name
        address.suburb = data.get('suburb') or address.suburb
        address.postcode = data.get('postcode') or address.postcode

        db.session.commit()
        return AddressSchema().dump(address)
    else:
        return {'error': f'You do not have an address with id {id}.'}, 404