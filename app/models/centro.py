from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import tipo_centro, turno

class Centro(db.Model):
    __tablename__ = 'centros'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address =  db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    open = db.Column(db.Time(timezone=True),nullable=False)
    close = db.Column(db.Time(timezone=True),nullable=False)
    municipio = db.Column(db.String(255), nullable=False)
    web = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    state =  db.Column(db.Boolean, nullable=False)
    protocol = db.Column(db.String(255), nullable=False)
    coordinates = db.Column(db.String(255), nullable=False)
    type = db.Column(Integer, ForeignKey('tipo_centros.id'))
    turnos = db.relationship("Turno",backref= "centros")#checkear el backref

    def __init__(self, data):
        self.name = data['name']
        self.address = data['address']
        self.phone = data['phone']
        self.open = data['open']
        self.close = data['close']
        self.municipio = data['municipio']
        self.web = data['web']
        self.email = data['email']
        self.state = data['state']
        self.protocol = data['protocol']
        self.coordinates = data['coordinates']
        self.type = data['type']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Centro {}>'.format(self.name)
