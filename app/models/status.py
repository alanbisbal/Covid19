from flask import request
from sqlalchemy.orm import relationship
from app.models import issue
from app.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class Status(db.Model):
    ____tablename__ = 'statuses'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    issues = db.relationship('Issue',backref='statuses',lazy=True)

    def __init__(self, data):
        self.name = data['name']
        db.session.commit()


    @classmethod
    def __str__(self):
        return '<Status {}>'.format(self.name)
