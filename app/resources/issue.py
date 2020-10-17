from flask import redirect, render_template, request, url_for
from app.db import connection
from app.models.issue import Issue
from app import db
# Public resources
def index():
    issues = Issue.all()
    return render_template("issue/index.html", issues=issues)

def new():
    return render_template("issue/new.html")


def create():
    Issue.add(request.form)
    return redirect(url_for("issue_index"))
