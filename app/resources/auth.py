from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from app.models.user import User
from app import db


def login():
    return render_template("auth/login.html")


def authenticate():
    user = db.session.query(User).filter(User.email == request.form['email']).filter(User.password == request.form['password']).first()
    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    session["user"] = user.email
    session["username"] = user.username
    flash("La sesión se inició correctamente.")
    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
