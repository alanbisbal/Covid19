from flask import request
from sqlalchemy.orm import relationship
from sqlalchemy import between, and_
from sqlalchemy import asc
from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import centro
from datetime import datetime, time, timedelta, date
import bleach
 

class Turno(db.Model):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    hora_inicio = db.Column(db.Time(timezone=True), nullable=False)
    hora_fin = db.Column(db.Time(timezone=True), nullable=True)
    fecha = db.Column(db.Date)
    centro_id = db.Column(db.Integer, db.ForeignKey('centros.id'))
    centro = relationship("Centro", backref="centro")

    def __init__(self, data):
        self.email = bleach.clean(data['email'])
        self.telefono = bleach.clean(data['telefono'])
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

    def with_email_centro(email, centro):
        con_mail = db.session.query(Turno).filter(Turno.email.contains(email))
        con_centro = db.session.query(Turno).filter(
            Turno.centro.has(nombre=centro))
        return con_mail.intersect(con_centro)

    def with_id_fecha(id, fecha):
        return db.session.query(Turno).filter(Turno.centro_id == id).filter(
            Turno.fecha == fecha)

    def bloques_disponibles(id, fecha):
        """
        Retorna todos los turnos disponibles en bloques de 30 minutos para un id y fecha en particular
        ordenados por hora y minutos de manera ascendente.
        """
        bloques = []
        ocupados = []

        turnos = db.session.query(Turno).filter(Turno.centro_id == id).filter(
            Turno.fecha == fecha).all()

        for t in turnos:
            ocupados.append(t.hora_inicio.strftime("%H:%M"))

        for i in range(9, 16):
            for j in (00, 30):
                hora = str(i) + ":" + str(j)
                date_time = datetime.strptime(hora, "%H:%M")
                hora = date_time.strftime("%H:%M")
                bloques.append(str(hora))
        result = list(set(bloques) - set(ocupados))
        result = sorted(result)

        return result

    def with_next_two_date(centro_id):
        """
         Retorna los turnos para hoy y los siguientes 2 dias a partir de un centro en particular,
         ordenados por fecha y hora de manera ascendente.
        """
        hoy = datetime.today().replace(hour=0,
                                       minute=0,
                                       second=0,
                                       microsecond=0)
        en_dos_dias = datetime.today() + timedelta(days=2)

        return db.session.query(Turno).filter(
            Turno.centro_id == centro_id).filter(
                Turno.fecha.between(hoy, en_dos_dias)).order_by(
                    Turno.fecha.asc(), Turno.hora_inicio.asc())

    def with_next_two():
        """
         Retorna los turnos para hoy y los siguientes 2 dias,ordenados por fecha y hora de manera ascendente.
        """
        hoy = datetime.today().replace(hour=0,
                                       minute=0,
                                       second=0,
                                       microsecond=0)
        en_dos_dias = datetime.today() + timedelta(days=2)

        return db.session.query(Turno).filter(
            Turno.fecha.between(hoy,
                                en_dos_dias)).order_by(Turno.fecha.asc(),
                                                       Turno.hora_inicio.asc())

    def update(self, data):
        if self.email != data['email']:
            self.email = data['email']
        if self.telefono != data['telefono']:
            self.telefono = data['telefono']
        if self.hora_inicio != data['hora_inicio']:
            self.hora_inicio = data['hora_inicio']
        if self.hora_fin != datetime.strptime(
                data['hora_inicio'], "%H:%M:%S") + timedelta(minutes=30):
            self.hora_fin = datetime.strptime(
                data['hora_inicio'], "%H:%M:%S") + timedelta(minutes=30)
        if self.fecha != data['fecha']:
            self.fecha = data['fecha']
        db.session.commit()

    def add(data):
        db.session.add(Turno(data))
        db.session.commit()

    def add_and_return(data):
        turno = Turno(data)
        db.session.add(turno)
        db.session.commit()
        return turno

    def all():
        return db.session.query(Turno).all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
