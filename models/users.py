from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    # first_name = db.Column(db.String)
    # last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    addresses = db.relationship('Address', back_populates='user', cascade='all, delete')

    class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=And(
        Length(min=6, error='Password must be at least 6 characters long.'),
        Regexp('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W]).*$', error='Password must inlcude at least one uppercase letter, one lowercase letter, one digit and one non-word character.')
    ))
    first_name = fields.String(validate=Length(min=1, error='Name entered must contain at least 1 characters.'))
    last_name = fields.String()

    class Meta:
        fields = ('id', 'email', 'password', 'full_name', 'age', 'is_admin')

