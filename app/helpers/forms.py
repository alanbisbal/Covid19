from flask_wtf import FlaskForm
from wtforms import validators,StringField,PasswordField,SubmitField, TimeField,IntegerField,SelectField,BooleanField,DateField,FloatField
from wtforms.validators import InputRequired ,NumberRange,Regexp,DataRequired
from wtforms.fields.html5 import EmailField
from app.models.tipo_centro import Tipo_centro
import requests

class CenterForm(FlaskForm):
    data = requests.get("https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios").json()['data']['Town']
    municipios={}
    for mun in data:
        municipios[data[mun]['name']]=mun
    nombre = StringField('Nombre',validators =[InputRequired()])
    direccion = StringField('Direccion',validators =[InputRequired()])
    telefono =StringField('Telefono',validators =[InputRequired()])
    hora_inicio = TimeField('Hora de apertura',validators =[InputRequired()])
    hora_fin = TimeField('Hora de cierre',validators =[InputRequired()])
    municipio_id = SelectField('Municipio',validate_choice=False ,choices= municipios)
    web = StringField('Sitio Web',validators =[InputRequired()])
    email = EmailField('Email',validators =[InputRequired()])
    estado = BooleanField('Estado (publicado o despublicado)',validators =[InputRequired()], render_kw={'checked': True})
    protocolo = StringField('Protocolo',validators =[InputRequired()])
    latitud = FloatField('latitud (coordenadas)',default="-34.9159",validators =[DataRequired()])
    longitud = FloatField('Longitud (coordenadas)',default="-57.9924",validators =[DataRequired()])
    tipo_centro = SelectField('Tipo',validators =[InputRequired()])


class TurnoForm(FlaskForm):
    email = StringField('email',validators =[InputRequired()])
    telefono = StringField('telefono')
    hora_inicio = TimeField('hora_inicio',validators =[InputRequired()])
    hora_fin = TimeField('hora_fin',validators =[InputRequired()])
    fecha = DateField('fecha', format='%Y-%m-%d',validators =[InputRequired()])
    centro_id = IntegerField('centro_id',validators =[InputRequired()])
