from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TimeField,IntegerField,SelectField
from wtforms.validators import InputRequired as InputRequired

class CenterForm(FlaskForm):
    name = StringField('Nombre',validators =[InputRequired(message="El nombre de usuario es requerido")])
    address = StringField('Direccion',validators =[InputRequired()])
    phone =StringField('Telefono',validators =[InputRequired()])
    open = TimeField('Hora de apertura',validators =[InputRequired()])
    close = TimeField('Hora de cierre',validators =[InputRequired()])
    municipio_id = SelectField('Municipio',validate_choice=False ,choices= [('1','La Plata'),('2','Avellaneda')])
    web = StringField('Sitio Web',validators =[InputRequired()])
    email = StringField('Email',validators =[InputRequired()])
    state = StringField('Estado',validators =[InputRequired()])
    protocol = StringField('Protocolo',validators =[InputRequired()])
    coordinates = StringField('Ubicacion (coordenadas)',validators =[InputRequired()])
    type = StringField('Tipo',validators =[InputRequired()])
    turnos = StringField('Turnos',validators =[InputRequired()])
