from wtforms import Form
from wtforms import PasswordField, EmailField, StringField, RadioField, SelectField, IntegerField, DateField
from wtforms import validators

class ProduccionForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    cantidad = IntegerField("Cantidad",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="La cantodad valida")
    ])
    g = StringField("Galleta",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="La cantodad valida")
    ])
    fecha = DateField('Fecha de Produccion')
    estatus_choices = [('pendiente', 'Pendiente'),('proceso', 'Proceso'), ('terminado','Terminado')]
    estatus = SelectField("Estatus", choices=estatus_choices, validators=[validators.DataRequired(message='El campo es requerido')])

    status2_choices = [('proceso', 'Proceso'), ('terminado','Terminado')]
    estatus2 = SelectField("Estatus", choices=status2_choices, validators=[validators.DataRequired(message='El campo es requerido')])
    galletas = [('chocolate y menta', 'Chocolate y Menta'),('avena y nueces', 'Avena y Nueces'),  ('limón', 'Limón'), ('coco',' Coco'), ('chocolate blanco y arándanos','Chocolate Blanco y Arándanos'), ('almendra','Almendra'), ('mantequilla de maní','Mantequilla de Maní'), ('chía y coco', 'Chía y Coco'), ('almendra y naranja','Almendra y Naranja'), ('maiz','Maiz')]
    galleta = SelectField("Galletas", choices=galletas, validators=[validators.DataRequired(message='Es nesesario seleccionar una galleta')])