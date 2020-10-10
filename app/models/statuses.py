from app import db
from flask import request


class Status(db.Model):
    ____tablename__ = 'statuses'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))


def __init__(self, data):
    self.name = data['name']
    db.session.commit()


@classmethod
def __str__(self):
    return '<statuses {}>'.format(self.name)
