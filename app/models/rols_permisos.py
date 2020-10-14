from app import db
from flask import request
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

class Rols_permisos(db.Model):
    ____tablename__ = 'rols_permisos'
    id = db.Column(db.Integer,primary_key = True)
    rol_id = db.Column(db.Integer, db.ForeignKey('rols.id'))
    permiso_id = db.Column(db.Integer, db.ForeingKey('permisos.id'))
    rol = relationship(Rol, backref=backref("rols_permisos,cascade=all, delete-orphan"))
    permiso = relationship(Permiso, backref=backref("rols_permisos,cascade=all, delete-orphan"))

    def __init__(self, data):
        self.name = data['name']
        db.session.commit()
