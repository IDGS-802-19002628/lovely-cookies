from wtforms import Form
from wtforms import PasswordField, EmailField, StringField, RadioField, SelectField, IntegerField, DateField
from wtforms import validators

class NotificacionForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    
    nombre_U = StringField('Nombre del personal')
    estatus_choices = [('normal', 'Normal'),('incremento', 'Incremento'), ('urgente','Urgente')]
    estatus = SelectField("Estatus", choices=estatus_choices, validators=[validators.DataRequired(message='El campo es requerido')])
    galletas = [('chocolate y menta', 'Chocolate y Menta'),('avena y nueces', 'Avena y Nueces'),  ('limón', 'Limón'), ('coco',' Coco'), ('chocolate blanco y arándanos','Chocolate Blanco y Arándanos'), ('almendra','Almendra'), ('mantequilla de maní','Mantequilla de Maní'), ('chía y coco', 'Chía y Coco'), ('almendra y naranja','Almendra y Naranja'), ('maiz','Maiz')]
    galleta = SelectField("Galletas", choices=galletas, validators=[validators.DataRequired(message='Es nesesario seleccionar una galleta')])