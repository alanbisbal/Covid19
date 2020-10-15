from flask import request
from sqlalchemy.orm import relationship
from app.models import issue
from app.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class Categorie(db.Model):
    ____tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    issues = db.relationship('Issue',backref='categories',lazy=True)

    


    def __init__(self, data):
        self.name = data['name']
        db.session.commit()


    @classmethod
    def __str__(self):
        return '<categories {}>'.format(self.name)
