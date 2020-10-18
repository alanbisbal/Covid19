from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

from app.models import rol, users_rols, rols_permisos


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, nullable=False)
    rols = db.relationship("Rol", secondary="users_rols")

    def __init__(self, data):
        self.username = data['username']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.activo = 1
        self.perfil= "Admin"
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<User {}>'.format(self.username)

    def add(data):
        db.session.add(User(data))
        db.session.commit()

    def all():
        return db.session.query(User).all()

    def with_email(data):
        return db.session.query(User).filter_by(email = data).first()

    def with_username(data):
        return db.session.query(User).filter_by(username = data).first()

    def with_id(data):
        return db.session.query(User).get(data)

    def update(self,data):
        if self.first_name != data['first_name']:
            self.first_name = data['first_name']
        if self.username != data['username']:
            self.username = data['username']
        if self.last_name != data['last_name']:
            self.last_name = data['last_name']
        if self.email != data['email']:
            self.email = data['email']
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def with_filter(filter):
        return db.session.query(User).filter(User.username.contains(filter))

    def active_with_filter(filter):
        return db.session.query(User).filter(User.activo == True,User.username.contains(filter))

    def deactive_with_filter(filter):
        return db.session.query(User).filter(User.activo == False,User.username.contains(filter))

    def active(self):
        return self.activo

    def activate(self):
        self.activo = True
        db.session.commit()

    def deactivate(self):
        self.activo = False
        db.session.commit()

    def permit_recovery(self):
        permissions = []
        for rol in self.rols:
            permissions += rol.permission_names()
        return permissions

    def has_permisions(self, string):
        # el in chequea si una cosa está en otra
        # otra forma: self.permit_recovery().contains(string)
        return string in self.permit_recovery()
