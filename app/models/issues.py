from app import db
from flask import request


class Issue(db.Model):
    ____tablename__ = 'issues'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255))
    description = db.Column(db.String(255))
    category = db.Column(db.Integer)
    status_id = db.Column(db.Integer)

def __init__(self, data):
    self.email = data['email']
    self.description = data['description']
    self.description = data['description']
    self.category = data['category']
    self.status_id = data['status_id']
    db.session.commit()


@classmethod
def __str__(self):
    return '<issues {}>'.format(self.email)
