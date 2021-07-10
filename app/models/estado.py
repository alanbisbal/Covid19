from flask import request
from sqlalchemy.orm import relationship
from collections import defaultdict
 
from app import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import centro


class Estado(db.Model):
    __tablename__ = 'estados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    centros = db.relationship("Centro", backref="centros")

    def __init__(self, data):
        self.nombre = data['nombre']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Estado {}>'.format(self.nombre)

    def all():
        return db.session.query(Estado).all()

    def with_id(data):
        return db.session.query(Estado).get(data)
