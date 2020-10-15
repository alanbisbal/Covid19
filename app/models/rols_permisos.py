from app import db
from flask import request
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import rol ,permiso


class Rols_permisos(db.Model):
    ____tablename__ = 'rols_permisos'
    id = db.Column(db.Integer,primary_key = True)
    rol_id = db.Column(db.Integer, db.ForeignKey('rols.id'))
    permiso_id = db.Column(db.Integer, db.ForeignKey('permisos.id'))
    rol = db.relationship('Rol', backref=db.backref("rols_permisos",cascade="all, delete-orphan"))
    permiso = db.relationship('Permiso', backref=db.backref("rols_permisos",cascade="all, delete-orphan"))

    def __init__(self, data):
        self.name = data['name']
        db.session.commit()
