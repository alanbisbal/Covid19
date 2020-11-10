from flask_wtf import FlaskForm
from wtforms import validators,StringField,PasswordField,SubmitField, TimeField,IntegerField,SelectField,BooleanField,DateField,FloatField
from wtforms.validators import InputRequired ,NumberRange,Regexp,DataRequired
from wtforms.fields.html5 import EmailField
from app.models.tipo_centro import Tipo_centro
from wtforms.widgets.html5 import NumberInput
import requests
from flask_wtf.file import FileField, FileAllowed, FileRequired

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
    protocolo = FileField('Protocolo')
    latitud = FloatField('latitud (coordenadas)',default="-34.9159",validators =[DataRequired()])
    longitud = FloatField('Longitud (coordenadas)',default="-57.9924",validators =[DataRequired()])
    estado_id = SelectField('Estado',validators =[InputRequired()])
    tipo_centro = SelectField('Tipo',validators =[InputRequired()])


class TurnoForm(FlaskForm):
    email = StringField('email',validators =[InputRequired()])
    telefono = StringField('telefono')
    hora_inicio = TimeField('hora_inicio',validators =[InputRequired()])
    hora_fin = TimeField('hora_fin',validators =[InputRequired()])
    fecha = DateField('fecha', format='%Y-%m-%d',validators =[InputRequired()])
    centro_id = IntegerField('centro_id',validators =[InputRequired()])

class ConfigForm(FlaskForm):
    titulo = StringField('titulo',validators =[InputRequired()])
    description = StringField('description',validators =[InputRequired()])
    email = StringField('email',validators =[InputRequired()])
    elementos = IntegerField('elementos',validators =[InputRequired()], widget=NumberInput(step=1, min=1, max=None))
   # estado = SelectField('estado',validators =[InputRequired()],choices=[ 'habilitado','deshabilitado'])


   
      
