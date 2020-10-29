from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import tipo_centro, turno

class Centro(db.Model):
    __tablename__ = 'centros'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion =  db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    hora_apertura = db.Column(db.DateTime(timezone=True),nullable=False)
    hora_cierre = db.Column(db.DateTime(timezone=True),nullable=False)
    municipio = db.Column(db.String(255), nullable=False)
    web = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    estado =  db.Column(db.Boolean, nullable=False)
    protocolo = db.Column(db.String(255), nullable=False)
    coordenadas = db.Column(db.String(255), nullable=False)
    tipo = db.Column(Integer, ForeignKey('tipo_centros.id'))
    turnos = db.relationship("Turno", backref='centro') #backref relacion bidireccional
 
    

    def __init__(self, data):
        self.nombre = data['nombre']
        self.direccion = data['direccion']
        self.telefono = data['telefono']
        self.hora_apertura = data['hora_apertura']
        self.hora_cierre = data['hora_cierre']
        self.municipio = data['municipio']
        self.web = data['web']
        self.email = data['email']
        self.estado = data['estado']
        self.protocolo = data['protocolo']
        self.coordenadas = data['coordenadas']
        self.tipo = data['tipo']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Centro {}>'.format(self.nombre)
