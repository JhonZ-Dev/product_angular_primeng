from .db import db

#modelo 
class Product(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    nombreproducto = db.Column(db.String(80), nullable=False)
    precioproducto = db.Column(db.Float, nullable=False)
    detalleproducto = db.Column(db.String(255), nullable=False)
    ivaproducto = db.Column(db.Float, nullable=False)
    preciototal = db.Column(db.Float, nullable=False)
    fechaactualizacion = db.Column(db.Date(), nullable=False)
    fechacreacion = db.Column(db.Date(), nullable=False)
    urlImagen = db.Column(db.String(80), nullable=False)
    sistema = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'<Product {self.name}>'
