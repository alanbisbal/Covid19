from flask import jsonify
from app.db import connection
from app.models.issue import Issue
from app import db
from flask import request


def index():
    issues = db.query(Issue).all()
    return jsonify(issues=issues)
