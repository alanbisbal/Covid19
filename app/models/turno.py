from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey 
from app.models import centro


class Turno(db.Model):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),nullable=False)
    telefono =  db.Column(db.String(255),nullable=False)
    hora_inicio = db.Column(db.Time(timezone=True),nullable=False)
    hora_fin = db.Column(db.Time(timezone=True),nullable=False)
    fecha = db.Column(db.Date)
    centro_id = db.Column(db.Integer, db.ForeignKey('centros.id'))
    centro = relationship("Centro", backref= "centro")

    def __init__(self, data):
        self.email = data['email']
        self.telefono = data ['telefono']
        self.hora_inicio = data['hora_inicio']
        self.hora_fin = data['hora_fin']
        self.fecha = data['fecha']
        self.centro_id = data['centro_id']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Turno {}>'.format(self.email)

    def with_centro_id(filter):
        return db.session.query(Turno).filter(Turno.centro_id == filter)

    def with_id(data):
        return db.session.query(Turno).get(data)

    def with_email(email):
        return db.session.query(Turno).filter(Turno.email.contains(email))

    def with_nombre_centro(data):
        return db.session.query(Turno).filter(Turno.centro.has(nombre=data))

    def with_email_centro_id(email,centro_id):
        return db.session.query(Turno).filter(Turno.email.contains(email)).filter(Turno.centro.has(nombre=centro))

    def with_email_centro(email,centro):
        con_mail = db.session.query(Turno).filter(Turno.email.contains(email))
        con_centro = db.session.query(Turno).filter(Turno.centro.has(nombre=centro))
        return con_mail.intersect(con_centro)

    def with_id_fecha(id,fecha):
       return db.session.query(Turno).filter(Turno.centro_id == id).filter(Turno.fecha == fecha) 



    #'bloque' no sabemos bien como definirlo
    def update(self,data):
        if self.email != data['email']:
            self.email = data['email']
        if self.telefono != data['telefono']:
            self.telefono = data['telefono']
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
