from flask import request
from sqlalchemy.orm import relationship

from app.db import db

from sqlalchemy import Table, Column, Integer, ForeignKey

class Tipo_centro(db.Model):
    __tablename__ = 'tipo_centros'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, data):
        self.name = data['name']
        db.session.commit()

    @classmethod
    def __str__(self):
        return '<Tipo_centro {}>'.format(self.name)
