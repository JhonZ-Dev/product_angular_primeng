from flask import Blueprint, request, jsonify
from .service import get_all_productos


product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = get_all_productos()
    return jsonify([product.name for product in products])

