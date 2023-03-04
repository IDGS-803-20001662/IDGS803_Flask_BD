from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators # agregar validacion

# (FORM) -> Heredar de Forms los metodos y atributos
class UserForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Correo electrónico')
    