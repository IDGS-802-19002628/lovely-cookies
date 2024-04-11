from wtforms import Form
from wtforms import StringField,FloatField, HiddenField, SelectField,  IntegerField
from wtforms import validators
from wtforms.validators import ValidationError
import re

class RecetaForm(Form):
 
    cantidad = StringField('Cantidad', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Regexp('^\d+(\.\d+)?$', message='Ingresa una cantidad válida')
    ])

    idMp= SelectField("ID mp",coerce=int)
    idGalleta = SelectField("ID de Galleta", coerce=int)  # Se asume que se cargarán 
    nombreGalleta = HiddenField()


class GalletaForm(Form):
    idGalleta = IntegerField('ID de Materia')
    nombre = StringField('Nombre')
    descripcion = StringField('Descripcion')
    precio=FloatField('Precio')
    peso=FloatField('Peso')
    
