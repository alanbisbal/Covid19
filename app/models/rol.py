from app import db
from flask import request
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import permiso, user, users_rols, rols_permisos


class Rol(db.Model):
    __tablename__ = 'rols'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    users = db.relationship("User" , secondary="users_rols")
    permisos = db.relationship("Permiso", secondary="rols_permisos")

    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Rol {}>'.format(self.name)

    def all():
        return db.session.query(Rol).all()
