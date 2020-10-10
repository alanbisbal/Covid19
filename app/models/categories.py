from app import db
from flask import request


class Categorie(db.Model):
    ____tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key = True)


def __init__(self, data):
    self.name = data['name']
    db.session.commit()


@classmethod
def __str__(self):
    return '<categories {}>'.format(self.name)
