from app import db
from flask import request

class Rol(db.Model):
    __tablename__ = 'rols'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        db.session.commit()


    @classmethod
    def __str__(self):
        return '<rols {}>'.format(self.name)
