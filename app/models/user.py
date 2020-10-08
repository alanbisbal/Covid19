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

    @classmethod
    def update(self,data):
        if self.first_name != data.first_name:
            self.first_name = data.first_name
        if self.username != data.username:
            self.username = data.username
        if self.first_name != data.first_name:
            self.first_name = data.first_name
        if self.last_name != data.last_name:
            self.last_name = data.last_name
        if self.activo != data.activo:
            self.activo = data.activo
        self.save()
        db.session.commit()
