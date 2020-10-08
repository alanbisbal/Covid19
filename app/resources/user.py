from flask import redirect, render_template, request, url_for, session, abort
from app.db import connection
from app.models.user import User
from app.helpers.auth import authenticated
from app import db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)
    users = User.all()
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)
    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)

    conn = connection()

    User.create(conn, request.form)
    return redirect(url_for("user_index"))


def update(user_id):
    if not authenticated(session):
        abort(401)

    user = User.find_by_id(user_id)
    return render_template("user/update.html",user = user)

def update_new():
    if not authenticated(session):
        abort(401)
    data =request.form
    User.update(data,data['user_id'])
    return redirect(url_for('user_index'))
