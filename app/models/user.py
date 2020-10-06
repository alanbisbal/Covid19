from app import db

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

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def all(cls):
        return db.session.query(User).all()


    @classmethod

    def create(cls, conn, data):

        sql = """
            INSERT INTO users (email, password, first_name, last_name)
            VALUES (%s, %s, %s, %s)
        """

        cursor = conn.cursor()
        cursor.execute(sql, list(data.values()))
        conn.commit()

        return True

    @classmethod
    def find_by_email_and_pass(cls, conn, email, password):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email = %s AND u.password = %s
        """
        cursor = conn.cursor()
        cursor.execute(sql, (email, password))
        return cursor.fetchone()
