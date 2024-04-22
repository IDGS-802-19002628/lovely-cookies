from wtforms import Form
from wtforms import StringField,FileField,FloatField,FieldList, HiddenField, SelectField,  IntegerField
from wtforms import validators
from wtforms.validators import ValidationError
from flask_wtf.file import FileField, FileAllowed

import re

class RecetaForm(Form):
 
    cantidad = StringField('Cantidad', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Regexp('^\d+(\.\d+)?$', message='Ingresa una cantidad válida')
    ])

    idMp= SelectField("Ingrediente",coerce=int)
    idGalleta = SelectField("Galleta", coerce=int)  # Se asume que se cargarán 
    nombreGalleta = HiddenField()


class GalletaForm(Form):
    idGalleta = IntegerField('Ingrediente',)
    nombre = StringField('Nombre')
    descripcion = StringField('Descripcion')
    precio=FloatField('Precio', validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=0, message='El precio debe ser mayor a cero')
    ])
    peso=FloatField('Peso', validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=0, message='El peso debe ser mayor a cero')
    ])
    imagen = FileField('Imagen', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imágenes!')])

class MpForm(Form):
    ingredientes = FieldList(SelectField('Ingrediente', coerce=int), min_entries=1)
