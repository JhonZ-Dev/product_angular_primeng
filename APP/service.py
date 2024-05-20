from .models import Product
from .db import db


#Función para obtener todos
def get_all_productos():
    return Product.query.all()

#Función para obtener producto por id
def get_product_by_id(id_producto):
    return Product.query.get(id_producto)