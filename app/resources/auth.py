from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection

from app.models.user import User
from app.models.config import Config
from app.helpers.permits import is_admin
from app.helpers.auth import authenticated
from app import db


def login():
    return render_template("auth/login.html")


def authenticate():
    """ 
    Este método realiza la autenticación de un usuario teniendo en cuenta si los datos ingresados son correctos,
    si el usuario se encuntra o no activo y si la pagina está o no habilitada

    """
    user = db.session.query(User).filter(
        User.username == request.form['username']).filter(
            User.password == request.form['password']).first()

    if not user:
        flash("Usuario o clave incorrecto.", "danger")
        return redirect(url_for("auth_login"))

    if not user.is_active():
        flash("Su usuario se encuentra desactivado.", "danger")
        return redirect(url_for("auth_login"))

    if not Config.getConfig().is_active():
        if not is_admin(user):
            flash("El sitio se encuentra en mantenimiento", "danger")
            return redirect(url_for("home"))
    session["user"] = user.email
    session["username"] = user.username
    flash("La sesión se inició correctamente.", "success")
    return redirect(url_for("home"))


def logout():
    """ 
    Este método verifica si el usuario esta logueado,de ser así lo desloguea

    """
    if not authenticated(session):
        return redirect(url_for("home"))
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.", "success")
    return redirect(url_for("auth_login"))
