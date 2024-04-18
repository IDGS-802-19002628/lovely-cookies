from flask_sqlalchemy import SQLAlchemy
import datetime
from config import db

class Proveedor(db.Model):
    idProveedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomEmpresa = db.Column(db.String(30))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(10))
    nomTrabajador = db.Column(db.String(30))
    estatus = db.Column(db.Boolean)
    
class ingredienteProveedor(db.Model):
    idIngreProvee = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idProveedor = db.Column(db.Integer, db.ForeignKey('proveedor.idProveedor'))
    idMP = db.Column(db.Integer, db.ForeignKey('mp.idMP'))
    proveedor = db.relationship('Proveedor', backref=db.backref('ingredientes_proveedor', lazy=True))
    #mp = db.relationship('MP', backref=db.backref('proveedores', lazy=True))
