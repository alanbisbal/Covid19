from flask import request
from sqlalchemy.orm import relationship
 
from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey, Float, LargeBinary
from app.models import tipo_centro, turno, estado
from app.models.estado import Estado
from app.helpers.upload import upload_pdf
import bleach


class Centro(db.Model):
    __tablename__ = 'centros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    hora_inicio = db.Column(db.Time(timezone=True), nullable=False)
    hora_fin = db.Column(db.Time(timezone=True), nullable=False)
    municipio_id = db.Column(db.String(255), nullable=False)
    web = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)

    estado_id = db.Column(db.Integer, db.ForeignKey('estados.id'))
    estado = db.relationship("Estado")

    protocolo = db.Column(db.String(255), nullable=True)
    latitud = db.Column(db.Float(), nullable=False)
    longitud = db.Column(db.Float(), nullable=False)

    tipo_centro = db.Column(db.Integer, db.ForeignKey('tipo_centros.id'))
    tipo = db.relationship("Tipo_centro")

    turnos = db.relationship("Turno", backref="centros")

    def __init__(self, data):
        self.nombre = data['nombre']
        self.direccion = data['direccion']
        self.telefono = data['telefono']
        self.hora_inicio = data['hora_inicio']
        self.hora_fin = data['hora_fin']
        self.municipio_id = data['municipio_id']
        self.web = data['web']
        self.email = data['email']
        self.estado_id = data['estado_id']

        self.latitud = data['latitud']
        self.longitud = data['longitud']
        self.tipo_centro = data['tipo_centro']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Centro {}>'.format(self.nombre)

    def add(data):
        centro = Centro(data)
        if data["protocolo"] is not None:
            centro.protocolo = bleach.clean(upload_pdf(data['protocolo']))
        db.session.add(centro)
        db.session.commit()
        return centro

    def all():
        return db.session.query(Centro).all()

    def with_id(data):
        return db.session.query(Centro).get(data)

    def with_email(data):
        return db.session.query(Centro).filter_by(email=data).first()

    def update(self, data):
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
        if self.municipio_id != data['municipio_id']:
            self.municipio_id = data['municipio_id']
        if self.web != data['web']:
            self.web = data['web']
        if self.email != data['email']:
            self.email = data['email']
        if data['protocolo'] is not None:
            self.protocolo = upload_pdf(data['protocolo'])
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
        publicado = db.session.query(Estado).filter(
            Estado.nombre == "Publicado").first()
        return db.session.query(Centro).filter(
            Centro.estado_id == publicado.id, Centro.nombre.contains(filter))

    def despublicate(filter):
        despublicado = db.session.query(Estado).filter(
            Estado.nombre == "Despublicado").first()
        return db.session.query(Centro).filter(
            Centro.estado_id == despublicado.id,
            Centro.nombre.contains(filter))

    def pending():
        pendiente = db.session.query(Estado).filter(
            Estado.nombre == "Pendiente").first()
        return db.session.query(Centro).filter(Centro.estado_id == "3")

    def pendiente(filter):
        pendiente = db.session.query(Estado).filter(
            Estado.nombre == "Pendiente").first()
        return db.session.query(Centro).filter(
            Centro.estado_id == pendiente.id, Centro.nombre.contains(filter))

    def publicar(self):
        self.estado_id = 1
        db.session.commit()

    def despublicar(self):
        self.estado_id = 2
        db.session.commit()

    def publicados():
        return db.session.query(Centro).filter_by(estado_id=1)

    @classmethod
    def count_approved(cls):
        """Retorna la cantidad total de centros aprobados"""
        return Centro.query.filter_by(estado_id=1).count()
