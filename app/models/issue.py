class Issue(object):
    @classmethod
    def all(cls, conn):
        sql = "SELECT * FROM issues"

        cursor = conn.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    def __init__(self, data):
        self.email = data['email']
        self.description = data['description']
        self.description = data['description']
        self.category = data['category']
        self.status_id = data['status_id']
        db.session.commit()
=======
    @classmethod
    def create(cls, conn, data):
        sql = """
            INSERT INTO issues (email, description, category_id, status_id)
            VALUES (%s, %s, %s, %s)
        """
>>>>>>> f018ddabf2f4c5210b6fe5a5d4b231f8d35ae302

        cursor = conn.cursor()
        cursor.execute(sql, list(data.values()))
        conn.commit()

<<<<<<< HEAD
    @classmethod
    def __str__(self):
        return '<issues {}>'.format(self.email)
>>>>>>> d615a0aba5e1824d2261b3bf51976f98a8e2c4dd
=======
        return True
>>>>>>> f018ddabf2f4c5210b6fe5a5d4b231f8d35ae302
