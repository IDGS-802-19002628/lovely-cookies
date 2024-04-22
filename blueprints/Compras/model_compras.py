from flask_sqlalchemy import SQLAlchemy
import datetime
from config import db

class CompraProducto(db.Model):
    __tablename__ = 'Compra_producto'

    idCompraProducto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cantidad = db.Column(db.Float)
    subTotal = db.Column(db.Float)
    fecha_caducidad = db.Column(db.String(30))
    idProveedor = db.Column(db.Integer)
    idMP = db.Column(db.Integer)
    idCompraTotal = db.Column(db.Integer)
class CompraTotal(db.Model):
    __tablename__ = 'Compra_total'

    idCompraTotal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    ticket = db.Column(db.String(30))
    total = db.Column(db.Float)
    fecha_compra = db.Column(db.String(30))
    estatus = db.Column(db.Integer, default=0)