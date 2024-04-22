from wtforms import Form
from wtforms import PasswordField, EmailField, StringField, RadioField, SelectField, IntegerField, DateField, TextAreaField
from wtforms import validators

class MermaForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    cantidad_m = IntegerField("Cantidad Merma",[
        validators.DataRequired(message='El campo es requerido'),
    ])
    galleta = StringField("Gallata",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])
    observaciones = TextAreaField("Observaciones",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])
    id_U = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])