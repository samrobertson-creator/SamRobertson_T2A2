from flask import Blueprint, request
from init import db
from models.products import Products, ProductSchema
from flask_jwt_extended import jwt_required

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/new_product/', methods=['POST'])
@jwt_required()
def add_product():
    product = Products(
        description = request.json.get('description'),
        brand = request.json.get('brand'),
        style = request.json.get('style'),
        category = request.json.get('category'),
        size = request.json.get('size'),
        price = request.json.get('price'),
        quantity = request.json.get('quantity')
    )

    db.session.add(product)
    db.session.commit()
    return ProductSchema().dump(product)

# This route views all available products
@products_bp.route('/', methods=['GET'])
@jwt_required()
def get_products():
    stmt = db.select(Products)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# This route sorts by Category
@products_bp.route('/<string:category>/', methods=['GET'])
@jwt_required()
def filter_by_category(category):
    stmt = db.select(Products).filter_by(category=category)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# This route sorts by Brand
@products_bp.route('/<string:brand>/', methods=['GET'])
@jwt_required()
def filter_by_brand(brand):
    stmt  = db.select(Products).filter_by(brand=brand)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# This route sorts by Style
@products_bp.route('/<string:style>/', methods=['GET'])
@jwt_required()
def filter_by_style(style):
    stmt = db.select(Products).filter_by(style=style)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# This route sorts by Price 
@products_bp.route('/<int:price>/', methods=['GET'])
@jwt_required()
def filter_by_price(price):
    stmt = db.select(Products).filter_by(price=price)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# This route sorts by Product ID
@products_bp.route('/<int:product_id>/', methods=['GET'])
@jwt_required()
def sort_by_product_id(product_id):
    stmt = db.select(Products).filter_by(product_id=product_id)
    products = db.session.scalars(stmt)
    if products:
        return ProductSchema(many=True).dump(products)
    else:
        return {'error': f'Product with id {id} not found'}, 404