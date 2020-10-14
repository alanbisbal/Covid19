from app import db
from flask import request

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    activo = db.Column(db.Boolean)
    perfil = db.Column(db.String(255))

    def __init__(self, data):
        self.first_name = data['first_name']
        self.username = data['username']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.activo = 1
        db.session.commit()


    @classmethod
    def __str__(self):
        return '<User {}>'.format(self.username)
