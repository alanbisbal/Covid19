from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

from app.models import rols_permisos,rol


class Permiso(db.Model):
    __tablename__ = 'permisos'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    rols = db.relationship("Rol", secondary="rols_permisos")

    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Permiso {}>'.format(self.name)
