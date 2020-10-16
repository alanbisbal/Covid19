from app import db
from flask import request
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import rol, users_rols

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), nullable=False, unique = True )
    email = db.Column(db.String(255), nullable=False, unique = True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, nullable=False)
    rols = db.relationship("Rol" , secondary="users_rols")

    def __init__(self, data):
        self.username = data['username']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.activo = 1
        db.session.commit()


    @classmethod
    def __str__(self):
        return '<User {}>'.format(self.username)
