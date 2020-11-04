from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TimeField,IntegerField,SelectField,BooleanField
from wtforms.validators import InputRequired as InputRequired
from wtforms.fields.html5 import EmailField
import requests

class CenterForm(FlaskForm):
    data = requests.get("https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios").json()['data']['Town']
    dict={}
    for mun in data:
        dict[data[mun]['name']]=mun
    name = StringField('Nombre',validators =[InputRequired()])
    address = StringField('Direccion',validators =[InputRequired()])
    phone =StringField('Telefono',validators =[InputRequired()])
    open = TimeField('Hora de apertura',validators =[InputRequired()])
    close = TimeField('Hora de cierre',validators =[InputRequired()])
    municipio_id = SelectField('Municipio',validate_choice=False ,choices= dict)
    web = StringField('Sitio Web',validators =[InputRequired()])
    email = EmailField('Email',validators =[InputRequired()])
    state = BooleanField('Estado (publicado o despublicado)',validators =[InputRequired()], render_kw={'checked': True})
    protocol = StringField('Protocolo',validators =[InputRequired()])
    coordinates = StringField('Ubicacion (coordenadas)',validators =[InputRequired()])
    type = StringField('Tipo',validators =[InputRequired()])
    turnos = StringField('Turnos',validators =[InputRequired()])

class TurnoForm(FlaskForm):
    email = StringField('email',validators =[InputRequired()])
    telefono = StringField('telefono')
    hora_inicio = TimeField('hora_inicio',validators =[InputRequired()])
    hora_fin = TimeField('hora_fin',validators =[InputRequired()])
    fecha = DateField('fecha', format='%Y-%m-%d',validators =[InputRequired()])
    centro_id = IntegerField('centro_id',validators =[InputRequired()])
