from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash
import datetime

db = SQLAlchemy()
class Usuario(db.Model, UserMixin):
    idUsuario = db.Column(db.Integer, primary_key=True)  # Renombramos el atributo a 'id'
    nomUsuario = db.Column(db.String(25))
    contraseña = db.Column(db.String(255))
    rol = db.Column(db.Integer)
    estatus = db.Column(db.Boolean)
    nombre = db.Column(db.String(25))
    apellidoP = db.Column(db.String(25))
    apellidoM = db.Column(db.String(25))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(30))

    def get_id(self):
        return str(self.idUsuario)  # Convertimos el id a string

    def check_password(self, password):
        return check_password_hash(self.contraseña, password)

class Proveedor(db.Model):
    idProveedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomEmpresa = db.Column(db.String(30))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(10))
    nomTrabajador = db.Column(db.String(30))
    estatus = db.Column(db.Boolean)

class MateriaPrima(db.Model):
    idMateriaP = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingrediente = db.Column(db.String(30))
    descripcion = db.Column(db.Text)

class MP(db.Model):
    idMP = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingrediente = db.Column(db.String(30))
    descripcion = db.Column(db.Text)

class ingredienteProveedor(db.Model):
    idIngreProvee = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idProveedor = db.Column(db.Integer, db.ForeignKey('proveedor.idProveedor'))
    idMP = db.Column(db.Integer, db.ForeignKey('mp.idMP'))
    proveedor = db.relationship('Proveedor', backref=db.backref('ingredientes_proveedor', lazy=True))
    mp = db.relationship('MP', backref=db.backref('proveedores', lazy=True))

class Galleta(db.Model):
    idGalleta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(25))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float)
    peso = db.Column(db.Float)