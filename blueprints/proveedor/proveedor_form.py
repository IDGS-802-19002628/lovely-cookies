from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, SelectMultipleField, ValidationError
from wtforms import validators

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