from flask import request
from sqlalchemy.orm import relationship
<<<<<<< HEAD
 
=======

>>>>>>> 8575660b5a51118cb48d5860bb7bc0a1b3c07c86
from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey
import bleach


class Config(db.Model):
    __tablename__ = 'configs'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False)
    elementos = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)

    def __init__(self, data):
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']
        self.email = data['email']
        self.elementos = data['elementos']
        self.estado = 1
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Config {}>'.format(self.email)

    def getConfig():
        return db.session.query(Config).first()

    def is_active(self):
        return self.estado

    def cant_elements(self):
        return self.elementos

    def activate(self):
        self.estado = True
        db.session.commit()

    def deactivate(self):
        self.estado = False
        db.session.commit()

    def update(self, data):
        self.titulo = bleach.clean(data['titulo'])
        self.descripcion = bleach.clean(data['descripcion'])
        self.email = bleach.clean(data['email'])
<<<<<<< HEAD
        self.elementos = data['elementos']
=======
        self.elementos = bleach.clean(data['elementos'])
>>>>>>> 8575660b5a51118cb48d5860bb7bc0a1b3c07c86
        if data['estado'] == "habilitado":
            self.estado = True
        else:
            self.estado = False
        db.session.commit()
