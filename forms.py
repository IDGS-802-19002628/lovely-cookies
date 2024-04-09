from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, BooleanField, validators, SelectMultipleField, FloatField, TextAreaField
from wtforms.validators import ValidationError

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
    captcha = StringField("Captcha", [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=1, max=10, message="Captcha incorrecto")])

class ProveedorForm(Form):
    nomEmpresa = StringField("Nombre de la empresa", [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=1, max=30, message="Ingresa un nombre de empresa válido")
    ])
    direccion = StringField("Dirección", [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=1, max=50, message="Ingresa una dirección válida")
    ])
    telefono = StringField("Teléfono", [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=1, max=10, message="Ingresa un teléfono válido")
    ])
    nomTrabajador = StringField("Nombre del trabajador", [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=1, max=30, message="Ingresa un nombre de trabajador válido")
    ])

class MateriaPForm(FlaskForm):
    ingredientes = SelectMultipleField("Ingredientes", coerce=int)

    def validate_ingredientes(form, field):
        if not field.data:
            raise ValidationError('Debes seleccionar al menos un ingrediente.')

class GalletaForm(FlaskForm):
    nombre = StringField('Nombre de la galleta', validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=1, max=25, message='Ingresa un nombre de galleta válido')])
    descripcion = TextAreaField('Descripción', validators=[
        validators.DataRequired(message='El campo es requerido')])
    precio = FloatField('Precio', validators=[
        validators.DataRequired(message='El campo es requerido')])
    peso = FloatField('Peso', validators=[
        validators.DataRequired(message='El campo es requerido')])