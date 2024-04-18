from flask_sqlalchemy import SQLAlchemy
import datetime
from config import db

class CompraProducto(db.Model):
    __tablename__ = 'Compra_producto'

    idCompraProducto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreProducto = db.Column(db.String(30))
    cantidad = db.Column(db.Float)
    medida = db.Column(db.String(25)),
    subTotal = db.Column(db.Double),
    idProveedor = db.Column(db.Integer, db.ForeignKey('Proveedor.idProveedor'))
    idMP = db.Column(db.Integer, db.ForeignKey('MP.idMP'))
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class CompraTotal(db.Model):
    __tablename__ = 'Compra_total'

    idCompraTotal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idCompraProducto = db.Column(db.Integer, db.ForeignKey('Compra_producto.idCompraProducto'))
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    ticket = db.Column(db.String(30))
    total = db.Column(db.Float)
    fecha_compra = db.Column(db.String(15))