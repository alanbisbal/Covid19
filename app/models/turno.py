from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey


class Turno(db.Model):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),nullable=False)
    telefono = db.Column(db.String(25),nullable=False)
    hora_inicio= db.Column(db.DateTime(timezone=True),nullable=False)
    hora_fin= db.Column(db.DateTime(timezone=True),nullable=False)
    fecha = Column(Date, index=True,nullable=False)
    centro_id = db.Column(db.Integer, db.ForeignKey('centro.id')

    def __init__(self, data):
        self.email = data['email']
        self.telefono = data['telefono']
        self.hora_inicio = data['hora_inicio']
        self.hora_fin = data['hora_fin']
        self.fecha = data['fecha']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Turno {}>'.format(self.email)
