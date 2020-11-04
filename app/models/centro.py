from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import tipo_centro

class Centro(db.Model):
    __tablename__ = 'centros'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address =  db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    open = db.Column(db.Time(timezone=True),nullable=False)
    close = db.Column(db.Time(timezone=True),nullable=False)
    municipio_id = db.Column(db.String(255), nullable=False)
    web = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    state =  db.Column(db.Boolean, nullable=False)
    protocol = db.Column(db.String(255), nullable=False)
    coordinates = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    #db.Column(Integer, ForeignKey('tipo_centros.id'))
    turnos = db.Column(db.String(255), nullable=False)
    #db.relationship("Turno",backref= "centros")#checkear el backref

    def __init__(self, data,id):
        self.name = data['name']
        self.address = data['address']
        self.phone = data['phone']
        self.open = data['open']
        self.close =  data['close']
        self.municipio_id = id
        self.web = data['web']
        self.email = data['email']
        if data['state'] == 'y':
            self.state = 1
        else:
            self.state = 0
        self.protocol = data['protocol']
        self.coordinates = data['coordinates']
        self.type = data['type']
        self.turnos = data['turnos']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Centro {}>'.format(self.name)


    def add(data,id):
        db.session.add(Centro(data,id))
        db.session.commit()


    def all():
        return db.session.query(Centro).all()

    def with_id(data):
        return db.session.query(Centro).get(data)

    def with_email(data):
        return db.session.query(Centro).filter_by(email = data).first()

    def update(self,data, id):
        if self.name != data['name']:
            self.name = data['name']
        if self.address != data['address']:
            self.address = data['address']
        if self.phone != data['phone']:
            self.phone = data['phone']
        if self.open != data['open']:
            self.open = data['open']
        if self.close != data['close']:
            self.close = data['close']
        if self.municipio_id != id
            self.municipio_id = id
        if self.web != data['web']:
            self.web = data['web']
        if self.email != data['email']:
            self.email = data['email']
        if data['state'] == 'y':
            self.state = 1
        else:
            self.state = 0
        if self.protocol != data['protocol']:
            self.protocol = data['protocol']
        if self.coordinates != data['coordinates']:
            self.coordinates = data['coordinates']
        if self.type != data['type']:
            self.type = data['type']
        if self.turnos != data['turnos']:
            self.turnos = data['turnos']
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
