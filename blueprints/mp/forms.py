from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,FloatField, SelectField
from wtforms import validators
from wtforms.validators import ValidationError
from wtforms.validators import DataRequired


class MPForm(FlaskForm):
    idMP = IntegerField('ID Ingrediente')
    ingrediente = StringField('Ingrediente', validators=[DataRequired()])
    medicion_choices = [('gr', 'gr'), ('ml', 'ml'), ('pz', 'pz')]
    medicion = SelectField('Medicion', choices=medicion_choices, validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    precio = FloatField('Precio', validators=[DataRequired()])