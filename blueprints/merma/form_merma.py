from wtforms import Form
from wtforms import PasswordField, EmailField, StringField, RadioField, SelectField, IntegerField, DateField
from wtforms import validators

class ProduccionForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    cantidad_m = IntegerField("Cantidad Merma",[
        validators.DataRequired(message='El campo es requerido'),
    ])
    cantidad_v = IntegerField("Cantidad Lote",[
        validators.DataRequired(message='El campo es requerido'),
    ])