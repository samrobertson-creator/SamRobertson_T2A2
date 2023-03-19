from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.users import User
from models.products import Products
from models.address import Address
# from models.orders import Order

db_commands = Blueprint('db', __name__)

#General Commands for Database Management and Testing
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            full_name = 'Steven Stevenson',
            email='suitshopadmin@suits.com',
            password=bcrypt.generate_password_hash('123').decode('utf-8'),
            is_admin=True,
            street_number = '1000',
            street_name = 'Suit Street',
            suburb = 'Queens',
            postcode = '4000'
        ),
        User(
            full_name = 'Burt Macklin',
            email='burt@fbi.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8'),
            street_number = '99',
            street_name = 'Pit Street',
            suburb = 'The Pit',
            postcode = '4101'
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    addresses = [
        Address(
            street_number = '1000',
            street_name = 'Suit Street',
            suburb = 'Queens',
            postcode = '4000',
            user = users[0]
        ),

        Address(
            street_number = '99',
            street_name = 'Pit Street',
            suburb = 'The Pit',
            postcode = '4101',
            user = users[1]
        )
    ]
    db.session.add_all(addresses)
    db.session.commit()

    products = [
        Products(
            description = 'Navy Blue Jacket',
            brand = 'MJ Bale',
            category = 'jackets',
            size = '40',
            price = '$399',
            quantity = '2'
        ),
        Products(
            description = 'White Slim Fit Shirt',
            brand = 'Anthony Squires',
            category = 'Business Shirts',
            size = '41',
            price = '$109',
            quantity = '3'
        ),
        Products(
            description = 'Black Regular Fit Trouser',
            brand = 'Hugo Boss',
            category = 'Pants',
            size = '36',
            price = '$249',
            quantity = '1'
        ),
        Products(
            description = 'Cream Cotton Linen Jacket',
            brand = 'Country Road',
            category = 'Jackets',
            size = '40',
            price = '$349',
            quantity = '4'
        ),
        Products(
            description = 'Black Bow Tie',
            brand = 'Politix',
            category = 'Ties',
            size = 'NA',
            price = '$99',
            quantity = '5'
        )
    ]
    db.session.add_all(products)
    db.session.commit()

    print('Tables Created & Seeded')