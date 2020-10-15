from app import db
from flask import request
from sqlalchemy import Table, Column, Integer, ForeignKey



class Config(db.Model):
    __tablename__ = 'configs'
    id = db.Column(db.Integer,primary_key = True)
    titulo = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    email = db.Column(db.String(255),nullable=False)
    elementos = db.Column(db.Integer,nullable=False)
    estado = db.Column(db.Boolean, nullable=False)

    def __init__(self, data):
        self.titulo = data['titulo']
        self.description = data['description']
        self.email = data['email']
        self.elementos = data['elementos']
        self.estado = 1
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Config {}>'.format(self.email)
