from flask_sqlalchemy import SQLAlchemy
import datetime
from config import db


class InventarioG(db.Model):
    __tablename__ = 'inventario_g'
    
    idInventarioG = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idGalleta = db.Column(db.Integer, db.ForeignKey('galleta.idGalleta'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    
    # Relación con Galleta
    galleta = db.relationship('Galleta', backref='inventario_g')

class VentaTotal(db.Model):
    __tablename__ = 'venta_total'
    
    idVentaTotal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.String(30))
    total = db.Column(db.Float, nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    # Relación con Usuario
    usuario = db.relationship('Usuario', backref='venta_total')

class VentaGalleta(db.Model):
    __tablename__ = 'venta_galleta'
    
    idVentaGalleta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idGalleta = db.Column(db.Integer, db.ForeignKey('galleta.idGalleta'), nullable=False)
    idVentaTotal = db.Column(db.Integer, db.ForeignKey('venta_total.idVentaTotal'), nullable=False)
    subTotal = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    tipoVenta = db.Column(db.String(10), nullable=False)
    peso = db.Column(db.Float(10), nullable=False)
    
    # Relaciones con Galleta y VentaTotal
    galleta = db.relationship('Galleta', backref='venta_galleta')
    venta_total = db.relationship('VentaTotal', backref='venta_galleta')

class Cajach(db.Model):
    __tablename__ = 'cajach'
    
    idCajach = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total = db.Column(db.Float, nullable=False)

class Pago_p(db.Model):
    __tablename__ = 'pago_p'
    
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Float)  # Asegúrate de que esta línea esté en tu modelo
    fecha = db.Column(db.Date)