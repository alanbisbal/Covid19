from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey


class Turno(db.Model):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),nullable=False)
    #hora_inicio= db.Column(db.DateTime(timezone=True),nullable=False)
    #hora_fin= db.Column(db.DateTime(timezone=True),nullable=False)
    #fecha = Column(Date, index=True)
    centro_id = kasbfjdaklfn
    #usuario_id= db.Column(db.Integer, db.ForeignKey('user.id')

    def __init__(self, data):
        self.email = data['email']
        self.bloque = data['bloque']
        self.dia = data['dia']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Turno {}>'.format(self.email)
