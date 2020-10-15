from app import db
from flask import request
from sqlalchemy.orm import relationship
from app.models import categorie
from sqlalchemy import Table, Column, Integer, ForeignKey

class Issue(db.Model):
    ____tablename__ = 'issues'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    categorie = db.relationship('Categorie',backref='recordowner')
    status =  db.relationship('Status',backref='recordowner')

    def __init__(self, data):
        self.email = data['email']
        self.description = data['description']
        self.description = data['description']
        db.session.commit()

        cursor = conn.cursor()
        cursor.execute(sql, list(data.values()))
        conn.commit()

    @classmethod
    def __str__(self):
        return '<Issue {}>'.format(self.email)
