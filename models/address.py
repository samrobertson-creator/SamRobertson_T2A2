from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)

    user = db.relationship('User', back_populates='addresses')

class AddressSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['first_name', 'last_name'])

    street_number = fields.String(required=True, validate=Regexp("^[0-9a-zA-Z.'#@%& -/]+$", error='Only numbers, letters, spaces and valid characters for addresses are allowed.'))
    street_name = fields.String(required=True, validate=Regexp("^[0-9a-zA-Z.'#@%& -/]+$", error='Only numbers, letters, spaces and valid characters for addresses are allowed.'))
    suburb = fields.String(required=True, validate=Regexp("^[a-zA-Z.'#@%& -/]+$", error='Only letters, spaces and valid characters for addresses are allowed.'))
    postcode = fields.String(required=True, validate=Regexp('^[0-9a-zA-Z]+$', error='Only numbers and letters are allowed.'))
    class Meta:
        fields = ('id', 'street_number', 'street_name', 'suburb', 'postcode', 'user_id', 'user')
        ordered = True