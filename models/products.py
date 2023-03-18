from init import db, ma 
from marshmallow import fields
from marshmallow.validate import OneOf

VALID_CATEGORY = ['Jackets', 'Pants', 'Ties', 'Business Shirts', 'Dress Shoes', 'Accessories']
VALID_BRAND = ['Hugo Boss', 'MJ Bale', 'Politix', 'Anthony Squries', 'Country Road']

class Products(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String)
    style = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class ProductSchema(ma.Schema):
    description = fields.String()
    category = fields.String(required=True, validate=OneOf(VALID_CATEGORY))
    brand = fields.String(required=True, validate=OneOf(VALID_BRAND))
    class Meta:
        fields = ('product_id', 'description', 'style', 'brand', 'category', 'size', 'price', 'quantity')
        ordered = True
