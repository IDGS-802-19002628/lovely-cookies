from flask_wtf import FlaskForm
from wtforms import InputRequired, EqualTo
from wtforms import Form, StringField, IntegerField, BooleanField, validators

class UserForm(FlaskForm):
    idUsuario = IntegerField('idUsuario', [validators.number_range(min=1, max=20, message='Valor no válido')])
    nomUsuario = StringField("Nombre de usuario", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=25, message="Ingresa un nombre de usuario válido")
    ])
    contraseña = StringField("Contraseña", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=255, message="Ingresa una contraseña válida")
    ])
    rol = IntegerField('Rol', [validators.number_range(min=1, max=100, message='Valor no válido')])
    estatus = BooleanField("Estatus")
    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=25, message="Ingresa un nombre válido")
    ])
    apellidoP = StringField("Apellido Paterno", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=25, message="Ingresa un apellido válido")
    ])
    apellidoM = StringField("Apellido Materno", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=25, message="Ingresa un apellido válido")
    ])
    telefono = StringField("Teléfono", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=10, message="Ingresa un teléfono válido")
    ])
    correo = StringField("Correo", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=30, message="Ingresa un correo válido")
    ])

class LoginForm(FlaskForm):
    nomUsuario = StringField("Nombre de usuario", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=25, message="Ingresa un nombre de usuario válido")
    ])
    contraseña = StringField("Contraseña", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=255, message="Ingresa una contraseña válida")])