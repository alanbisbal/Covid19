from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TimeField,IntegerField,DateField
from wtforms.validators import InputRequired as InputRequired

class CenterForm(FlaskForm):
    name = StringField('name',validators =[InputRequired()])
    address = StringField('address',validators =[InputRequired()])
    phone =StringField('phone',validators =[InputRequired()])
    open = TimeField('open',validators =[InputRequired()])
    close = TimeField('close',validators =[InputRequired()])
    municipio_id = IntegerField('municipio_id',validators =[InputRequired()])
    web = StringField('web',validators =[InputRequired()])
    email = StringField('email',validators =[InputRequired()])
    state = StringField('state',validators =[InputRequired()])
    protocol = StringField('protocol',validators =[InputRequired()])
    coordinates = StringField('coordinates',validators =[InputRequired()])
    type = StringField('type',validators =[InputRequired()])
    turnos = StringField('turnos',validators =[InputRequired()])

class TurnoForm(FlaskForm):
    email = StringField('email',validators =[InputRequired()])
    telefono = StringField('telefono',validators =[InputRequired()])
    hora_inicio = TimeField('hora_inicio',validators =[InputRequired()])
    hora_fin = TimeField('hora_fin',validators =[InputRequired()])
    fecha = DateField('fecha', format='%Y-%m-%d',validators =[InputRequired()])
    centro_id = IntegerField('centro_id',validators =[InputRequired()])
    
    
