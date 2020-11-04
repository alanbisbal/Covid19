from flask import request
from sqlalchemy.orm import relationship

from app import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import centro

class Tipo_centro(db.Model):
    __tablename__ = 'tipo_centros'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    centros = db.relationship("Centro",backref= "centros")

    def __init__(self, data):
        self.nombre = data['nombre']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Tipo_centro {}>'.format(self.nombre)

    def all():
        return db.session.query(Tipo_centro).all()
