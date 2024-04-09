from flask_wtf import FlaskForm
from wtforms import StringField, validators, FloatField, TextAreaField

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