from flask import redirect, render_template, request, url_for
from app.db import connection
from app.models.issue import Issue
from app import db
# Public resources
def index():
    issues = db.session.query(Issue).all()
    return render_template("issue/index.html", issues=issues)

def new():
    return render_template("issue/new.html")


def create():
    db.session.add(User(request.form))
    db.session.commit()

    return redirect(url_for("issue_index"))
