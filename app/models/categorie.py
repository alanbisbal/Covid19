from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from flask import request
from sqlalchemy.orm import relationship
from app.models import issue

class Categorie(db.Model):
    ____tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    issue_id = db.Column(db.Integer, db.ForeignKey('issues.id'))

    def __init__(self, data):
        self.name = data['name']
        db.session.commit()


    @classmethod
    def __str__(self):
        return '<Categorie {}>'.format(self.name)
