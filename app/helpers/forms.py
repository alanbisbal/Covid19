from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TimeField,IntegerField,SelectField
from wtforms.validators import InputRequired as InputRequired

class CenterForm(FlaskForm):
    name = StringField('name',validators =[InputRequired()])
    address = StringField('address',validators =[InputRequired()])
    phone =StringField('phone',validators =[InputRequired()])
    open = TimeField('open',validators =[InputRequired()])
    close = TimeField('close',validators =[InputRequired()])
    municipio_id = SelectField('municipio_id',validators =[InputRequired()],choices= [])
    web = StringField('web',validators =[InputRequired()])
    email = StringField('email',validators =[InputRequired()])
    state = StringField('state',validators =[InputRequired()])
    protocol = StringField('protocol',validators =[InputRequired()])
    coordinates = StringField('coordinates',validators =[InputRequired()])
    type = StringField('type',validators =[InputRequired()])
    turnos = StringField('turnos',validators =[InputRequired()])
