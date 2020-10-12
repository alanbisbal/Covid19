from app import db
from flask import request


    @classmethod
    def create(cls, conn, data):
        sql = """
            INSERT INTO issues (email, description, category_id, status_id)
            VALUES (%s, %s, %s, %s)
        """


        return True
