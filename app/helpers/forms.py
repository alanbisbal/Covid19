from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TimeField,IntegerField,SelectField,BooleanField,DateField, FileField
from wtforms.validators import InputRequired as InputRequired, regexp

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
    protocolo = FileField('Protocolo', validators= regexp(u'^[^/\\]\.pdf$')) #HABRIA QUE CAMBIARLO??

    coordenadas = StringField('Ubicacion (coordenadas)',validators =[InputRequired()])
    tipo_centro = SelectField('Tipo',validators =[InputRequired()])

class TurnoForm(FlaskForm):
    email = StringField('email',validators =[InputRequired()])
    telefono = StringField('telefono')
    hora_inicio = TimeField('hora_inicio',validators =[InputRequired()])
    hora_fin = TimeField('hora_fin',validators =[InputRequired()])
    fecha = DateField('fecha', format='%Y-%m-%d',validators =[InputRequired()])
    centro_id = IntegerField('centro_id',validators =[InputRequired()])
