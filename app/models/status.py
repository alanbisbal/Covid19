from app import db
from flask import request
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
class Status(db.Model):
    ____tablename__ = 'statuses'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    issue_id = db.Column(db.Integer, db.ForeingKey('issues.id'))

    def __init__(self, data):
        self.name = data['name']
        db.session.commit()


    @classmethod
    def __str__(self):
        return '<Status {}>'.format(self.name)
