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


    def __init__( request):
           self.stuff = []

    @db.reconstructor
    def init_on_load(self):
        self.stuff = []

    @classmethod
    def all(self):
        return db.session.query(User).all()

    @classmethod
    def __str__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def create(request):
        print (request)
        usuario = User(request)

        db.session.add(usuario)
        db.session.commit()

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
