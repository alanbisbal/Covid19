from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
                    TimeField, IntegerField, SelectField, BooleanField, \
                    DateField, FloatField, DecimalField
from flask_wtf.file import FileField
from wtforms.validators import InputRequired, NumberRange, Regexp, DataRequired, Optional,EqualTo,Regexp
from wtforms.fields.html5 import EmailField
from app.models.tipo_centro import Tipo_centro
from app.models.estado import Estado
from wtforms.widgets.html5 import NumberInput
import requests
from app.models.turno import Turno
import requests, time
# from flask_wtf.file import FileField, FileAllowed, FileRequired

class CenterForm(FlaskForm):
    nombre = StringField('Nombre',validators =[InputRequired()])
    direccion = StringField('Direccion',validators =[InputRequired()])
    telefono =StringField('Telefono',validators =[InputRequired()])
    hora_inicio = TimeField('Hora de apertura',default=time,validators =[InputRequired()])
    hora_fin = TimeField('Hora de cierre',default= time,validators =[InputRequired()])
    municipio_id = SelectField('Municipio',validate_choice=False, choices=[])
    web = StringField('Sitio Web',validators =[InputRequired()])
    email = EmailField('Email',validators =[InputRequired()])
    protocolo = FileField(label="Protocolo",validators =[Optional(strip_whitespace=True)])
    latitud = FloatField('Latitud (coordenadas)',default="-34.9159",widget=NumberInput(),validators =[InputRequired()])
    longitud = FloatField('Longitud (coordenadas)',default="-57.9924",widget=NumberInput(),validators =[InputRequired()])
    estado_id = SelectField('Estado',validate_choice=False)
    tipo_centro = SelectField('Tipo',validators =[InputRequired()])
    submit = SubmitField(label="Guardar")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        tipos = Tipo_centro.all()
        estados = Estado.all()
        choices = []
        for _type in tipos:
            choices.append((_type.id, _type.nombre))
        self.tipo_centro.choices = choices
        choices = []
        for _type in estados:
            choices.append((_type.id, _type.nombre))
        self.estado_id.choices = choices
        choices = []
        municipios= requests.get("https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios").json()['data']['Town']
        for mun in municipios:
            choices.append((municipios[mun]["id"], municipios[mun]["name"]))
        self.municipio_id.choices = choices

class TurnoForm(FlaskForm):
    email = EmailField('Email',validators =[InputRequired()])
    telefono = StringField('Telefono')
    hora_inicio = SelectField('Hora inicio',validate_choice=False)
    fecha = DateField('Fecha', format='%Y-%m-%d',validators =[InputRequired()])
    centro_id = IntegerField('')

class NewTurnoForm(FlaskForm):
    fecha = DateField('Fecha', format='%Y-%m-%d',validators =[InputRequired()])
    centro_id = SelectField('nombre de centro', validators =[InputRequired()])

class SearchForm(FlaskForm):
    email =  StringField('Email')
    centro = SelectField('nombre de centro', validators =[InputRequired()])

class ConfigForm(FlaskForm):
    titulo = StringField('Titulo',validators =[InputRequired()])
    descripcion = StringField('Descripcion',validators =[InputRequired()])
    email = StringField('Email',validators =[InputRequired()])
    elementos = IntegerField('Cantidad de elementos por pagina',validators =[InputRequired(),NumberRange(min=1, max=50)], widget=NumberInput(step=1, min=1, max=50))
   # estado = SelectField('estado',validators =[InputRequired()],choices=[ 'habilitado','deshabilitado'])
