from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey,Float,LargeBinary
from app.models import tipo_centro,turno,estado

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

    estado_id = db.Column(db.Integer, db.ForeignKey('estados.id'))
    estado =  db.relationship("Estado")

    protocolo = db.Column(db.LargeBinary)
    latitud = db.Column(db.Float(),nullable=False)
    longitud = db.Column(db.Float(),nullable=False)

    tipo_centro = db.Column(db.Integer, db.ForeignKey('tipo_centros.id'))
    tipo = db.relationship("Tipo_centro")

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
        self.estado_id = data['estado_id']
        self.protocolo = bytes(data['protocolo'],encoding='utf8')
        self.latitud = data['latitud']
        self.longitud = data['longitud']
        self.tipo_centro = data['tipo_centro']
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
        if self.estado_id != data['estado_id']:
            self.estado_id = data['estado_id']
        
        if self.latitud != data['latitud']:
            self.latitud = data['latitud']
        if self.longitud != data['longitud']:
            self.longitud = data['longitud']
        if self.tipo_centro != data['tipo_centro']:
            self.tipo_centro = data['tipo_centro']
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def with_filter(filter):
        return db.session.query(Centro).filter(Centro.nombre.contains(filter))

    def publicate(filter):
        return db.session.query(Centro).filter(Centro.estado.nombre == "Publicado",Centro.nombre.contains(filter))

    def despublicate(filter):
        return db.session.query(Centro).filter(Centro.estado.nombre == "Despublicado",Centro.nombre.contains(filter))

    def pending(filter):
        return db.session.query(Centro).filter(Centro.estado.nombre == "Pendiente",Centro.nombre.contains(filter))
