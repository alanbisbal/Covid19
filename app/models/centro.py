from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import tipo_centro,turno

class Centro(db.Model):
    __tablename__ = 'centros'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion =  db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    hora_inicio = db.Column(db.Time(timezone=True),nullable=False)
    hora_fin = db.Column(db.Time(timezone=True),nullable=False)
    municipio_id = db.Column(db.String(255), nullable=False)
    web = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    estado =  db.Column(db.Boolean, nullable=False)
    protocolo = db.Column(db.String(255), nullable=False)
    coordenadas = db.Column(db.String(255), nullable=False)
    tipo_centro = db.Column(db.Integer, db.ForeignKey('tipo_centros.id'))
    turnos = db.relationship("Turno",backref= "centros")

    def __init__(self, data,id):
        self.nombre = data['nombre']
        self.direccion = data['direccion']
        self.telefono = data['telefono']
        self.hora_inicio = data['hora_inicio']
        self.hora_fin =  data['hora_fin']
        self.municipio_id = id
        self.web = data['web']
        self.email = data['email']
        if data['estado'] == 'y':
            self.estado = 1
        else:
            self.estado = 0
        self.protocolo = data['protocolo']
        self.coordenadas = data['coordenadas']
        self.type = data['type']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Centro {}>'.format(self.nombre)


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
        if self.nombre != data['nombre']:
            self.nombre = data['nombre']
        if self.direccion != data['direccion']:
            self.direccion = data['direccion']
        if self.telefono != data['telefono']:
            self.telefono = data['telefono']
        if self.hora_inicio != data['hora_inicio']:
            self.hora_inicio = data['hora_inicio']
        if self.hora_fin != data['hora_fin']:
            self.hora_fin = data['hora_fin']
        if self.municipio_id != id:
            self.municipio_id = id
        if self.web != data['web']:
            self.web = data['web']
        if self.email != data['email']:
            self.email = data['email']
        if data['estado'] == 'y':
            self.estado = 1
        else:
            self.estado = 0
        if self.protocolo != data['protocolo']:
            self.protocolo = data['protocolo']
        if self.coordenadas != data['coordenadas']:
            self.coordenadas = data['coordenadas']
        if self.type != data['type']:
            self.type = data['type']
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def with_filter(filter):
        return db.session.query(Centro).filter(Centro.nombre.contains(filter))

    def active_with_filter(filter):
        return db.session.query(Centro).filter(Centro.estado == True,Centro.nombre.contains(filter))

    def deactive_with_filter(filter):
        return db.session.query(Centro).filter(Centro.estado == False,Centro.nombre.contains(filter))
