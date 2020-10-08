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


    @classmethod
    def __str__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def all(self):
        return db.session.query(User).all()

    @classmethod
    def find_by_id(slef,id):
        return db.session.query(User).get(id)


    @classmethod

    def create(self, conn, data):

        sql = """
            INSERT INTO users (email, password, first_name, last_name)
            VALUES (%s, %s, %s, %s)
        """

        cursor = conn.cursor()
        cursor.execute(sql, list(data.values()))
        conn.commit()

        return True

    @classmethod
    def find_by_email_and_pass(self, conn, email, password):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email = %s AND u.password = %s
        """
        cursor = conn.cursor()
        cursor.execute(sql, (email, password))
        return cursor.fetchone()

    @classmethod
    def update(self,data,id):
        user = db.session.query(User).get(id)
        if user.first_name != data['first_name']:
            user.first_name = data['first_name']
        if user.username != data['username']:
            user.username = data['username']
        if user.last_name != data['last_name']:
            user.last_name = data['last_name']
        if user.email != data['email']:
            user.email = data['email']

        db.session.commit()
        return True
