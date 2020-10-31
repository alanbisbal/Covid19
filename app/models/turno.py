from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey


class Turno(db.Model):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),nullable=False)
    telefono =  db.Column(db.String(255),nullable=False)
    hora_inicio = db.Column(db.Time(timezone=True),nullable=False)
    hora_fin = db.Column(db.Time(timezone=True),nullable=False)
    fecha = db.Column(db.Date)
    centro_id = db.Column(db.Integer, db.ForeignKey('centros.id'))

    def __init__(self, data):
        self.email = data['email']
        self.telefono = data ['telefono']
        self.hora_inicio = data['hora_inicio']
        self.hora_fin = data['hora_fin']
        self.fecha = data['fecha']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Turno {}>'.format(self.email)

    def with_filter(filter):
        return db.session.query(Turno).filter(Turno.centro_id.contains(filter))

    def with_id(data):
        return db.session.query(Turno).get(data)

    #'bloque' no sabemos bien como definirlo
    def update(self,data):
        if self.email != data['email']:
            self.email = data['email']
        if self.email != data['telefono']:
            self.email = data['telefono']
        if self.hora_inicio != data['hora_inicio']:
            self.hora_inicio = data['hora_inicio']
        if self.hora_fin != data['hora_fin']:
            self.hora_fin = data['hora_fin']
        if self.fecha != data['fecha']:
            self.fecha = data['fecha']
        db.session.commit()


    def add(data):
        db.session.add(Turno(data))
        db.session.commit()


    def all():
        return db.session.query(Turno).all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

