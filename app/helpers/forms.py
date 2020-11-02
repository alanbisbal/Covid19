from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TimeField,IntegerField,SelectField
from wtforms.validators import InputRequired as InputRequired
import requests

class CenterForm(FlaskForm):
    data = requests.get("https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios").json()['data']['Town']
    dict={}
    for mun in data:
        dict[data[mun]['name']]=mun
    name = StringField('Nombre',validators =[InputRequired(message="El nombre de usuario es requerido")])
    address = StringField('Direccion',validators =[InputRequired()])
    phone =StringField('Telefono',validators =[InputRequired()])
    open = TimeField('Hora de apertura',validators =[InputRequired()])
    close = TimeField('Hora de cierre',validators =[InputRequired()])
    municipio_id = SelectField('Municipio',validate_choice=False ,choices= dict)
    web = StringField('Sitio Web',validators =[InputRequired()])
    email = StringField('Email',validators =[InputRequired()])
    state = StringField('Estado',validators =[InputRequired()])
    protocol = StringField('Protocolo',validators =[InputRequired()])
    coordinates = StringField('Ubicacion (coordenadas)',validators =[InputRequired()])
    type = StringField('Tipo',validators =[InputRequired()])
    turnos = StringField('Turnos',validators =[InputRequired()])
