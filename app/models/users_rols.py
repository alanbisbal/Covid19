from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

from app.models import user ,rol

class Users_rols(db.Model):
    ____tablename__ = 'users_rols'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rol_id = db.Column(db.Integer, db.ForeignKey('rols.id'))
    user = db.relationship('User', backref=db.backref("users_rols",cascade="all, delete-orphan"))
    rol = db.relationship('Rol', backref=db.backref("users_rols",cascade="all, delete-orphan"))

    def __init__(self, user_id,rol):
        self.user_id = user_id
        self.rol_id = rol
        db.session.commit()

    def add(user_id,rol_id):
        db.session.add(Users_rols(user_id,rol_id))
        db.session.commit()

    def with_userid_rolid(data):
        return db.session.query(Users_rols).filter(Users_rols.user_id == data['user_id'],Users_rols.rol_id == data['rol_id']).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
