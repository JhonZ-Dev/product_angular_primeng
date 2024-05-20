from .models import Product
from .db import db
from datetime import date



#Función para obtener todos
def get_all_productos():
    products =  Product.query.all()
    return [product.to_dict() for product in products]

#Función para obtener producto por id
def get_product_by_id(id_producto):
    return Product.query.get(id_producto)

#Funcion para crear el producto
def create_product(nombreproducto,precioproducto, 
detalleproducto,
ivaproducto,
urlImagen,
sistema):
    #calcular el precio total incluytendo el iva
    preciototal = precioproducto + (precioproducto *(ivaproducto / 100))

    #crear la instancia del producto
    new_product = Product(
        nombreproducto = nombreproducto,
        precioproducto = precioproducto,
        detalleproducto = detalleproducto,
        ivaproducto = ivaproducto,
        preciototal = preciototal,
        fechacreacion = date.today(),
        urlImagen = urlImagen,
        sistema = sistema
    )
    db.session.add(new_product)
    db.session.commit()
    return new_product