from .db import db

#modelo 
class Product(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    nombreproducto = db.Column(db.String(80), nullable=False)
    precioproducto = db.Column(db.Float, nullable=False)
    detalleproducto = db.Column(db.String(255), nullable=False)
    ivaproducto = db.Column(db.Float, nullable=False)
    preciototal = db.Column(db.Float, nullable=True)
    fechaactualizacion = db.Column(db.Date(), nullable=True)
    fechacreacion = db.Column(db.Date(), nullable=False)
    urlImagen = db.Column(db.String(80), nullable=False)
    sistema = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'<Product {self.name}>'
    def __repr__(self):
        return f'<Product {self.nombreproducto}>'
    
    def to_dict(self):
        data = {
            'id_producto': self.id_producto,
            'nombreproducto': self.nombreproducto,
            'precioproducto': self.precioproducto,
            'detalleproducto': self.detalleproducto,
            'ivaproducto': self.ivaproducto,
            'preciototal': self.preciototal,
            'urlImagen': self.urlImagen,
            'sistema': self.sistema
        }

        if self.fechaactualizacion is not None:
            data['fechaactualizacion'] = self.fechaactualizacion.isoformat()

        if self.fechacreacion is not None:
            data['fechacreacion'] = self.fechacreacion.isoformat()

        return data
    


    
        
